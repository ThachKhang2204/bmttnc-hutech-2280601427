from flask import Flask, request, jsonify
from cipher.rsa.rsa_cipher import RSACipher

app = Flask(__name__)
rsa_cipher = RSACipher()

@app.route("/api/rsa/gen_keys", methods=["POST"])
def gen_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data.get('message')
    keytype = data.get('keytype')

    if not message or keytype not in ['public', 'private']:
        return jsonify({'error': 'Invalid input'}), 400

    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if keytype == 'public' else private_key

    encrypted_message = rsa_cipher.encrypt(message, key)
    return jsonify({'encrypted_message': encrypted_message.hex()})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data.get('cipher_text')
    key_type = data.get('keytype')

    if not ciphertext_hex or key_type not in ['public', 'private']:
        return jsonify({'error': 'Invalid input'}), 400

    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == 'public' else private_key

    try:
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = rsa_cipher.decrypt(ciphertext, key)
        if decrypted_message is False:
            return jsonify({'error': 'Decryption failed'}), 400
        return jsonify({'decrypted_message': decrypted_message})
    except:
        return jsonify({'error': 'Invalid ciphertext format'}), 400

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    data = request.json
    message = data.get('message')
    signature_hex = data.get('signature')

    if not message or not signature_hex:
        return jsonify({'error': 'Message and signature are required'}), 400

    _, public_key = rsa_cipher.load_keys()

    try:
        signature = bytes.fromhex(signature_hex)
        is_verified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({'verified': is_verified})
    except:
        return jsonify({'error': 'Invalid signature format'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
