# Python script for Kinesis  Stream PutRecord API

import requests
import uuid
import random
import time
import json
import boto3


client = boto3.client(kinesis, region_name = '<INSERT THE REGION NAME>')

partition_key = str(uuid.uuid4())

while true:
    get_data = requests.get('https://randomuser.me/api/?exc=login')

    data = json.dumps(get_data.json())

    client.put_record(
            StreamName = '<INSERT THE STREAM NAME>',
            Data = data,
            PartitionKey = partition_key
    )

    time.sleep(random.uniform(0,1))
