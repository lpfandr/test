# -*- coding:utf-8 _*-
"""
@author:lpf_a
@file: 电话组合排列.py
@time: 2022/6/28  19:26
"""

def phoneLetter(digits):
    if not digits:
        return []
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(keyboard[digits])
    else:
        result = phoneLetter(digits[1:])
        for i in result:
            for j in keyboard[digits[0]]:
                res.append((j + i))
        return res


print(phoneLetter("234"))
