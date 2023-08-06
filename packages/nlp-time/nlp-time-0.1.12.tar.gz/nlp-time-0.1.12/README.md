📦 nlp-time
=======================

Time NLP module

Installation
-----

```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://pypi.org/simple/ nlp-time
```

Example
-----

```python
import nlp_time
from datetime import datetime
# Partial replacement according to regular expression
res = nlp_time.get_time("我是周六早上6点的飞机")
# output: ('周六早上6点', ('2022-05-28 06:00:00', '2022-05-28 06:59:59'))
res = nlp_time.get_time("我是周六早上6点的飞机", tend_future=False)
# output: ('周六早上6点', ('2022-05-21 06:00:00', '2022-05-21 06:59:59'))
res = nlp_time.get_text(datetime.strptime("2022-05-22 20:06:00", "%Y-%m-%d %H:%M:%S"))
# output: 昨天晚上20点06分
res = nlp_time.get_text("2022-05-22 20:06:00")
# output: 昨天晚上20点06分
res = nlp_time.get_text("2021-05-22 20:06:00")
# output: 去年5月22号晚上20点06分
res = nlp_time.get_text(1653091200)
# output: 前天早上8点
res = nlp_time.get_text("2021-05-18 20:06:00")
# output: 上周三晚上20点06分
```

To Do
-----

-   Be the best version of you.


More Resources
--------------

-   [nlp-time] on github.com
-   [Official Python Packaging User Guide](https://packaging.python.org)
-   [The Hitchhiker's Guide to Packaging]
-   [Cookiecutter template for a Python package]

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

  [nlp-time]: https://github.com/holbos-deng/nlp_time
  [PyPi]: https://docs.python.org/3/distutils/packageindex.html
  [Twine]: https://pypi.python.org/pypi/twine
  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
  [The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage
