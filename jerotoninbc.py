import hashlib
from data import *

class Jerotoninbc:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# Define a function to limit each block to 256 transactions
def limit_transactions(transactions):
    # Split the transactions into chunks of 256
    transaction_chunks = [transactions[i:i+256] for i in range(0, len(transactions), 256)]
    # Create a list of blocks, where each block contains up to 256 transactions
    blocks = []
    previous_block_hash = 'Initial String'
    for chunk in transaction_chunks:
        block = Jerotoninbc(previous_block_hash, chunk)
        blocks.append(block)
        previous_block_hash = block.block_hash
    return blocks

# Get a list of all transactions
transactions = [globals()[f"t{i+1}"] for i in range(6)]

# Limit the transactions to 256 per block
blocks = limit_transactions(transactions)

# Print the description and hash for each block
for i, block in enumerate(blocks):
    print(f"Block {i+1} - Description: {'-'.join(block.transaction_list)} - Hash: {block.block_hash}")
