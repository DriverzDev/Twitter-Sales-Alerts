import os 
import csv
import asyncio
from flow_py_sdk import flow_client, Script
from flow_py_sdk.cadence import decode, Address, UInt64

async def main():
    user_address = "0x759761445426d6b0"
    nft_id = UInt64(4393)
    address = Address.from_hex(user_address)
    script_file = "readDriverzPublicData.cdc"
    csv_file = "nft_metadata.csv"

    async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
        latest_block = await client.get_latest_block()
        block_id = latest_block.id

        with open(script_file, "r") as f:
            script_code = f.read()

        script = Script(code=script_code, arguments=[address, nft_id])
        result = await client.execute_script(script=script)

        if result is not None:
            metadata = decode(result.value, t=dict)

            with open(csv_file, "w", newline="") as csvfile:
                fieldnames = list(metadata.keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(metadata)

            print(f"Metadata for NFT ID {nft_id} has been writtern to {csv_file}")
        else:
            print(f"No metadata found for NFT ID {nft_id}")

if __name__ == "__main__":
    asyncio.run(main())



