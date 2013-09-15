# -*- coding: utf-8 -*-
import rectable
from rectable import emit


def side(s, n):
    lines = s.split('\n')
    width = max(len(l) for l in lines)
    return (
        [l + ' ' * (width - len(l)) for l in lines] +
        [' ' * width] * (n - len(lines))
    )

def assertEqual(x, y):
    if x != y:
        lines = max(x.count('\n'), y.count('\n'))
        sides = '\n'.join(
            left + ' | ' + right
            for left, right in zip(side(x, lines), side(y, lines)))
        print sides
    assert x == y


class TestEmit(object):
    def test_simple(self):
        r = emit.render((None, []))
        assertEqual(
            r,
            (
                '<table>\n'
                '</table>\n'
            )
        )

    def test_single(self):
        r = emit.render((None, [('style', 0, 'x')]))
        assertEqual(
            r,
            (
                '<table>\n'
                '  <tr class="style">\n'
                '    <th>\n'
                '      0\n'
                '    </th>\n'
                '    <td>\n'
                '      x\n'
                '    </td>\n'
                '  </tr>\n'
                '</table>\n'
            )
        )

    def test_front(self):
        s = rectable.present({'k': 2})
        assertEqual(
            s,
            (
                '<table>\n'
                '  <tr class="key">\n'
                '    <th>\n'
                '      k\n'
                '    </th>\n'
                '    <td>\n'
                '      2\n'
                '    </td>\n'
                '  </tr>\n'
                '</table>\n'
            )
        )
