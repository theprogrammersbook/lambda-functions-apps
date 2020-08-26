# Need to install docker.
### How to install docker
https://nagarajugajula.blogspot.com/2020/08/install-docker-on-ubuntu-using-default.html

### Get Python AWS Template 
sls create --template aws-python

# Sample ETL Data Job

This is a companion project for the post [ETL Job Processing with Serverless and AWS Redshift](https://serverless.com/blog/etl-job-processing-with-serverless-lambda-and-redshift/).

## Pre-requisites

Setting up AWS Redshift is out of scope of this sample, but we need one set up to dump data into it from our ETL job. Once you have it set up and configured, keep the cluster endpoint in Redshift handy, as we will need it later to configure the database connection string.

### Redshift cluster endpoint

`<cluster_name>.xxxxxxxxxxxx.<region>.redshift.amazonaws.com:<port>`

### DB Connection String

`postgres://<username>:<password>@<hostname>:<port>/<db_name>`
where `<hostname>:<port>` is the cluster endpoint

## Install dependencies

`$ pip install -r requirements.txt`



### Init the npm
npm init -y

### Add the serverless-python-requirements to npm
 npm i --save-dev serverless-python-requirements

### Check the code in handler.py and serverless.yml file 

### Docker require root permission.
If we get any errors related to docker permission.
then 
```sudo chmod 666 /var/run/docker.sock```

### Now deploy the app
sls deploy -v
## App is not running in AWS Lambda Console , Have some problems.
          
          