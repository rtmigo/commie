[![Actions Status](https://github.com/rtmigo/commie.python/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)


A fork from [comment_parser](https://github.com/jeanralphaviles/comment_parser). 
Differences from the original:
- `comment_parser` returned only a line number, `commie` returns exact positions where the comment
starts and ends (just like regular string search)
- `comment_parser` returned only the text of a comment, but `commie` respects markup as well, 
making it possible to remove or replace the comment   
- `comment_parser` depends on [python-magic](https://pypi.org/project/python-magic) requiring 
optional installation of binaries. `commie` removes this dependency 
