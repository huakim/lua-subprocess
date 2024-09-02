
package = 'subprocess'
version = '0.5.6-14'
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
  platforms = {
   unix = {
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
   },
   windows = {
    modules = {
     subprocess = {
      defines = {
       "OS_WINDOWS",
       "LUA_BUILD_AS_DLL",
       "_CRT_SECURE_NO_WARNINGS",
      },
      sources = {
       "subprocess.c",
       "liolib-copy.c",
      },
     },
    },
    type = "builtin",
   },
  },
 }
dependencies = {
  "lua >= 5.1",
 }
