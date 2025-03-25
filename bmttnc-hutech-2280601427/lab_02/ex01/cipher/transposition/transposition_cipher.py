class TranspositionCipher:
    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            if row == key or (row == key - 1 and col >= len(text) % key):
                row = 0
                col += 1
        return ''.join(decrypted_text)
