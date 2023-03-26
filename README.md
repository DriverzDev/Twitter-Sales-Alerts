TOC

1. DriverzNFT Withdraw Event Listener



1. DriverzNFT Withdraw Event Listener

This script (read_id_owneraddress_on_withdraw.py) listens for the Withdraw event from the DriverzNFT smart contract on the Flow blockchain, and writes the NFT IDs and their owner addresses to a CSV file called nft_minted.csv.

Requirements
Python 3.7+
flow-py-sdk

Installation
Install Python 3.7+ if you haven't already.
Install the required Python package (flow-py-sdk) by running the following line in Powershell from the Scripts directory of your Python installation:

pip install flow-py-sdk

Run the script with the following command from the directory where the script is located:

python read_id_owneraddress_on_withdraw.py

The script will continuously listen for the Withdraw events on the Flow blockchain and write the NFT ID and owner address to the nft_minted.csv file. The file will be created in the same directory as the script if it doesn't already exist. If it does exist, new data will be appended to the file.

The script queries events from the last 10 blocks and checks for new events every 10 seconds.

Notes

 - This script uses the Flow Mainnet Access Node, access.mainnet.nodes.onflow.org with port 9000. To use a different access node or network, update the flow_client instance's host and port in the script accordingly.
 - The script only listens for the Withdraw event of the DriverzNFT contract. If you want to listen to a different event, modify the event_type variable at the end of the script.