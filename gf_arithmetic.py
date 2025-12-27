"""
gf_arithmetic.py
Core GF(2^8) arithmetic operations for AES S-box generation
"""

IRREDUCIBLE = 0x11B  # x^8 + x^4 + x^3 + x + 1


def gf_mul(a: int, b: int) -> int:
    """
    Multiply two elements in GF(2^8) using Russian peasant multiplication
    with reduction modulo the AES irreducible polynomial (0x11B).
    """
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= IRREDUCIBLE
        a &= 0xFF
        b >>= 1
    return result


def gf_inverse(a: int) -> int:
    """
    Compute the multiplicative inverse in GF(2^8).
    Returns 0 for input 0 (AES convention).
    Uses brute-force search (acceptable for small field size 256).
    """
    if a == 0:
        return 0

    for i in range(1, 256):
        if gf_mul(a, i) == 1:
            return i

    raise ValueError("No inverse found - field arithmetic error")


def gf_inverse_extended_euclidean(a: int) -> int:
    """
    Alternative: Extended Euclidean Algorithm version (more efficient in theory).
    Included for completeness / educational purpose.
    """
    if a == 0:
        return 0

    old_r, r = IRREDUCIBLE, a
    old_s, s = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r ^ gf_mul(quotient, r)
        old_s, s = s, old_s ^ gf_mul(quotient, s)

    return old_s & 0xFF