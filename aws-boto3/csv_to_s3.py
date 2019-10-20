
''' 
Upload csv files in local directory to AWS S3 with boto3. 
'''

from pathlib import Path
import boto3
from os import rename


# The csv files in the local directory:
path = Path('~/MembraneTests/')


# Upload csv files to S3
s3 = boto3.client('s3')
bucket_name = 'bl-csv-01-2018'

for file in path.glob('*'):
    filenameins3 = str(file)
    content = open(file, 'rb')
    s3.put_object(
        Bucket=bucket_name,
        Key=filenameins3,
        Body=content
    )

print("Files uploaded to S3")
