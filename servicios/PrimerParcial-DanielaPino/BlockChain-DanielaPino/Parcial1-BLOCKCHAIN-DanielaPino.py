import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()
    
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        block_hash = hashlib.sha256(block_contents.encode())
        return block_hash.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis block", "0")

    def add_block(self, block):
        block.previous_hash = self.chain[-1].hash
        self.chain.append(block)

    def print_blocks(self):
        for i in range(len(self.chain)):
            block = self.chain[i]
            print("Block {}:".format(i))
            print("Data: {}".format(block.data))
            print("Previous Hash: {}".format(block.previous_hash))
            print("Hash: {}".format(block.hash))
            print("Timestamp: {}".format(block.timestamp))
            print()

blockchain = Blockchain()
blockchain.add_block(Block("First block data", "genesis_block_hash"))
blockchain.add_block(Block("Second block data", blockchain.chain[-1].hash))
blockchain.add_block(Block("Third block data", blockchain.chain[-1].hash))

blockchain.print_blocks()
