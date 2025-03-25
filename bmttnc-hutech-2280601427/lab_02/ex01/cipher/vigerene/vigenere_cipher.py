class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""  # ✅ Khởi tạo biến trước khi sử dụng
        key_index = 0
        
        for char in plain_text:
            if char.isalpha():  # ✅ Kiểm tra chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
                else:
                    encrypted_text += chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
                key_index += 1  # ✅ Chỉ tăng khi gặp ký tự chữ cái
            else:
                encrypted_text += char  # ✅ Giữ nguyên ký tự đặc biệt
        
        return encrypted_text

    def vigenere_decrypt(self, cipher_text, key):
        decrypted_text = ""  # ✅ Khởi tạo biến trước khi sử dụng
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr(((ord(char) - ord('A') - key_shift) % 26) + ord('A'))
                else:
                    decrypted_text += chr(((ord(char) - ord('a') - key_shift) % 26) + ord('a'))
                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text
