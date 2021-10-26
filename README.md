# Google Cloud Storage Auto Transcode with Dolby.io

A sample application for [Google Cloud Functions](https://cloud.google.com/functions) to use Dolby.io's [Transcode API](https://docs.dolby.io/media-apis/docs/transcoding-media) to automatically transcode any new files uploaded to a [Cloud Storage](https://cloud.google.com/storage) Bucket.

## Setup

You will need to use your own Google Cloud project as the basis of this automation.

Ensure that in configuring the automation, the **Trigger type** is set to **Cloud Storage** and **Event type** is set to [Finalize/Create](https://cloud.google.com/functions/docs/calling/storage#finalize).

![](img/setup.png)

This application was made using the Python 3.10 runtime. All other versions have not been tested for compatibility.

![](img/runtime.png)

## File Structure

- `main.py`: The main file used to call the Dolby.io API
- `signedUrls.py`: A helper file containing code to create [Presigned URLs](https://cloud.google.com/storage/docs/access-control/signed-urls) to read and write the files from
