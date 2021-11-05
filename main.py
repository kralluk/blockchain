# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import time
import hashlib
import json
import string
import random

class Block:
    hash = None
    previousHash = None
    data = None
    nonce = random.choice(string.ascii_letters)
    timestamp = time.time()

    def __init__(self, data, previousHash):
        self.previousHash = previousHash
        self.data = data

    def hashCalc(self):
        preHash = (self.previousHash + self.data + str(self.timestamp)+ self.nonce).encode("utf-8")
        self.hash = hashlib.sha256(preHash).hexdigest()
        return self.hash
    def jsonBlock(self):
        json_data = {"data":self.data, "timestamp":self.timestamp, "previusHash":self.previousHash, "hash":self.hash}
        print(json.dumps(json_data, indent=4))
        return json_data

    def mineBlock(self,difficulty):
        zeroamount = '0' * difficulty
        fhash = ""
        while(fhash.startswith(zeroamount)!=True):
            self.nonce += random.choice(string.ascii_letters)
            if (len(self.nonce) > 20):                            # pro urychlení procesu - pokud by se stalo, že se hash delší dobu
                self.nonce = random.choice(string.ascii_letters)  # nenajde, potobm by nonce byl moc velky a vypocet samotného hashe by zabral moc času
            fhash = self.hashCalc()

        self.hash = fhash
        return self.hash

    def isBlockValid(self):
        if(self.hash == self.hashCalc()):
            return True
        else:
            return False
    def BlockDataChange(self,chdata):
        self.data = chdata


difficulty = 6
blockchain = []

start = time.time()
blockchain.append(Block("Ahoj, ja jsem prvni blok", "0"))
print("Tezim blok 1... ")
blockchain[0].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[0].hash)

blockchain.append(Block("Ja jsem druhy", blockchain[0].hash))
print("Tezim blok 2... ")
blockchain[1].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[1].hash)

blockchain.append(Block("A ja treti", blockchain[1].hash))
print("Tezim blok 3... ")
blockchain[2].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[2].hash)
end = time.time()
print("\nTěžení bloků trvalo: ",end-start,"s")


# blockchain[1].BlockDataChange("Ja nejsem druhy") # <--- zmena dat v druhem bloku

def isChainValid():
    for i in range(len(blockchain)):
        if(blockchain[i].isBlockValid() == False):
            return False
    return True
print("\nBlockchain je platny: " + str(isChainValid()))
print("\nBlockchain:")

for i in range(len(blockchain)):
    blockchain[i].jsonBlock()
