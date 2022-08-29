import hashlib

class ProofOfWork():
    def __init__(self,block):
        self.block = block
    def mine(self):
        i = 0

        prefix = '0000'

        while True:
            nonce = str(i)
            message = hashlib.sha256()
            message.update(str(self.block.data).encode('utf-8'))
            message.update(nonce.encode('utf-8'))
            digest = message.hexdigest()
            if digest.startswith(prefix):
                return nonce,digest

            i+=1


class Block:
    def __init__(self,data,perv_hash):
        self.pervious_hash = perv_hash
        self.data = data
        self.nonce = 0

    @property
    def hash(self):
        message = hashlib.sha256()
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.nonce).encode('utf-8'))
        digest = message.hexdigest()
        return digest


def create_genesis_block():
    block = Block(data = 'Genesis Block',perv_hash = '')
    pow = ProofOfWork(block)
    nonce ,digest = pow.mine()
    block.nonce = nonce
    return block

class BLockChain:
    def __init__(self):
        self.blocks = [create_genesis_block()]
    def add_block(self,data):
        prev_block = self.blocks[len(self.blocks)-1]
        block = Block(data,prev_block.hash)
        pow = ProofOfWork(block)
        nonce ,digest = pow.mine()
        block.nonce = nonce
        self.blocks.append(block)
        return block


bc = BLockChain()

b1 = bc.add_block('Jack Send 0.3 btc to Alice')
b2 = bc.add_block('Alice Send 0.1 btc to Tom')


for b in bc.blocks:
    print('Prev Hash :{}'.format(b.pervious_hash))
    print("data:{}".format(b.data))
    print("Hash:{}".format(b.hash))
    print('\n')




