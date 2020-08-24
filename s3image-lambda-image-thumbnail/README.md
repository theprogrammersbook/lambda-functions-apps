# Need to install docker.
### How to install docker
https://nagarajugajula.blogspot.com/2020/08/install-docker-on-ubuntu-using-default.html

### Get Python AWS Template 
sls create --template aws-python

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
