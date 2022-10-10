from SimpleBlockChain import Block
from SimpleBlockChain import Blockchain
from time import time

TestChain = Blockchain()

TestChain.addBlock(Block(str(int(time())),({"from": "Person1","to":"Person2","amount":100})))

TestChain.addBlock(Block(str(int(time())),({"from": "Person3","to":"Person4","amount":100})))

print(TestChain)
print(TestChain.isValid())

TestChain.unValidateChain()

print(TestChain)
print(TestChain.isValid())