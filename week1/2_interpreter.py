# -*- coding: utf-8 -*-

import sys
import site

the_world_is_flat = True
if the_world_is_flat:
    print("如果世界是平的，小心不要掉下去了!")

print('套件位置')
print(site.getusersitepackages())

print('中文編碼')
print(sys.getdefaultencoding())
