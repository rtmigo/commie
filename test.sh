#!/bin/bash
set -e

thisFileParentDir="$(dirname "$(perl -MCwd -e 'print Cwd::abs_path shift' "$0")")"
cd "$thisFileParentDir"

nosetests --all-modules

# also could be run like that:
# python3 setup.py test
# but it does npt work well with GitHub Actions on Python 3.7