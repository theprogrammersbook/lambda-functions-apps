#!/bin/bash


# Install serverless 
sudo npm install -g serverless

# Setup serverlesss

export AWS_ACCESS_KEY_ID=XXXX
export AWS_SECRET_ACCESS_KEY=yyyyy

or

serverless config credentials --provider aws --key XXX --secret YYY --profile serverless-admin