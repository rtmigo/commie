#!/bin/bash
set -e && source "scripts/pyrel.sh"

pyrel_test_begin # check it builds
python3 -c "import commie"
pyrel_test_end # cleanup