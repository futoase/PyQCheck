# -*- coding:utf-8 -*-

class PyQWorker(object):
  def __init__(self):
    self.jobs , self.working, self.finished = [], [], []
    self.processed = 0

  def set(self, worker):
    self.worker = worker
    return self

  def start(self, process=4):
    self.process = process
    for job in self.worker:
      self.jobs.append(job)

    while True:
      if set(self.jobs) == set(self.working):
        break

      if self.processed < process:
        for job in self.jobs:
          if self.processed >= process:
            break

          if job.is_alive() == False and not job in self.working:
            job.start()
            self.working.append(job)
            self.__inc_process()

      self.__finished()

  def __is_process_max(self):
    return self.processed > self.process

  def __inc_process(self):
    self.processed += 1

  def __dec_process(self):
    self.processed -= 1

  def __finished(self):
    while True:
      for job in self.working:
        if job.is_alive() == False and not job in self.finished:
          self.finished.append(job)
          self.__dec_process()
      if not self.__is_process_max():
         break
