import os
import requests
# Import our helper functions to presign GCP urls
from signedUrls import *

url = "https://api.dolby.com/media/enhance"
headers = {
    # Set your Dolby.io Media API key here
    "x-api-key": "<API_KEY>",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
# Input your GCP bucket name here
bucketName = "<GCP_BUCKET_NAME>"
# This will be automated with the Cloud Function
fileName  = ""

body = {
  "input" : generate_download_signed_url_v4(bucketName, fileName),
  # Specifically renaming the file to know that it is processed
  "output" : generate_upload_signed_url_v4(bucketName, "dolbyio-"+fileName)
}

def hello_gcs(event, context):
    file = event
    # Set filename
    global fileName
    fileName = {file['name']}
    # Exit function if dealing with post-processed file
    if fileName.startswith("dolbyio-"):
        return
    print(f"Processing file: {fileName}.")
    # Make Dolby.io API call
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    # This will log the job_id to the Cloud Function logs.
    print(response.json())
