# -*- coding:utf-8 -*-
__all__ = [
  'pyqcheck', 
  'arbitrary', 
  'pyqworker', 
  'arbitraries'
]

__name__ = "PyQCheck"
__version__ = "0.3.4"
__description__ = "PyQCheck is Quick Check-like random testing framework."
__author__ = "Keiji Matsuzaki"
__author_email__ = "futoase@gmail.com"
__license__ = "MIT License"
__url__ = "https://github.com/futoase/PyQCheck" 

# See http://pypi.python.org/pypi?%3Aaction=list_classifiers.
__classifiers__ = [
  "Programming Language :: Python :: 3.3",
  "Topic :: Software Development"
]

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))

if not SCRIPT_DIR in sys.path:
  sys.path.insert(0, os.path.normpath(SCRIPT_DIR))

from multiprocessing import Process

from prop import Prop, PropRunner
from arbitrary import Arbitrary, ArbitraryAbstraction
from pyqworker import PyQWorker
from util import PrettyPrinter


# for backward compatibility
def __obsolete_property(target, label, func, *exception, **kwargs):
    return Prop(target, func, label, *exception, **kwargs)

def __obsolete_run(target, count=15, queue=None):
    # lose compatibility: remove 'verbose' argument
    runner = PropRunner(count)
    return runner.run(target, queue)

def __obsolete_result(target, verbose=True):
    # lose compatibility: add 'verbose' argument
    printer = PrettyPrinter(verbose, True)
    printer.print_results([target.test_result])

Arbitrary.property = __obsolete_property
Prop.run = __obsolete_run
PropRunner.result = __obsolete_result


class set_arbitrary(object):
  def __init__(self, *arbitraries, **kwargs):
    self.arbitraries = arbitraries
    self.exceptions = kwargs.get('exceptions', ())
    self.arguments = kwargs.get('arguments', {})

  def __call__(self, func):
    label = func.__doc__ if func.__doc__ is not None else 'no label'
    PyQCheck(verbose=False).add(
      Prop(
        Arbitrary(*self.arbitraries), func, label.strip(), *self.exceptions, **self.arguments))

class PyQCheck(object):
  TEST_STEP = []

  def __init__(self, verbose=False, process=1):
    self.results = []
    self.verbose = verbose
    self.process = process

  def clear(self):
    PyQCheck.TEST_STEP = []

  def add(self, test):
    PyQCheck.TEST_STEP.append(test)
    return self

  def run(self, count=Arbitrary.TEST_COUNT):
    print('start test.')

    if self.process > 1:
      from multiprocessing import Queue
    else:
      from queue import Queue

    runner = PropRunner(count)
    queue = Queue(maxsize=len(PyQCheck.TEST_STEP))
    if self.process > 1:
      # multi process
      PyQWorker().set([
        Process(
          target=runner.run, args=(test,), kwargs={"queue": queue})         for test in PyQCheck.TEST_STEP
      ]).start(self.process)
    else:
      # linear
      for test in PyQCheck.TEST_STEP:
        runner.run(test, queue=queue)

    length = len(PyQCheck.TEST_STEP)
    while True:
      if queue.full():
        print('finish.')
        for i in range(length):
          self.results.append(queue.get())
        return self

  def result(self, with_emoji=True):
    printer = PrettyPrinter(self.verbose, with_emoji)
    printer.print_results(self.results)
