class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt(self, plain_text, key):  # 🔹 Đổi tên từ rail_fence_encrypt -> encrypt
        rails = [[] for _ in range(key)]
        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction

        cipher_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text

    def decrypt(self, cipher_text, key):  # 🔹 Đổi tên từ rail_fence_decrypt -> decrypt
        rail_lengths = [0] * key
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction

        return plain_text
