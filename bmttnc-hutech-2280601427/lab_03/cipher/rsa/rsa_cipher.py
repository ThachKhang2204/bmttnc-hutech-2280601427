import rsa
import os

class RSACipher:
    def __init__(self):
        self.key_dir = 'cipher/rsa/keys'
        os.makedirs(self.key_dir, exist_ok=True)

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(1024)

        with open(f'{self.key_dir}/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open(f'{self.key_dir}/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        public_key_path = f'{self.key_dir}/publicKey.pem'
        private_key_path = f'{self.key_dir}/privateKey.pem'

        if not os.path.exists(public_key_path) or not os.path.exists(private_key_path):
            raise FileNotFoundError("Chưa tạo khóa RSA! Vui lòng chạy API /api/rsa/gen_keys trước.")

        with open(public_key_path, 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())

        with open(private_key_path, 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())

        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except:
            return False

    def sign(self, message, key):
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('utf-8'), signature, key) == 'SHA-1'
        except:
            return False
