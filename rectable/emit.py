# -*- coding: utf-8 -*-
from rectable.util import string, safe


class Emitter(object):
    def __init__(self, options=None):
        self.options = options if options else {}

    def line(self, text='', indent=0):
        return (
            self.options.get('indent', '') * indent +
            text +
            self.options.get('linesep', '')
        )

    def tag(self, name, indent=0, css=None):
        return self.line(
            '<' + name + (' class="%s"' % css if css else '') + '>', indent)

    def wrap(self, name, inner, indent=0, css=None):
        return (
            self.tag(name, indent, css) +
            inner +
            self.tag('/' + name, indent)
        )

    def row(self, keytype, key, val, indent=0):
        return self.wrap(
            'tr',
            self.wrap('th', self.line(safe(key), indent + 2), indent + 1) +
            self.wrap('td', self.render(val, indent + 2), indent + 1),
            indent, keytype)

    def table(self, source, indent=0, css=None):
        sep = self.options.get('linesep', '')
        return (
            self.tag('table', indent, css) +
            sep.join(self.row(keytype, key, val, indent + 1)
                     for keytype, key, val in source) +
            self.tag('/table', indent)
        )

    def render(self, thing, indent=0, css=None):
        if isinstance(thing, string):
            return self.line(safe(thing), indent)
        else:
            css, thing = thing
            return self.table(thing, indent, css)


def render(thing, options=None):
    options.setdefault('linesep', '\n')
    options.setdefault('indent', '  ')
    return Emitter(options).render(thing, 0, 'rectable')
