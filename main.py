import hashlib

Nounce_lim = 1000000000000
zeros = 4

block_number = int(input("block_number : "))   #Exemple : 12#
transactions = input("transactions : ")  #Exemple : 76123fcj2487#
previous_hash = input("previous_hash : ") #Exemple : 869de875jj967c87#

def mine(block_number, transactions, previous_hash):
    for nonce in range(Nounce_lim):
        base_text = str(block_number)+ transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeros):
            print(f"Found Hash With Nounce: {nonce}")
            return hash_try

mine(block_number, transactions, previous_hash)