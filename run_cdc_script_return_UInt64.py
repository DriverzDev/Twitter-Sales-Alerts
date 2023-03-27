import asyncio
from flow_py_sdk import flow_client, Script
import csv

flag_tot_sup = False
flag_ext_url = True

async def main():
    if flag_tot_sup:
        script_file = "read_total_supply.cdc"
        csv_file = "driverz_supply.csv"
    elif flag_ext_url:
        script_file = "read_external_url.cdc"
        csv_file = "driverz_external_url.csv"

    async with flow_client(host="access.mainnet.nodes.onflow.org", port=9000) as client:
        with open(script_file, "r") as f:
            script_code = f.read()

        script = Script(code=script_code)
        result = await client.execute_script(script=script)

        if flag_tot_sup:

            total_supply = result.value
            print("Total Supply", total_supply)

            with open(csv_file, "w", newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(["Total Supply"])
                csvwriter.writerow([total_supply])

        elif flag_ext_url:

            ext_url = result.fields["url"]
            print("External URL", ext_url)

            with open(csv_file, "w", newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow({"External URL"})
                csvwriter.writerow([ext_url])          


asyncio.run(main())
