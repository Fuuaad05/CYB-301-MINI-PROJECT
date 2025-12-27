# AES S-box Algebraic Analysis  
**CYB 301 Mini Project – Cryptographic Techniques and Their Applications**  
2025/2026 Session

Implementation of the AES (Rijndael) S-box generation using finite field arithmetic over **GF(2⁸)**, including:
- Field multiplication and inversion
- Affine transformation
- Full S-box table generation
- Basic cryptographic property analysis (differential uniformity)

## Project Structure
crypto_project/
├── gf_arithmetic.py        # GF(2^8) core operations (mul, inverse)
├── aes_sbox.py             # S-box generation + affine transform
├── analysis.py             # Cryptographic metrics (differential uniformity)
├── README.md               # This file
└── requirements.txt        # (empty – pure Python, no external packages)


## Features

- Correct AES S-box generation (matches official values: `sbox[0x00] = 0x63`, `sbox[0x53] = 0xed`, etc.)
- Clean, commented code with meaningful variable names
- Simple brute-force inverse (educational & sufficient for GF(256))
- Differential uniformity computation (expected result: **4**)

## How to Run

Make sure you have **Python 3.8+** installed.

### 1. Generate and display the full AES S-box

```bash
python aes_sbox.py
```

### 2. Run cryptographic analysis (differential uniformity)

```bash
python analysis.py
```

Expected result:

```
Differential Uniformity (δ): 4
AES S-box known nonlinearity (NL): 112
```

### Quick verification of key values
You can also run this tiny snippet in any Python shell:

```bash
from aes_sbox import generate_aes_sbox
sbox = generate_aes_sbox()
print(f"sbox[0x00] = 0x{sbox[0]:02x}")     # Should be 63
print(f"sbox[0x01] = 0x{sbox[1]:02x}")     # Should be 7c
print(f"sbox[0x53] = 0x{sbox[0x53]:02x}")  # Should be ed
```

## Requirements

- Python 3.8 or higher
- No external libraries needed

## License
Educational / Academic use only 




