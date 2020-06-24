__author__ = 'lee'
#coding=utf-8
import os
import sys
print(__file__)
path=__file__
print(os.path.realpath(__file__))
print(os.path.split(__file__)[0])
print(r'{}/gaokaodaojishi.zip'.format(path))