import json

with open("data/metro_data.json") as f:
    metro_data = json.load(f)

def get_fare(start, end):
    key1 = f"{start}-{end}"
    key2 = f"{end}-{start}"
    return metro_data["fares"].get(key1) or metro_data["fares"].get(key2)

def get_timing(start, end):
    key1 = f"{start}-{end}"
    key2 = f"{end}-{start}"
    return metro_data["timings"].get(key1) or metro_data["timings"].get(key2)

def station_exists(name):
    return name in metro_data["stations"]

def get_all_stations():
    return metro_data["stations"]
