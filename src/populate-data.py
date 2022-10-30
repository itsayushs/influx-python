import random
from influxdb_client import InfluxDBClient, Point, WritePrecision
import time
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS

token = "FWqUMyYl8-3ukSf3h5frRuzqGIfqFhtIa_pLkEGdEXw6TozvBdWo_4wB2c93tcCCpoyAHyNgyYZzO2XDY1iuNQ=="
org = "ankit"
'''
List of buckets
aerosol
gamma
radiation
surface
swipe
'''

def ingest_data(bucket, point):
    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket, org, point)
    time.sleep(2)


def insert_gama_data(location):
    data = str(round(random.uniform(1,5), 3))
    point = Point("gama").tag("location", location).field("doseRate", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("gamma", point)

def insert_surface_data(location):
    data = str(round(random.uniform(1,5), 3))
    point = Point("surface").tag("location", location).field("doseRate", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("surface", point)

def insert_aerosol_data(location):
    data = str(round(random.uniform(1,5), 3))
    data2 = str(round(random.uniform(1,5), 3))
    point = Point("aerosol").tag("location", location).field("alpha", data).field("beta",data2).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("aerosol", point)

def insert_swipe_data(location):
    data = str(round(random.uniform(1,5), 3))
    data2 = str(round(random.uniform(1,5), 3))
    point = Point("swipe").tag("location", location).field("alpha", data).field("beta",data2).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("swipe", point)

def insert_radiation_data(location):
    data = str(round(random.uniform(1,5), 3))
    data2 = str(round(random.uniform(1,5), 3))
    point = Point("radiation").tag("location", location).field("value", data).time(datetime.utcnow(), WritePrecision.NS)
    ingest_data("radiation", point)

counter=0
location="entrance2"
while counter < 10:
    insert_gama_data(location)
    insert_surface_data(location)
    insert_aerosol_data(location)
    insert_swipe_data(location)
    insert_radiation_data(location)
    print("Datapoint: "+str(counter)+" added")
    counter += 1
