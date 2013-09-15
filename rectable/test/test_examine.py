# -*- coding: utf-8 -*-
from rectable import examine


def assertEqual(x, y):
    if x != y:
        msg = "%r = %r" % (x, y)
    assert x == y, msg


class TestExamine(object):
    def test_simple(self):
        r = examine.stream('x')
        assertEqual(r, 'x')

    def test_convert(self):
        r = examine.stream(123)
        assertEqual(r, '123')

    def test_str_list(self):
        t, r = examine.stream(['x', 'y', 'z'])
        assertEqual(
            (t, list(r)),
            (
                None,
                [
                    ('index', 0, 'x'),
                    ('index', 1, 'y'),
                    ('index', 2, 'z'),
                ]
            )
        )

    def test_str_dict(self):
        t, r = examine.stream({'k1': 'x', 'k2': 'y', 'k3': 'z',})
        assertEqual(
            (t, list(r)),
            (
                None,
                [
                    ('key', 'k1', 'x'),
                    ('key', 'k2', 'y'),
                    ('key', 'k3', 'z'),
                ]
            )
        )

    def test_nest(self):
        t, r = examine.stream({
            'k1': 'x',
            'k2': [0, 'one', 1],
            'k3': 'z',
        })
