"""
analysis.py
Cryptographic property analysis of the AES S-box
- Differential uniformity
- (Nonlinearity value is well-known: 112)
"""

from aes_sbox import generate_aes_sbox


def differential_uniformity(sbox: list[int]) -> int:
    """
    Compute the differential uniformity (delta) of the S-box.
    delta = max number of solutions to S(x) ⊕ S(x ⊕ α) = β for α ≠ 0
    AES target: 4
    """
    max_count = 0

    for alpha in range(1, 256):  # nonzero input differences
        count = [0] * 256
        for x in range(256):
            output_diff = sbox[x] ^ sbox[x ^ alpha]
            count[output_diff] += 1

        current_max = max(count)
        if current_max > max_count:
            max_count = current_max

    return max_count


if __name__ == "__main__":
    print("Running cryptographic analysis...\n")
    sbox = generate_aes_sbox()

    delta = differential_uniformity(sbox)
    print(f"Differential Uniformity (δ): {delta}")
    print("AES S-box known nonlinearity (NL): 112")
    print("\nConclusion: Very strong resistance to differential cryptanalysis (δ=4)")