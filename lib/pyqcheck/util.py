# -*- coding:utf-8 -*-


class PropResultSymbol:
    def __init__(self, with_emoji):
        self.with_emoji = with_emoji

    def success(self):
        return u'\u2600' if self.with_emoji else 'success'

    def failure(self):
        return u'\u2601' if self.with_emoji else 'failure'

    def error(self):
        return u'\u2603' if self.with_emoji else 'error  '


class PrettyPrinter:
    def __init__(self, with_emoji):
        self.result_symbol = self.__check_emoji_ablity(with_emoji)

    @staticmethod
    def __check_emoji_ablity(with_emoji):
        if not with_emoji:
            return PropResultSymbol(False)
        else:
            import sys
            try:
                if sys.stdout.encoding is not None:
                    '\u2602'.encode(sys.stdout.encoding)
                else:
                    '\u2602'.encode('utf-8')
                return PropResultSymbol(True)
            except UnicodeEncodeError:
                return PropResultSymbol(False)

    def print_results(self, results):
        print('----- PyQCheck test results... -----')
        for result in results:
            print('label: ' + str(result.label).strip())
            print('success: ' + str(result.success))
            print('failure: ' + str(result.failure))
            if len(result.exceptions) != 0:
                print('exceptions: ')
                for key in result.exceptions:
                    print('  ' + key + ': ' + str(result.exceptions[key]))
            if len(result.prop_results) != 0:
                print('verbose: ')
                verboses = self.to_verbose_string(result.prop_results)
                for verbose in verboses:
                    print('  ' + verbose)
            print('-----')

    def to_verbose_string(self, prop_results):
        for result in prop_results:
            if result.succeeded:
                func_name, inputs, is_valid = result.succeeded

                icon = self.result_symbol.success() if is_valid else self.result_symbol.failure()
                verbose_variable = PrettyPrinter.get_verbose(inputs)

                yield icon + '  ' + func_name + verbose_variable
            else:
                func_name, inputs, _ = result.failed
                verbose_variable = PrettyPrinter.get_verbose(inputs)
                yield self.result_symbol.error() + '  ' + func_name + verbose_variable

    @staticmethod
    def get_verbose(inputs):
        if len(inputs) == 1:
            try:
                verbose_variable = '(' + str(inputs[0]) + ')'
            except UnicodeEncodeError:
                verbose_variable = '(' + inputs[0] + ')'
        else:
            try:
                verbose_variable = str(tuple(inputs))
            except UnicodeEncodeError:
                verbose_variable = str(tuple(inputs))
        return verbose_variable