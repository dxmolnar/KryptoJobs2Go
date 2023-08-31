![An image shows a wallet with bitcoin.](Images/19-4-challenge-image.png)

# KryptoJobs2Go 
This is a web application that allows users to hire Fintech professionals using Ether as a form of payment. The application is built on Python and uses the web3 and Streamlit libraries to integrate with the Ethereum blockchain.

## The application consists of two Python scripts:

crypto_wallet.py: This script contains functions for generating Ethereum accounts, retrieving account balances, and sending transactions.

krypto_jobs.py: This script is the main application. It uses Streamlit to create an interactive web interface where users can select candidates to hire, enter the number of hours worked, and send payments in Ether.

## To set up and run the application, you will need:

1. Python 3.7 or newer
2. The web3 and Streamlit libraries
3. A mnemonic seed phrase for your Ethereum wallet

Once you have all of the required dependencies, you can set up the application by following these steps:

1. Clone the repository
2. Install the required dependencies by running pip install -r requirements.txt
3. Create a .env file and add your mnemonic seed phrase as an environment variable
4. Start the Streamlit application by running streamlit run krypto_jobs.py
   
The application will then be available at the local or network URL provided by Streamlit.


