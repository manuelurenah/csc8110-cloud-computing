import requests
import json
import time
from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.docker_monitor

def insert(document, collection_name):

    if collection_name == 'container_1':
        benchmarks = db.container_1
    elif collection_name == 'container_2':
        benchmarks = db.container_2
    else:
        print('Invalid collection name, it should be either container_1 or container_2')
        return

    if document:
        for item in document:
            benchmark_id = benchmarks.insert_one(item).inserted_id
            print('Inserted one benchmark')
    else:
        print('The provided document is empty')

def fetch_benchmarks(url):
    response = requests.get(url)

    if response.ok:
        json_data = json.loads(response.content)[0]
    else:
        response.raise_for_status()

    return json_data['stats']
