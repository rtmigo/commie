[![Actions Status](https://github.com/rtmigo/commie.python/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)
[![PyPI status](https://img.shields.io/pypi/status/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI license](https://img.shields.io/pypi/l/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/commie.svg)](https://pypi.python.org/pypi/commie/)

A fork from [comment_parser](https://github.com/jeanralphaviles/comment_parser). 
Differences from the original:
- **comment_parser** returned only a line number, **commie** returns exact positions where the comment
starts and ends (just like regular string search)
- **comment_parser** returned only the text of a comment, but **commie** respects markup as well, 
making it possible to remove or replace the comment   
- **comment_parser** depends on [python-magic](https://pypi.org/project/python-magic) requiring 
an optional installation of binaries. `commie` removes this dependency 
