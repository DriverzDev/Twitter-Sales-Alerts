import csv
from flow_py_sdk import flow_client
import asyncio



async def event_listener(event_type: str):
    with open('nft_minted.csv', mode='a', newline='') as csvfile:
        fieldnames = ['nftID', 'ownerAddress']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        #block_height = 49070216

        async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
            latest_block = await client.get_latest_block()
        start_height = latest_block.height - 10
        print(f"Initial start_height: {start_height}")

        while True:

            async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
                latest_block = await client.get_latest_block()
            end_height = latest_block.height
            print(f"Querying events from height {start_height} to {end_height}")

            async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
                events = await client.get_events_for_height_range(
                    type = event_type, 
                    start_height=start_height, 
                    end_height=end_height
                )

            start_height = end_height
            

            if events:
                for event_response in events:
                    for event in event_response.events:
                        print(f"Event recieved: {event}")

                        nft_id = event.value.fields[0].value
                        owner_address = event.value.fields[0].value                
                    
                        nft_data = {
                            'nftID': event.payload.nftID,
                            'ownerAddress': owner_address
                        }

                        writer.writerow(nft_data)
                             
            await asyncio.sleep(10)

event_type = "A.a039bd7d55a96c0c.DriverzNFT.Withdraw"
    
asyncio.run(event_listener(event_type))
