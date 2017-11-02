import os
import platform
import pandas as pd  

from azure.storage.blob import BlockBlobService

block_blob_service = BlockBlobService(account_name='aacount', account_key='secretkeys')
block_blob_service.create_container('testcontainer')

message = "Using Python '{0}'".format(platform.python_version())  
print(message)

print("Hello World")
print("Added this line")

print('Pandas version ' + pd.__version__)