#!/usr/bin/python
# -*- coding: utf8 -*-
# -*- coding: ascii -*-
__author__ = 'ting'
#ASCII<->UNICODE;ord,chr,unichar,repr()是将一个对象转成字符串显示
print ord('a')
print chr(97)
print ord(u'\u2020')
print unichr(8224)
print repr(unichr(8224))
print chr(97),str(97)
print map(ord,'ciao')
print ''.join(map(chr,range(97,100)))


