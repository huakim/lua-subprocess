#!/usr/bin/python3
from lua2pack import main
import os
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
rockspec = 'text://'+rockspec
for template in ('rock.rockspec', 'generic.spec', 'obs.obsinfo'): main(['generate', '--rockspec',rockspec,'--template',template])
