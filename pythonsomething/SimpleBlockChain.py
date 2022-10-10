from hashlib import sha256
from time import time
import json


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.prevHash = None
        self.nonce = 0
        self.hash = self.getHash()

    def getHash(self):
        hash = sha256()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()

    def mine(self,diff):
        while self.hash[:diff] != '0' * diff:
            self.nonce += 1
            self.hash = self.getHash()

class Blockchain:
    def __init__(self):
        self.chair = [Block(str(int(time())))]
        self.diffinulty = 1

    def getLastBlockUwU(self):
        return self.chair[len(self.chair)-1]

    def addBlock(self, block):
        block.prevHash = self.getLastBlockUwU().hash
        block.hash = block.getHash()
        block.mine(self.diffinulty)
        self.chair.append(block)

    def isValid(self):
        for i in range(1, len(self.chair)):
            currentBlock = self.chair[i]
            prevBlock = self.chair[i-1]

            if (currentBlock.hash != currentBlock.getHash() or prevBlock.hash != currentBlock.prevHash):
                return False

        return True

    def unValidateChain(self):
        self.chair[1].data = ["hi"]
        self.chair[1].timestamp = 69
        self.chair[1].hash = self.chair[1].getHash()

    def __repr__(self):
        return json.dumps([{'data': item.data, 'timestamp':item.timestamp, 'nonce':item.nonce,'hash':item.hash, 'prevHash':item.prevHash}for item in self.chair], indent=4)

