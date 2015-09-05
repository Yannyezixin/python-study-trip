#coding: utf-8
import re

s = 'words,  names,  yes, sex, book.'
gbk = '中文, name, 名字.'

print re.split('\W+', s)
print re.split('\W+', gbk)
print re.split('\W+', s, 2)
print re.split('\W+', s, 3)
print re.split('(\W+)', s)
print re.split('(\W+)', gbk)

