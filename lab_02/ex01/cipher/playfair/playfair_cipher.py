class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        unique_key = ""
        for char in key:
            if char not in unique_key:
                unique_key += char

        remaining_letters = [letter for letter in alphabet if letter not in unique_key]
        combined_letters = unique_key + "".join(remaining_letters)

        playfair_matrix = [list(combined_letters[i:i + 5]) for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, letter, matrix):
        """Tìm tọa độ (row, col) của chữ cái trong ma trận"""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Trả về None nếu không tìm thấy

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
            if len(pair) == 1:
                pair += "X"

            row1_col1 = self.find_letter_coords(pair[0], matrix)
            row2_col2 = self.find_letter_coords(pair[1], matrix)

            if row1_col1 is None or row2_col2 is None:
                raise ValueError(f"Lỗi: Một trong các ký tự '{pair}' không tồn tại trong ma trận!")

            row1, col1 = row1_col1
            row2, col2 = row2_col2

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        """Giải mã văn bản đã mã hóa bằng PlayFair"""
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1_col1 = self.find_letter_coords(pair[0], matrix)
            row2_col2 = self.find_letter_coords(pair[1], matrix)

            if row1_col1 is None or row2_col2 is None:
                raise ValueError(f"Lỗi: Một trong các ký tự '{pair}' không tồn tại trong ma trận!")

            row1, col1 = row1_col1
            row2, col2 = row2_col2

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text
