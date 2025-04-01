from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Tạo block đầu tiên với proof = 1 và previous_hash là '0'
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Làm trống danh sách các giao dịch sau khi đã tạo block
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        # Cố gắng tìm proof hợp lệ
        while not check_proof:
            # Tính toán hash từ sự chênh lệch giữa hai proof
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # Nếu hash bắt đầu bằng '0000', thì proof là hợp lệ
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        # Thêm giao dịch vào danh sách các giao dịch
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        # Trả về chỉ mục của block tiếp theo sẽ chứa giao dịch này
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        # Kiểm tra tính hợp lệ của chuỗi blockchain
        while block_index < len(chain):
            block = chain[block_index]
            # Kiểm tra nếu hash của block hiện tại không khớp với previous_hash của block trước đó
            if block.previous_hash != previous_block.hash:
                return False
            previous_proof = previous_block.proof
            proof = block.proof
            # Kiểm tra nếu proof không hợp lệ
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
