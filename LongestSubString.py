"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""


def longest_substing(s):
    a, b = '', 0
    for i in range(len(s)):
        if i == 0:
            a += s[i]
            continue
        if s[i] not in a:
            a += s[i]
        else:
            if len(a) > b:
                b = len(a)
            a = s[i]
    return b



