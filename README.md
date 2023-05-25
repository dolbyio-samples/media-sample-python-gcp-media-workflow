[![License](https://img.shields.io/github/license/dolbyio-samples/blog-gcp-media-automations)](LICENSE)

![Blog Picture](https://dolby.io/wp-content/uploads/2021/11/Automating-Transcoding-Workflows-with-Google-Cloud-Functions-and-DolbyIO.jpg)

# Google Cloud Storage Auto Transcode with Dolby.io
This repository will follow [this blog](https://dolby.io/blog/automating-dolby-io-media-workflows-with-google-cloud-functions/) to automate media workflows using Google Cloud Functions.

# Overview
A sample application for [Google Cloud Functions](https://cloud.google.com/functions) to use Dolby.io's [Media APIs](https://docs.dolby.io/media-apis/docs) to automatically transcode any new files uploaded to a [Cloud Storage](https://cloud.google.com/storage) Bucket.

# Requirements
To begin, there should be a familiarity with web development and JavaScript. An active [Dolby.io account](https://dolby.io/) to access the Dolby.io Media Processing APIs as well as a [Google Cloud Platform (GCP)](https://cloud.google.com/) account and project with the appropriate permissions. 

# Getting Started
You will need to use your own Google Cloud project as the basis of this automation.

Ensure that in configuring the automation, the **Trigger type** is set to **Cloud Storage** and **Event type** is set to [Finalize/Create](https://cloud.google.com/functions/docs/calling/storage#finalize).

![](img/setup.png)

You will also want to ensure your `requirements.txt` contains the required packages.

![](img/requirements.png)

This application was made using the Python 3.9 runtime. All other versions have not been tested for compatibility.

![](img/runtime.png)

## File Structure

The code used for the Google Cloud Function lives in the `cloud-function` folder.

- `main.py`: The main file used to call the Dolby.io API
- `signedUrls.py`: A helper file containing code to create [Presigned URLs](https://cloud.google.com/storage/docs/access-control/signed-urls) to read and write the files from
- `requirements.txt`: The list of Python packages Cloud Functions needs to install for the run to be successful.

## Additional Notes

Upon execution, the function will log a job id that will contain the status. To see the job's status, use [the get status endpoint](https://docs.dolby.io/media-apis/reference/media-enhance-get).

Logic to ensure no post-processed files are ran through the pipeline is necessary to prevent infinite loops. Depending on your workflow, modify the logic to exit on a processed file, whether that be by file extension, name or other methods.

# Report a Bug 
In the case any bugs occur, report it using Github issues, and we will see to it. 

# Forking
We welcome your interest in trying to experiment with our repos.

# Feedback 
If there are any suggestions or if you would like to deliver any positive notes, feel free to open an issue and let us know!

# Learn More
For a deeper dive, we welcome you to review the following:
 - [Media API](https://docs.dolby.io/media-apis/docs)
 - [API Reference](https://docs.dolby.io/media-apis/reference/get-api-token)
 - [Getting Started with GCP](https://docs.dolby.io/media-apis/docs/gcp-cloud-storage)
 - [Transcoding Files Using Zapier, Google Drive, and Dolby.io](https://dolby.io/blog/transcoding-files-using-zapier-google-drive-and-dolby-io/)
 - [Visualizing Media Diagnose Workflows with Postman Flows](https://dolby.io/blog/visualizing-media-diagnose-workflows-with-postman-flows/)

# About Dolby.io
Using decades of Dolby's research in sight and sound technology, Dolby.io provides APIs to integrate real-time streaming, voice & video communications, and file-based media processing into your applications. [Sign up for a free account](https://dashboard.dolby.io/signup/) to get started building the next generation of immersive, interactive, and social apps.

<div align="center">
  <a href="https://dolby.io/" target="_blank"><img src="https://img.shields.io/badge/Dolby.io-0A0A0A?style=for-the-badge&logo=dolby&logoColor=white"/></a>
&nbsp; &nbsp; &nbsp;
  <a href="https://docs.dolby.io/" target="_blank"><img src="https://img.shields.io/badge/Dolby.io-Docs-0A0A0A?style=for-the-badge&logoColor=white"/></a>
&nbsp; &nbsp; &nbsp;
  <a href="https://dolby.io/blog/category/developer/" target="_blank"><img src="https://img.shields.io/badge/Dolby.io-Blog-0A0A0A?style=for-the-badge&logoColor=white"/></a>
</div>

<div align="center">
&nbsp; &nbsp; &nbsp;
  <a href="https://youtube.com/@dolbyio" target="_blank"><img src="https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube&logoColor=white" alt="Dolby.io on YouTube"/></a>
&nbsp; &nbsp; &nbsp; 
  <a href="https://twitter.com/dolbyio" target="_blank"><img src="https://img.shields.io/badge/Twitter-blue?style=flat-square&logo=twitter&logoColor=white" alt="Dolby.io on Twitter"/></a>
&nbsp; &nbsp; &nbsp;
  <a href="https://www.linkedin.com/company/dolbyio/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="Dolby.io on LinkedIn"/></a>
</div>
