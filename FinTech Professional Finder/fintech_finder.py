# Cryptocurrency Wallet
################################################################################

# Imports
import streamlit as st
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Importing the Crypto Wallet functions from the `crypto_wallet.py` file
from crypto_wallet import generate_account, get_balance, send_transaction, get_eth_price

################################################################################
# Fintech Finder Candidate Information

# Simple Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# Function to get candidates from the db and show them in the Streamlit interface
def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(db_list)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Retrieving the account and geting its balance
account = generate_account()
balance = get_balance(w3, account.address)

# Displaying the current account balance in Streamlit Sidebar 
st.sidebar.write(f"Account Address: {account.address}")
# Write the client's Ethereum account address to the sidebar
st.sidebar.write(f"Account Balance: {balance: .5f} Ether")

st.sidebar.write("---------")

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', list(candidate_database.keys()))

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Calculating the total Wage in Ether and USD equivalent, if get_eth_price returns the current Ether price (see comments to get_eth_price function)
# Cakculates and shows the total Wage in Ether only if get_eth_price returns false value
# False can be returned in case of frequent events - more than five per minute - TBD: control requests - use the current price and request new if only more than 1 minute has passed
wage_in_ether = hourly_rate * hours
eth_price = get_eth_price()
if eth_price is not False:
    wage_in_usd = wage_in_ether * eth_price
    st.sidebar.markdown(f"## Total Wage in Ether: {wage_in_ether: .2f}")
    st.sidebar.markdown(f"### Wage in USD equivalent: {wage_in_usd: .2f} (${eth_price} / Ether)")
else:
    st.sidebar.markdown(f"## Total Wage in Ether: {wage_in_ether: .2f}")


################################################################################
# Step 2: Sign and Execute a Payment Transaction

if st.sidebar.button("Send Transaction"):

    # Creating the transaction from the given client's account to the candidate's account in amount of calculated wage in Ether
    transaction_hash = send_transaction(w3, account, candidate_address, wage_in_ether)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()