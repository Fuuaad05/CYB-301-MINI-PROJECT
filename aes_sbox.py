"""
aes_sbox.py
Generates the AES S-box using multiplicative inverse + affine transformation
"""

from gf_arithmetic import gf_inverse, gf_mul


def affine_transform(byte: int) -> int:
    """
    Apply the AES affine transformation over GF(2):
    s = A * inv(byte) + 0x63 (matrix-vector multiplication in GF(2))
    """
    # AES affine matrix (rows from top to bottom)
    # Each row defines which input bits are XORed to produce output bit
    result = 0

    # We can use the bit-wise formulation (most common implementation)
    x = byte

    result |= ((x >> 0) & 1) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1) ^ ((x >> 6) & 1) ^ ((x >> 7) & 1) ^ 1
    result |= (((x >> 0) & 1) ^ ((x >> 1) & 1) ^ ((x >> 5) & 1) ^ ((x >> 6) & 1) ^ ((x >> 7) & 1) ^ 1) << 1
    result |= (((x >> 0) & 1) ^ ((x >> 1) & 1) ^ ((x >> 2) & 1) ^ ((x >> 6) & 1) ^ ((x >> 7) & 1) ^ 0) << 2
    result |= (((x >> 0) & 1) ^ ((x >> 1) & 1) ^ ((x >> 2) & 1) ^ ((x >> 3) & 1) ^ ((x >> 7) & 1) ^ 0) << 3
    result |= (((x >> 0) & 1) ^ ((x >> 1) & 1) ^ ((x >> 2) & 1) ^ ((x >> 3) & 1) ^ ((x >> 4) & 1) ^ 0) << 4
    result |= (((x >> 1) & 1) ^ ((x >> 2) & 1) ^ ((x >> 3) & 1) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1) ^ 1) << 5
    result |= (((x >> 2) & 1) ^ ((x >> 3) & 1) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1) ^ ((x >> 6) & 1) ^ 1) << 6
    result |= (((x >> 3) & 1) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1) ^ ((x >> 6) & 1) ^ ((x >> 7) & 1) ^ 0) << 7

    return result


def generate_aes_sbox() -> list[int]:
    """
    Generate the full 256-byte AES S-box.
    Returns: list of 256 integers (0-255)
    """
    sbox = [0] * 256

    for i in range(256):
        # Step 1: Multiplicative inverse (0 -> 0 by AES convention)
        inv = gf_inverse(i)
        # Step 2: Apply affine transformation
        sbox[i] = affine_transform(inv)

    return sbox


def print_sbox(sbox: list[int]):
    """Pretty-print the S-box in 16x16 hex format"""
    print("AES S-box (hex):")
    print("   " + " ".join(f"{j:02x}" for j in range(16)))
    for i in range(16):
        row = sbox[i*16 : (i+1)*16]
        print(f"{i:x}0 " + " ".join(f"{x:02x}" for x in row))


if __name__ == "__main__":
    # Quick test
    sbox = generate_aes_sbox()
    print_sbox(sbox)
    # Known values
    print("\nVerification:")
    print(f"sbox[0x00] = 0x{sbox[0x00]:02x}  (should be 63)")
    print(f"sbox[0x01] = 0x{sbox[0x01]:02x}  (should be 7c)")
    print(f"sbox[0x53] = 0x{sbox[0x53]:02x}  (should be ed)")