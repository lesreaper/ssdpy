# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    import mock
else:
    from unittest import mock  # noqa
