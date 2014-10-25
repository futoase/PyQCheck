# -*- coding:utf-8 -*-

import re
import sys
import traceback
import marshal
from arbitrary import Arbitrary


class PropResult:
    def __init__(self):
        self.succeeded = None
        self.failed = None

    @classmethod
    def succeed(cls, func_name, inputs, is_valid):
        result = PropResult()
        result.succeeded = (func_name, inputs, is_valid)
        return result

    @classmethod
    def fail(cls, func_name, inputs, error):
        result = PropResult()
        result.failed = (func_name, inputs, error)
        return result


class Prop:

    def __init__(self, arb, func, label, *exception, **kwargs):
        self.arbitrary_generators = arb.generate_arbitraries()
        self.func = func
        self.label = label
        self.exception = exception
        self.type_of_return_value = kwargs.get('type')

    def execute(self):
        label, func, exception = self.label, self.func, self.exception
        inputs = []

        try:
            inputs = [f() for f in self.arbitrary_generators]

            result = func(*inputs)

            if self.type_of_return_value:
                is_valid = isinstance(result, self.type_of_return_value)
            else:
                is_valid = result

            return PropResult.succeed(func.__name__, inputs, is_valid)

        except exception as error:
            return PropResult.fail(func.__name__, inputs, error)


def for_all(arbitraries, label, func):
    arb = Arbitrary(*arbitraries)
    if type(func) == PossibleFuncToThrow:
        return Prop(arb, func.to_function, label, *(func.exceptions))
    else:
        return Prop(arb, func, label)


class PossibleFuncToThrow:
    def __init__(self, func, should_all_throw, *exception):
        self.to_function = func
        self.should_all_throw = should_all_throw
        self.exceptions = exception


def may_throw(func, *exception):
    return PossibleFuncToThrow(func, False, *exception)


class RunningResult:
    def __init__(self, label, func_name, func_code, success, failure, exceptions, results):
        self.label = label
        self.func_name = func_name
        self.func_code = func_code
        self.success = success
        self.failure = failure
        self.exceptions = exceptions
        self.prop_results = results


class PropRunner:

    TEST_COUNT = 15

    def __init__(self, count=15):
        self.count = count if count >= 1 else PropRunner.TEST_COUNT
        self.test_result = []

    def run(self, prop, queue=None):
        success, failure = 0, 0
        exceptions = {}
        results = []

        try:
            for i in range(self.count):
                prop_result = prop.execute()

                if prop_result.succeeded:
                    _, _, is_valid = prop_result.succeeded
                    success = success + 1 if is_valid else success
                    failure = failure + 1 if not is_valid else failure

                    results.append(prop_result)
                else:
                    _, _, error = prop_result.failed
                    exception_key = re.match('^([a-zA-Z]+)\(.*$', repr(error)).group(1)
                    exceptions.setdefault(exception_key, 0)
                    exceptions[exception_key] += 1

                    results.append(prop_result)

            test_result = RunningResult(
                prop.label,
                prop.func.__name__,
                marshal.dumps(prop.func.__code__),
                success,
                failure,
                exceptions,
                results
            )

            if queue is not None:
                queue.put(test_result)

            self.test_result = test_result
            return self

        except TypeError as error:
            print('TypeError! please check into function variables.')
            print(error.args[0])
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=10, file=sys.stdout)
            sys.exit(0)

        except ImportError as error:
            print('ImportError! ' +
                  'please check import module name or module file-path.')
            print(error.args[0])
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=10, file=sys.stdout)
            sys.exit(0)

        except Exception as error:
            print('!!! Exclude Error !!!')
            print(error.args[0])
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=10, file=sys.stdout)
