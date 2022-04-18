# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons. By using import statements, you will integrate this `crypto_wallet.py` Python script into the Fintech Finder interface program that is found in the `fintech_finder.py` file.

################################################################################
# Imports
import pandas as pd
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.gas_strategies.time_based import medium_gas_price_strategy

################################################################################
# Wallet functionality

# Function that returns the current Ether price in USD. 
# If there is no Alpha Vintage key specified in .env file the function returns false value
# If API call or further transformation return errors the function returns flase value
# Otherwise the function returns the current Ether price

# NOTE: Alpha Vantage by default is limited by 5 requests per minute, frequent calls will cause an error and the corresponding behavior in web interface
def get_eth_price():
    # Fetch Alpha Vantage API key from the environment variable 
    av_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if av_api_key is None:
        return False
    else: 
        url = f"https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD&interval=1min&apikey={av_api_key}"
        try:
            response = requests.get(url).json()
            df = pd.DataFrame(response['Time Series Crypto (1min)']).T
            price = df.iloc[0]['4. close']
        except:
            return False
    return float(price)
    

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from the environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account

def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in ether
    return ether


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(wage, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Testing generate_account and get_balance functions
#print(get_balance(Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545')), generate_account().address))
