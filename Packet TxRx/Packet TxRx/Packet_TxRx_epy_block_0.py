import numpy as np
from gnuradio import gr


class SimpleXOREncrypt(gr.sync_block):
    """Embedded Python Block example - simple XOR-based encryption"""

    def __init__(self, xor_key=0xAA):
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Simple XOR Encrypt',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )

        # XOR key for encryption
        self.xor_key = xor_key

    def work(self, input_items, output_items):
        """simple XOR-based encryption for every byte"""
        input_data = np.frombuffer(input_items[0], dtype=np.uint8)

        # Encrypt every byte using XOR
        encrypted_data = input_data ^ self.xor_key

        # Copy the encrypted data to the output buffer
        np.copyto(output_items[0], encrypted_data)

        return len(output_items[0])




