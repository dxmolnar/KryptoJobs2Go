# Cryptocurrency Wallet

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv('secret.env')
from bip44 import Wallet
from web3 import Web3
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

################################################################################
# Wallet functionality

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")
    mnemonic_str = str(mnemonic)

    # Create Wallet Object
    wallet = Wallet(mnemonic_str)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.from_key(private)

    return account

def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address) # changed from web3

    # Convert Wei value to ether
    ether_balance = w3.from_wei(wei_balance, "ether") # changed from web3

    # Return the value in ether
    return ether_balance

def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    wei_value = w3.eth.to_wei(wage, "ether") #changed from to_wei

    # Calculate gas estimate
    gas_estimate = w3.eth.estimateGas( #changed from gas_estimate, estimate_gas
        {"to": to, "from": account.address, "value": wei_value}
    )
    # Get the current gas price using the medium_gas_price_strategy
    gas_price = medium_gas_price_strategy(w3, None) #-d out

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": wei_value,
        "gas": gas_estimate, #changed from gas_estimate
        "gasPrice": 975000000, #changed from 975000000
        "nonce": w3.eth.getTransactionCount(account.address), #changed from get_transaction_count
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)