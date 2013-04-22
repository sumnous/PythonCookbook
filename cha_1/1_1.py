#!/usr/bin/python
# -*- coding: utf8 -*-
# -*- coding: ascii -*-
__author__ = 'ting'

#每次处理一个字符
#list,map
#获得该字符串的所有字符的集合，调用sets.Set

import sets
magic_chars = sets.Set('abracadabra')
poppins_chars = sets.Set('supercalifragilisticexpialidocious')
print ''.join(magic_chars & poppins_chars) #集合的交集
