import sys

def xor_encrypt(input_file, output_file, xor_key):
    try:
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                while True:
                    byte = f_in.read(1)
                    if not byte:
                        break  # End of file
                    encrypted_byte = bytes([byte[0] ^ xor_key])
                    f_out.write(encrypted_byte)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 xor_encrypt.py <input file> <output file> <xor key>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        xor_key = int(sys.argv[3])
    except ValueError:
        print("Error: XOR key must be an integer")
        sys.exit(1)

    xor_encrypt(input_file, output_file, xor_key)
    print(f"Encryption with XOR key {xor_key} completed. Encrypted file saved as {output_file}")
