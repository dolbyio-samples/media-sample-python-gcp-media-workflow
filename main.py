import os
import requests
# Import our helper functions to presign GCP urls
from signedUrls import *

url = "https://api.dolby.com/media/transcode"
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

# Define transcode parameters as documented:
# https://docs.dolby.io/media-apis/reference/media-transcode-post
body = {
    "inputs": [{ "source" : generate_download_signed_url_v4(bucketName, fileName) }],
    "outputs": [
        {
            "id" : "MP4-H.264",
            "destination" : generate_upload_signed_url_v4(bucketName, os.path.splitext(fileName)[0]+".mp4"),
            "kind" : "mp4",
            "audio" : {
                "codec" : "aac_lc",
                "bitrate_kb": 128
            }
        }
    ]
}

def hello_gcs(event, context):
    file = event
    # Set filename
    global fileName
    fileName = {file['name']}
    print(f"Processing file: {fileName}.")
    # Make Dolby.io API call
    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(response.text)
    print(response.json()["job_id"])
