# -*- coding:utf-8 _*-
"""
@author:lpf_a
@file: test.py
@time: 2022/6/28  21:12
"""

from datetime import datetime
from threading import Timer

import psutil as psutil
import sys
import gc
import objgraph

"""
内存泄漏：
    在使用完毕后未释放，结果导致一直占据该内存单元。直到程序结束。从生命周期角度考虑就是超出了引用此内存的类的生命周期。
    长时间内存泄漏很可能造成内存溢出。对于一个长期运行的后台服务进程来说，如果内存持续增长，那么很可能是内存泄露。
    python自带垃圾回收机制，在此基础上，内存泄漏从底层C程序、外部库、循环引用等角度进行处理。
"""

gc.collect()
objgraph.show_growth()


class A:
    def __init__(self):
        self.a = None


def func():
    a1 = A()
    a2 = A()
    a3 = A()
    print('a1/a2引用计数为2')
    print('a1:', sys.getrefcount(a1))
    a1.a = a2
    a2.a = a1
    print('a1:', sys.getrefcount(a1))
    a3.a = a1
    print('a1:', sys.getrefcount(a1))
    del a3  # 删除a3同时减少a1的引用计数
    print('a1:', sys.getrefcount(a1))

    print(id(a2.a))
    return


def MonitorSystem(logfile=None):
    # cpu监测
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    memper = mem.percent
    now = datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = '{0} cpu:{1}%, mem:{2}%'.format(ts, cpuper, memper)
    print(line)
    print('当前内存', mem)
    # 启动定时器任务，每三秒执行一次
    Timer(3, MonitorSystem).start()


if __name__ == '__main__':
    # 这个执行之后，a3引用计数满足内存释放条件
    # a1,a2 引用计数不满足内存释放条件
    func()
    # 执行到此，a3被回收（或者可回收状态），而a1,a2用由于相互引用，在函数func执行完之后
    # 而不能够被回收，变成不可管理的垃圾内存
    # 在func退出之前对a1.a、a2.a赋予一个None值即可，解除循环引用导致垃圾内存不能够回收。
    MonitorSystem()
