#!/bin/bash
rm *.o *.so *.tar.gz *.spec *.rockspec
LUA_SUBPROCESS_VERSION="$(git describe --tags | sed -r 's/([^-]*-[^-]*).*/\1/')" python3 generate_spec.py
rm *.obsinfo
git add --all
git commit -m update
git push

