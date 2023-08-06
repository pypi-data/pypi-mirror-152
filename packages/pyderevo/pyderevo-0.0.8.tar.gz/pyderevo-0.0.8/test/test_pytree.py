import unittest

from collections import namedtuple

from pytree import (
    broadcast_to_and_flatten,
    register_custom,
    tree_flatten,
    tree_map,
    tree_unflatten,
    TreeSpec,
)


def _spec(o):
    _, spec = tree_flatten(o)
    return spec


def _spec_str(type_char, n):
    spec = type_char + str(n)
    for i in range(n):
        spec += "#1"
    spec += "("
    for i in range(n):
        if i > 0:
            spec += ","
        spec += "$"
    spec += ")"
    return spec


def _spec_str_dict(d):
    n = len(d)
    spec = "D" + str(n)
    for i in range(n):
        spec += "#1"
    spec += "("
    i = 0
    for key in d.keys():
        if i > 0:
            spec += ","
        if isinstance(key, str):
            spec += "'" + key + "'"
        else:
            spec += str(key)
        spec += ":$"
        i += 1
    spec += ")"
    return spec


class O:
    def __init__(self, *args):
        self.args = args


class TestPytree(unittest.TestCase):
    def test_treespec_equality(self):
        self.assertTrue(TreeSpec.from_str("$") == TreeSpec.from_str("$"))
        self.assertTrue(_spec([1]) == TreeSpec.from_str("L1#1($)"))
        self.assertTrue(_spec((1)) != _spec([1]))
        self.assertTrue(_spec((1)) == _spec((2)))

    def test_flatten_unflatten_leaf(self):
        def run_test_with_leaf(leaf):
            values, treespec = tree_flatten(leaf)
            self.assertEqual(values, [leaf])
            self.assertEqual(treespec, TreeSpec.from_str("$"))

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, leaf)

        run_test_with_leaf(1)
        run_test_with_leaf(1.0)
        run_test_with_leaf(None)
        run_test_with_leaf(bool)
        run_test_with_leaf(3)

    def test_flatten_unflatten_list(self):
        def run_test(lst):
            spec = _spec_str("L", len(lst))

            expected_spec = TreeSpec.from_str(spec)
            values, treespec = tree_flatten(lst)
            self.assertTrue(isinstance(values, list))
            self.assertEqual(values, lst)
            self.assertEqual(treespec, expected_spec)

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, lst)
            self.assertTrue(isinstance(unflattened, list))

        run_test([])
        run_test([1.0, 2])
        run_test([O(1, 2), 2, 10, 9, 11])

    def test_flatten_unflatten_tuple(self):
        def run_test(tup):
            spec = _spec_str("T", len(tup))

            expected_spec = TreeSpec.from_str(spec)
            values, treespec = tree_flatten(tup)
            self.assertTrue(isinstance(values, list))
            self.assertEqual(values, list(tup))
            self.assertEqual(treespec, expected_spec)

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, tup)
            self.assertTrue(isinstance(unflattened, tuple))

        run_test(())
        run_test((1.0,))
        run_test((1.0, 2))
        run_test((O(1, 2), 2, 10, 9, 11))

    def test_flatten_unflatten_namedtuple(self):
        Point = namedtuple("Point", ["x", "y"])

        def run_test(tup):
            spec = _spec_str("N", len(tup))
            expected_spec = TreeSpec.from_str(spec)

            values, treespec = tree_flatten(tup)
            self.assertTrue(isinstance(values, list))

            self.assertEqual(values, list(tup))
            self.assertEqual(treespec, expected_spec)

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, tup)

        run_test(Point(1.0, 2))
        run_test(Point("1.", 2))

    def test_flatten_unflatten_torch_namedtuple_return_type(self):
        x = O(2, 3)
        expected = O(0)

        values, spec = tree_flatten(expected)
        result = tree_unflatten(values, spec)

        self.assertEqual(type(result), type(expected))
        self.assertEqual(result, expected)

    def test_flatten_unflatten_dict(self):
        def run_test(d):
            spec = _spec_str_dict(d)

            values, treespec = tree_flatten(d)
            self.assertTrue(isinstance(values, list))
            self.assertEqual(values, list(d.values()))
            self.assertEqual(treespec, TreeSpec.from_str(spec))

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, d)
            self.assertTrue(isinstance(unflattened, dict))

        run_test({})
        run_test({"a": 1})
        run_test({"abcdefg": O(2, 3)})
        run_test({1: O(1, 2)})
        run_test({"a": 1, "b": 2, "c": O(1, 2)})

    def test_flatten_unflatten_nested(self):
        def run_test(pytree):
            values, treespec = tree_flatten(pytree)
            self.assertTrue(isinstance(values, list))
            self.assertEqual(len(values), treespec.num_leaves)

            unflattened = tree_unflatten(values, treespec)
            self.assertEqual(unflattened, pytree)

        cases = [
            [()],
            ([],),
            {"a": ()},
            {"a": 0, "b": [{"c": 1}]},
            {"a": 0, "b": [1, {"c": 2}, O(3)], "c": (O(1, 2), 1)},
        ]

    def test_treemap(self):
        def run_test(pytree):
            def f(x):
                return x * 3

            sm1 = sum(map(tree_flatten(pytree)[0], f))
            sm2 = tree_flatten(tree_map(f, pytree))[0]
            self.assertEqual(sm1, sm2)

            def invf(x):
                return x // 3

            self.assertEqual(tree_flatten(tree_flatten(pytree, f), invf), pytree)

            cases = [
                [()],
                ([],),
                {"a": ()},
                {"a": 1, "b": [{"c": 2}]},
                {"a": 0, "b": [2, {"c": 3}, 4], "c": (5, 6)},
            ]
            for case in cases:
                run_test(case)

    def test_treespec_repr(self):
        pytree = (0, [0, 0, 0])
        _, spec = tree_flatten(pytree)
        self.assertEqual(repr(spec), "T2#1#3($,L3#1#1#1($,$,$))")

    def test_custom_tree_node(self):
        class Point(object):
            def __init__(self, x, y, name):
                self.x = x
                self.y = y
                self.name = name

            def __repr__(self):
                return "Point(x:{}, y:{}, name: {})".format(self.x, self.y, self.name)

        def custom_flatten(p):
            children = [p.x, p.y]
            extra_data = p.name
            return (children, extra_data)

        def custom_unflatten(children, extra_data):
            return Point(*children, extra_data)

        register_custom(Point, custom_flatten, custom_unflatten)

        point = Point((1.0, 1.0, 1), 2.0, "point_name")
        children, spec = tree_flatten(point)
        point2 = tree_unflatten(children, spec)
        self.assertEqual(str(point), str(point2))

    def test_broadcast_to_and_flatten(self):
        cases = [
            (1, (), []),
            # Same (flat) structures
            ((1,), (0,), [1]),
            ([1], [0], [1]),
            ((1, 2, 3), (0, 0, 0), [1, 2, 3]),
            ({"a": 1, "b": 2}, {"a": 0, "b": 0}, [1, 2]),
            # Mismatched (flat) structures
            ([1], (0,), None),
            ([1], (0,), None),
            ((1,), [0], None),
            ((1, 2, 3), (0, 0), None),
            ({"a": 1, "b": 2}, {"a": 0}, None),
            ({"a": 1, "b": 2}, {"a": 0, "c": 0}, None),
            ({"a": 1, "b": 2}, {"a": 0, "b": 0, "c": 0}, None),
            # Same (nested) structures
            ((1, [2, 3]), (0, [0, 0]), [1, 2, 3]),
            ((1, [(2, 3), 4]), (0, [(0, 0), 0]), [1, 2, 3, 4]),
            # Mismatched (nested) structures
            ((1, [2, 3]), (0, (0, 0)), None),
            ((1, [2, 3]), (0, [0, 0, 0]), None),
            # Broadcasting single value
            (1, (0, 0, 0), [1, 1, 1]),
            (1, [0, 0, 0], [1, 1, 1]),
            (1, {"a": 0, "b": 0}, [1, 1]),
            (1, (0, [0, [0]], 0), [1, 1, 1, 1]),
            (1, (0, [0, [0, [], [[[0]]]]], 0), [1, 1, 1, 1, 1]),
            # Broadcast multiple things
            ((1, 2), ([0, 0, 0], [0, 0]), [1, 1, 1, 2, 2]),
            ((1, 2), ([0, [0, 0], 0], [0, 0]), [1, 1, 1, 1, 2, 2]),
            (([1, 2, 3], 4), ([0, [0, 0], 0], [0, 0]), [1, 2, 2, 3, 4, 4]),
        ]
        for pytree, to_pytree, expected in cases:
            _, to_spec = tree_flatten(to_pytree)
            result = broadcast_to_and_flatten(pytree, to_spec)
            self.assertEqual(result, expected, msg=str([pytree, to_spec, expected]))


if __name__ == "__main__":
    unittest.main()
