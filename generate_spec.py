#!/usr/bin/python3
from lua2pack import generator
import os

args = type('AttrDict', (dict,), {'__slots__':(),'__getattr__':dict.get,'__setattr__':dict.__setitem__})()

def main(template):
    args.template = template
    generator(args)

rockspec = r'''
package = "subprocess"
version = "'''+os.environ.get('LUA_SUBPROCESS_VERSION','0.5.5-1')+'''"
source = {
  url = "git://github.com/huakim/lua-subprocess.git"
}
description = {
  summary = "Subprocess module for Lua",
  detailed = [[
  ]],
  homepage = "https://github.com/huakim/lua-subprocess",
  license = "LGPL"
}
dependencies = {
  "lua >= 5.1"
}
build = {

   platforms = {
      unix = {
         type = "builtin",
         modules = {
            subprocess = {
               sources = { "subprocess.c", "liolib-copy.c" },
               defines = { "OS_POSIX" }
            }
         }
      },
      windows = {
         type = "builtin",
         modules = {
            subprocess = {
               sources = { "subprocess.c", "liolib-copy.c" },
               defines = { "OS_WINDOWS", "LUA_BUILD_AS_DLL", "_CRT_SECURE_NO_WARNINGS" }
            }
         }
      }
   }

}
'''

args.rockspec = ['text://'+rockspec]

main('rock.rockspec')
main('generic.spec')
main('obs.obsinfo')
