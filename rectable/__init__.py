# -*- coding: utf-8 -*-
from rectable import emit
from rectable import examine

Emitter = emit.Emitter
render = emit.render

Examiner = examine.Examiner
stream = examine.stream


def present(thing, **kw):
    source = stream(thing, kw)
    result = render(source, kw)
    return result
