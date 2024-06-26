#!/bin/bash
rm *.o *.so *.tar.gz *.obsinfo *.spec *.rockspec
python3 generate_spec.py
git add --all
git commit -m update
git push
