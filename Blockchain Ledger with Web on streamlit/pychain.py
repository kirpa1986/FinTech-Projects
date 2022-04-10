# PyChain Ledger
################################################################################

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Defining Record class - unit that consists of the data about the financial transaction - sender, receiver and the amount of the transaction
@dataclass
class Record:
    sender: int
    receiver: int
    amount: float
    

################################################################################
# Defing Block Data class to store financial transaction (object of Data class) along with other block metadata
@dataclass
class Block:
    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%M-%d-%Y %H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

################################################################################
# Defining the PyChain class which stores the chain of Blocks and provides functions for adding new blocks with Proof of Work calculations based on the difficulty parameter set for the chain
@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True


################################################################################
# Defining a function to initiate the chain with Genesis block
@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


# Initializing the chain and assignin it to the pychain variable
pychain = setup()


################################################################################
# Adding Relevant User Inputs to the Streamlit Interface

with st.sidebar:
    #Adding block difficulty configuration
    st.header("New Block Configuration")
    difficulty = st.slider("Block Difficulty", 1, 5, 2)
    pychain.difficulty = difficulty
    
    #Adding user input fields
    st.header("Add new Transaction Record to the PyChain")
    sender_input = st.text_input("Sender")
    receiver_input = st.text_input("Receiver")
    amount_input = st.text_input("Transaction Amount")

    #Adding button to run adding new block to the chain
    if st.button("Add Block"):
        prev_block = pychain.chain[-1]
        prev_block_hash = prev_block.hash_block()
        new_block = Block(record = Record(sender = sender_input, receiver = receiver_input, amount = amount_input), creator_id = 1, prev_hash=prev_block_hash)
        with st.spinner("It may take some time"):
            pychain.add_block(new_block)
        st.balloons()


#Showing the whole PyChain Ledger as a DataFrame in the Streamlit Interface
st.header("The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
pychain_df.columns = ['Record', 'Creator ID', 'Previous Hash', 'Timestamp', 'Nonce']
st.write(pychain_df)

#Adding button to validate the chain
if st.button("Validate Chain"):
    if pychain.is_valid():
        st.write("Great! Chain is valid!")
        
    else:
        st.write("Oooops! Chain is invalid!")

#Adding Block Inspection functionality to the Streamlit Interface
st.header("Block Inspector")
selected_block = st.selectbox("Which block would you like to see?", pychain.chain)
st.write(selected_block)



################################################################################
# Step 4:
# Test the PyChain Ledger by Storing Records

# Test your complete `PyChain` ledger and user interface by running your
# Streamlit application and storing some mined blocks in your `PyChain` ledger.
# Then test the blockchain validation process by using your `PyChain` ledger.
# To do so, complete the following steps:

# 1. In the terminal, navigate to the project folder where you've coded the
#  Challenge.

# 2. In the terminal, run the Streamlit application by
# using `streamlit run pychain.py`.

# 3. Enter values for the sender, receiver, and amount, and then click the "Add
# Block" button. Do this several times to store several blocks in the ledger.

# 4. Verify the block contents and hashes in the Streamlit drop-down menu.
# Take a screenshot of the Streamlit application page, which should detail a
# blockchain that consists of multiple blocks. Include the screenshot in the
# `README.md` file for your Challenge repository.

# 5. Test the blockchain validation process by using the web interface.
# Take a screenshot of the Streamlit application page, which should indicate
# the validity of the blockchain. Include the screenshot in the `README.md`
# file for your Challenge repository.
