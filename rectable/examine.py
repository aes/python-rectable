# -*- coding: utf-8 -*-
from rectable import util


class Examiner(object):
    default_parsers = (
        ('json', util.json.loads),
    )

    def __init__(self, options=None):
        self.options = o = options if options else {}
        o.setdefault('parsers', self.default_parsers)

    def parse(self, thing):
        for name, parser in self.options['parsers']:
            try:
                return name, parser(thing)
            except:
                pass

        return '', thing

    def examine(self, thing, flavour=None):
        if isinstance(thing, util.string):
            flavour, thing = self.parse(thing)

        if isinstance(thing, util.string):
            return thing

        elif callable(getattr(thing, 'keys', None)):
            return (
                flavour,
                (('key', k, self.examine(thing[k]))
                 for k in sorted(thing.keys())))
        elif hasattr(thing, '__iter__'):
            return (
                flavour,
                (('index', i, self.examine(v))
                 for i, v in enumerate(thing)))
        else:
            return self.examine(str(thing))


def stream(thing, options=None):
    e = Examiner(options)
    return e.examine(thing)
