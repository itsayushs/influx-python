from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "FWqUMyYl8-3ukSf3h5frRuzqGIfqFhtIa_pLkEGdEXw6TozvBdWo_4wB2c93tcCCpoyAHyNgyYZzO2XDY1iuNQ=="
org = "ankit"
bucket = "radsen"

def ingest_data(name, loc, data):
    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

    data = name+",loc="+loc+" data="+data
    write_api.write(bucket, org, data)


# ingest_data('rad1','IN','0.4322232')