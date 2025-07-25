from itertools import islice
import unittest

from pe import sequences


class TestTriangulars(unittest.TestCase):
    triangle_numbers = [
        0,
        1,
        3,
        6,
        10,
        15,
        21,
        28,
        36,
        45,
        55,
        66,
        78,
        91,
        105,
        120,
        136,
        153,
        171,
        190,
        210,
        231,
        253,
        276,
        300,
        325,
        351,
        378,
        406,
        435,
        465,
        496,
        528,
        561,
        595,
        630,
        666,
    ]

    def test_sequence(self):
        tris = sequences.Triangulars()
        for i, n in enumerate(self.triangle_numbers):
            # test contains
            self.assertTrue(n in tris)
            # test getitem
            self.assertEqual(n, tris[i])
            # test index
            self.assertEqual(i, tris.index(n))

        # test iter
        self.assertSequenceEqual(self.triangle_numbers, list(islice(tris, len(self.triangle_numbers))))
        # test getitem slice
        self.assertSequenceEqual(self.triangle_numbers[2:18:3], tris[2:18:3])

    def test_failures(self):
        tris = sequences.Triangulars()

        self.assertFalse(-1 in tris)
        self.assertFalse(625 in tris)
        with self.assertRaises(IndexError):
            tris[-1]
        with self.assertRaises(ValueError):
            tris.index(-1)
        with self.assertRaises(ValueError):
            tris.index(2)
        with self.assertRaises(ValueError):
            tris[5:]


class TestPentagonals(unittest.TestCase):
    pentagonal_numbers = [
        0,
        1,
        5,
        12,
        22,
        35,
        51,
        70,
        92,
        117,
        145,
        176,
        210,
        247,
        287,
        330,
        376,
        425,
        477,
        532,
        590,
        651,
        715,
        782,
        852,
        925,
        1001,
        1080,
        1162,
        1247,
        1335,
        1426,
        1520,
        1617,
        1717,
        1820,
        1926,
        2035,
        2147,
        2262,
        2380,
        2501,
        2625,
        2752,
        2882,
        3015,
        3151,
    ]

    def test_sequence(self):
        pents = sequences.Pentagonals()
        for i, n in enumerate(self.pentagonal_numbers):
            # test contains
            self.assertTrue(n in pents)
            # test getitem
            self.assertEqual(n, pents[i])
            # test index
            self.assertEqual(i, pents.index(n))

        # test iter
        self.assertSequenceEqual(self.pentagonal_numbers, list(islice(pents, len(self.pentagonal_numbers))))
        # test getitem slice
        self.assertSequenceEqual(self.pentagonal_numbers[2:18:3], pents[2:18:3])

    def test_failures(self):
        pents = sequences.Pentagonals()

        self.assertFalse(-1 in pents)
        self.assertFalse(4 in pents)
        with self.assertRaises(IndexError):
            pents[-1]
        with self.assertRaises(ValueError):
            pents.index(-1)
        with self.assertRaises(ValueError):
            pents.index(4)
        with self.assertRaises(ValueError):
            pents[5:]
