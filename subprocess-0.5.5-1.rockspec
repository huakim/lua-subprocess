
package = 'subprocess'
version = '0.5.5-1'
source = {
  url = "git://github.com/huakim/lua-subprocess.git",
 }
description = {
  detailed = "  ",
  homepage = "https://github.com/huakim/lua-subprocess",
  license = "LGPL",
  summary = "Subprocess module for Lua",
 }
build = {
  modules = {
   subprocess = {
    defines = {
     "OS_POSIX",
    },
    sources = {
     "subprocess.c",
     "liolib-copy.c",
    },
   },
  },
  type = "builtin",
 }
dependencies = {
  "lua >= 5.1",
 }