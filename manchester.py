#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Manchester(object):
    """
    G. E. Thomas: 0 = 01, 1 = 10
    ISO 802.4: 0 = 10, 1 = 01
    """
    _bit_symbol_map = {
        # bit: symbol
        '0': '01',
        '1': '10',
        'invert': {
            # bit: symbol
            '0': '10',
            '1': '01'},
        'differential': {
            # (init_level, bit): symbol
            ('1', '0'): '01',
            ('0', '0'): '10',
            ('0', '1'): '11',
            ('1', '1'): '00'
        }
    }

    def __init__(self, differential=False, invert=False):
        self._invert = invert
        self._differential = differential
        self._init_level = '0'

    def invert(self):
        self._invert = not self._invert

    def differential(self):
        self._differential = not self._differential

    def encode(self, bits, init_level=None):
        if init_level:
            self._init_level = init_level

        symbols = ''
        for bit in bits:
            # Differential Manchester Coding
            if self._differential:
                symbols += self._bit_symbol_map['differential'][(self._init_level, bit)]
                self._init_level = symbols[-1]
                continue

            # IEEE 802.4 (Inverted Manchester Coding)
            if self._invert:
                symbols += self._bit_symbol_map['invert'][bit]
                continue

            # Manchester Coding
            symbols += self._bit_symbol_map[bit]

        return symbols

    def decode(self, symbols):
        bits = ''
        while len(symbols):
            symbol = symbols[0:2]
            symbols = symbols[2:]

            if self._differential:
                for ib, s in self._bit_symbol_map['differential'].items():
                    if symbol == s:
                        bits += ib[1]
                continue

            if self._invert:
                for b, s in self._bit_symbol_map['invert'].items():
                    if symbol == s:
                        bits += b
                continue

            for b, s in self._bit_symbol_map.items():
                if symbol == s:
                    bits += b

        return bits
