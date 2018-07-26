
# -*- coding: utf-8 -*-

# Copyright (c) 2018-2018 the ValueX authors
# All rights reserved.
#
# The project sponsor and lead author is Xu Rendong.
# E-mail: xrd@ustc.edu, QQ: 277195007, WeChat: ustc_xrd
# See the contributors file for names of other contributors.
#
# Commercial use of this code in source and binary forms is
# governed by a LGPL v3 license. You may get a copy from the
# root directory. Or else you should get a specific written 
# permission from the project author.
#
# Individual and educational use of this code in source and
# binary forms is governed by a 3-clause BSD license. You may
# get a copy from the root directory. Certainly welcome you
# to contribute code of all sorts.
#
# Be sure to retain the above copyright notice and conditions.

import datetime
import threading

class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kv):
        if cls in cls.objs:
            return cls.objs[cls]['obj']
        
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:  # double check locking
                return cls.objs[cls]['obj']
            obj = object.__new__(cls)
            cls.objs[cls] = {'obj': obj, 'init': False}
            setattr(cls, '__init__', cls.decorate_init(cls.__init__))
        finally:
            cls.objs_locker.release()
        
        return cls.objs[cls]['obj']

    @classmethod
    def decorate_init(cls, fn):
        def init_wrap(*args):
        #def init_wrap(*args, **kv): # 子类可以使用 __init__(self, **kwargs) 形式传参
            if not cls.objs[cls]['init']:
                fn(*args)
                #fn(*args, **kv) # 子类可以使用 __init__(self, **kwargs) 形式传参
                cls.objs[cls]['init'] = True
            return
        
        return init_wrap

def GetDateShort():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def GetTimeShort():
    return datetime.datetime.now().strftime("%H:%M:%S")

def TransDateIntToStr(int_date):
    year = int(int_date / 10000)
    month = int((int_date % 10000) / 100)
    day = int_date % 100
    return "%d-%d-%d" % (year, month, day)

def TransDateIntToDate(int_date):
    year = int(int_date / 10000)
    month = int((int_date % 10000) / 100)
    day = int(int_date % 100)
    return datetime.date(year, month, day)

def TransTimeIntToStr(int_time):
    hour = int(int_time / 10000)
    minute = int((int_time % 10000) / 100)
    second = int_time % 100
    return "%d:%d:%d" % (hour, minute, second)
