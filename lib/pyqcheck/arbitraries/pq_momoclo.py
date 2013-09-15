# -*- coding:utf-8 -*-

import random
import datetime

class PyQMomoclo(object):
  '''
  This Momoclo class is returned momoclo member.
  '''

  def __init__(self):
    pass

  def generate(self, current=True):
    '''
    generate of momoclo members.
    '''
    def func():
      while True:
        choice = random.choice([
          {
           "name": "Kanako Momota",
           "color": "Red",
           "birthday": datetime.datetime(1994, 7, 12),
           "current": True
          },
          {"name": "Shiori Tamai",
           "color": "Yellow",
           "birthday": datetime.datetime(1995, 6, 4),
           "current" : True
          },
          {"name": "Ayaka Sasaki",
           "color": "Pink",
           "birthday": datetime.datetime(1996, 6, 11),
           "current": True
          },
          {"name": "Momoka Ariyasu",
           "color": "Green",
           "birthday": datetime.datetime(1995, 3, 15),
           "current": True
          },
          {"name": "Reni Takagi",
           "color": "Purple",
           "birthday": datetime.datetime(1993, 6, 21),
           "current": True
          },
          {"name": "Tsukina Takai",
           "color": None,
           "birthday": datetime.datetime(1995, 7, 6),
           "current": False
          },
          {"name": "Miyuu Wagawa",
           "color": None,
           "birthday": datetime.datetime(1993, 12, 19),
           "current": False
          },
          {"name": "Manami Ikura",
           "color": None,
           "birthday": datetime.datetime(1994, 2, 4),
           "current": False
          },
          {"name": "Sumire Fujishiro",
           "color": None,
           "birthday": datetime.datetime(1994, 5, 8),
           "current": False
          },
          {"name": "Yukina Kashiwa",
           "color": None,
           "birthday": datetime.datetime(1994, 8, 12),
           "current": False
          },
          {"name": "Akari Hayami",
           "color": "Blue",
           "birthday": datetime.datetime(1995, 3, 17),
           "current": False
          }
        ])
  
        if (current and choice.get('current')) or not current:
          return choice

    return func
