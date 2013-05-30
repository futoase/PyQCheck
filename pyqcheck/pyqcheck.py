# -*- coding:utf-8 -*-

from multiprocessing import Process

from .arbitrary import Arbitrary, ArbitraryList
from .pyqworker import PyQWorker
from .util import print_results

class set_arbitrary(object):
  def __init__(self, *arbitraries, **kwargs):
    self.arbitraries = arbitraries
    self.exceptions = kwargs.get('exceptions', ())
    self.arguments = kwargs.get('arguments', {})

  def __call__(self, func):
    label = func.__doc__ if func.__doc__ is not None else 'no label'
    PyQCheck(verbose=False).add(
      Arbitrary(*self.arbitraries).property(
        label.strip(), func, *self.exceptions, **self.arguments))

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

    queue = Queue(maxsize=len(PyQCheck.TEST_STEP))
    if self.process > 1:
      # multi process
      PyQWorker().set([
        Process(
          target=test.run, args=(count, self.verbose), kwargs={"queue": queue})         for test in PyQCheck.TEST_STEP
      ]).start(self.process)
    else:
      # linear
      for test in PyQCheck.TEST_STEP:
        test.run(count, self.verbose, queue=queue)

    length = len(PyQCheck.TEST_STEP)
    while True:
      if queue.full():
        print('finish.')
        for i in range(length):
          self.results.append(ArbitraryList(*queue.get()))
        return self

  def result(self):
    print_results(self.results)
