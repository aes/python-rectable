# -*- coding: utf-8 -*-
try:
    import anyjson as json
except:
    import json

try:  # 2/3 compatibility
    string = basestring
except:
    string = str


def safe_char(c):
    return 32 <= ord(c) < 127 and c not in '<>&'


def safe(s):
    return ''.join(c if safe_char(c) else ("&%d;" % ord(c)) for c in str(s))
