#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
from manchester import Manchester

bits = '101010'
symbols = '100110011001'
diff_symbols = ['110100101101', '001011010010']
invert_bits = ''.join([i == '1' and '0' or '1' for i in bits])
invert_symbols = ''.join([i == '1' and '0' or '1' for i in symbols])
invert_diff_symbols = ['101101001011', '010010110100']

class ManchesterEncodeTests(unittest.TestCase):
    def setUp(self):
        self.codec = Manchester()

    def test_encode(self):
        self.assertEqual(self.codec.encode(bits), symbols)

    def test_invert_encode(self):
        self.codec.invert()
        self.assertEqual(self.codec.encode(bits), invert_symbols)

class ManchesterDecodeTests(unittest.TestCase):
    def setUp(self):
        self.codec = Manchester()

    def test_decode(self):
        self.assertEqual(self.codec.decode(symbols), bits)

    def test_invert_decode(self):
        self.codec.invert()
        self.assertEqual(self.codec.decode(symbols), invert_bits)

class DifferentialManchesterEncodeTests(unittest.TestCase):
    def setUp(self):
        self.codec = Manchester(differential=True)

    def test_encode(self):
        self.assertIn(self.codec.encode(bits), diff_symbols)
        for symbols in diff_symbols:
            init_level = symbols[0] == '1' and '0' or '1'
            self.assertEqual(self.codec.encode(bits, init_level=init_level), symbols)

    def test_invert_encode(self):
        self.assertIn(self.codec.encode(invert_bits), invert_diff_symbols)
        for symbols in invert_diff_symbols:
            init_level = symbols[0] == '1' and '0' or '1'
            self.assertEqual(self.codec.encode(invert_bits, init_level=init_level), symbols)

class DifferentialManchesterDecodeTests(unittest.TestCase):
    def setUp(self):
        self.codec = Manchester(differential=True)

    def test_decode(self):
        for symbols in diff_symbols:
            self.assertEqual(self.codec.decode(symbols), bits)

    def test_invert_decode(self):
        for invert_symbols in invert_diff_symbols:
            self.assertEqual(self.codec.decode(invert_symbols), invert_bits)

if __name__ == '__main__':
    unittest.main()
