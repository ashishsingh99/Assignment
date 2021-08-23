import os
import boto3
from botocore.exceptions import ClientError

access_key = 'your-access-key'
access_secret = 'Your-access-secret-key'
bucket_name = 'assignme'

s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret

)
filename = '/Users/ashish/Downloads/Data Files/myassignment.txt'
s3.upload_file(filename,bucket_name,filename)
