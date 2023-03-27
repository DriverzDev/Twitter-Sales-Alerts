import asyncio
from flow_py_sdk import flow_client, Script
import csv

async def main():
    script_file = "read_total_supply.cdc"
    csv_file = "driverz_supply"

    async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
        with open(script_file, "r") as f:
            script_code = f.read()

        script = Script(code=script_code)
        result = await client.execute_script(script=script)

        total_supply = result.value

        print("Total Supply", total_supply)

        with open(csv_file, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Total Supply"])
            csvwriter.writerow([total_supply])

asyncio.run(main())
