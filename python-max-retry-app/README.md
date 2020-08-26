## Created project 
sls create --template aws-python

## Added max retry code in the serverless.yml file

 maximumEventAge: 720
 maximumRetryAttempts: 1
 
## Deploy applicaiton 

sls deploy -v 

## Verified the function in AWS Lambda functions console.
This function is verfied in console , it is working. 
    