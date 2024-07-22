#!/usr/bin/python3
"""Validation of UTF-8"""


def get_bits(num):
    """returns the number bits"""
    bits = 0
    helper = 1 << 7
    while helper & num:
        bits += 1
        helper = helper >> 1
    return bits


def validUTF8(data):
    """determines a valid UTF8"""
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_bits(data[i])
            if bits_count == 0:
                continue
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
