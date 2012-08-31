#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from _import import Arbitrary

def run():
  Arbitrary('string').property(
    'x =~ /^[a-zA-Z0-9]+$/g', 
    lambda x : re.match(ur'^[a-zA-Z0-9]+$', x) is not None
  ).run(100, verbose=False).result()

if __name__ == '__main__':
  run()
