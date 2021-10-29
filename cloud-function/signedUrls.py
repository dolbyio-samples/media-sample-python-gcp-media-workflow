# pip install google-cloud-storage

import datetime
import os

from google.cloud import storage

def generate_download_signed_url_v4(bucket_name, blob_name):
    # If you don't have the authentication file set to an environment variable
    # See: https://cloud.google.com/docs/authentication/getting-started for more information
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<KEY_FILE>.json"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow GET requests using this URL.
        method="GET",
    )

    print("Generated GET signed URL:")
    print(url)
    print("You can use this URL with any user agent, for example:")
    print("curl '{}'".format(url))
    return url

def generate_upload_signed_url_v4(bucket_name, blob_name):
    # If you don't have the authentication file set to an environment variable
    # See: https://cloud.google.com/docs/authentication/getting-started for more information
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<KEY_FILE>.json"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow PUT requests using this URL.
        method="PUT",
        content_type="application/octet-stream",
    )

    print("Generated PUT signed URL:")
    print(url)
    print("You can use this URL with any user agent, for example:")
    print(
        "curl -X PUT -H 'Content-Type: application/octet-stream' "
        "--upload-file my-file '{}'".format(url)
    )
    return url
