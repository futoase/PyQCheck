# -*- coding:utf-8 -*-

import logging

def print_results(results):
  # pretty print of results
  # [[label, func.func_name, marshal.dumps(func.func_code), success, failure, exceptions, verbose], ...]
  print('----- PyQCheck test results... -----')
  for result in results:
    #func = types.FunctionType(marshal.loads(result[2]), globals(), result[1])
    print('label: ' + str(result.label).strip())
    print('success: ' + str(result.success))
    print('failure: ' + str(result.failure))
    if len(result.exceptions) != 0:
      print('exceptions: ')
      for key in result.exceptions:
        print('  ' + key + ': ' + str(result.exceptions[key]))
    if len(result.verbose) != 0:
      print('verbose: ')
      for verbose in result.verbose:
        print('  ' + verbose)
    print('-----')
