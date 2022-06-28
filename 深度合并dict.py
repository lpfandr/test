# -*- coding:utf-8 _*-
"""
@author:lpf_a
@file: 深度合并dict.py
@time: 2022/6/28  19:26
"""


def merge_dict(dict1, dict2):
    try:
        for key in dict2.keys():
            print(key)
            # print(dict1.keys())
            # 如果dict1不存在dict2的key，在1中新增key，值为2的值
            if key not in dict1.keys():
                dict1[key] = dict2[key]
            # 如果dict1中存在dict2的key,确定值的类型都是dict时,继续合并，否则更新，值为2的值
            # print('dict1有dict2的key')
            # print(type(dict2[key]))
            elif type(dict1[key]) is dict and type(dict2[key]) is dict:
                merge_dict(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]
    except Exception as e:
        print(e)
        if "object has no attribute 'keys'" in str(e):
            print('您输入的参数不是dict类型')


if __name__ == '__main__':

    source_dict = {
        'key0': 'a',
        'key1': 'b',
        'key2': {
            'inner_key0': 'c',
            'inner_key1': 'd'
        }
    }
    update_dict = {
        'key1': 'x',
        'key2': {
            'inner_key0': 'y'
        }
    }

    dict3 = {
        'key0': 'a1',
        'key3': {2: {}}
    }

    aa = []

    n = 0
    for dictT in [aa, update_dict, dict3]:
        n = n + 1
        print('第{}次'.format(n))
        merge_dict(source_dict, dictT)

    print('合并次数', n)
    print('最终dict')
    print(source_dict)
