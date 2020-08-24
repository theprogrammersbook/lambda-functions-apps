# lambda-functions-apps
Examples of lambda functions

# Step 1 : Install NodeJS 

sudo apt-get install npm

# Step 2: Install Serverless 

 npm install  -g serverless

 # Step 3: Seup Serverless
  - Create User in AWS with lambda as services 
export AWS_ACCESS_KEY_ID=XXXX
export AWS_SECRET_ACCESS_KEY=yyyyy

Or

serverless config credentials --provider aws --key XXX --secret YYY --profile serverless-admin


default region : us-east-1


## To create Python AWS template 
sls create --template aws-python

## To create NodeJs AWS template 
sls create --template aws-nodejs

## To create JavaMaven AWS template 
sls create --template aws-java-maven

### To get Other AWS Templates 

 sls create --template
 
Serverless: Generating boilerplate...
 
  Serverless Error ---------------------------------------
 
  Template "true" is not supported. Supported templates are: 
                                               "aws-clojure-gradle", "aws-clojurescript-gradle", "aws-nodejs", "aws-nodejs-typescript", "aws-alexa-typescript", "aws-nodejs-ecma-script", "aws-python", "aws-python3"
                                               "aws-groovy-gradle", "aws-java-maven", "aws-java-gradle", "aws-kotlin-jvm-maven", "aws-kotlin-jvm-gradle", "aws-kotlin-jvm-gradle-kts", "aws-kotlin-nodejs-gradle", "aws-scala-sbt"
                                               "aws-csharp", "aws-fsharp", "aws-go", "aws-go-dep", "aws-go-mod", "aws-ruby", "aws-provided"
                                               "tencent-go", "tencent-nodejs", "tencent-python", "tencent-php"
                                               "azure-csharp", "azure-nodejs", "azure-nodejs-typescript", "azure-python"
                                               "cloudflare-workers", "cloudflare-workers-enterprise", "cloudflare-workers-rust"
                                               "fn-nodejs", "fn-go"
                                               "google-nodejs", "google-python", "google-go"
                                               "kubeless-python", "kubeless-nodejs"
                                               "knative-docker"
                                               "openwhisk-java-maven", "openwhisk-nodejs", "openwhisk-php", "openwhisk-python", "openwhisk-ruby", "openwhisk-swift"
                                               "spotinst-nodejs", "spotinst-python", "spotinst-ruby", "spotinst-java8"
                                               "twilio-nodejs"
                                               "aliyun-nodejs"
                                               "plugin"
                                               "hello-world".
 
  Get Support --------------------------------------------
     Docs:          docs.serverless.com
     Bugs:          github.com/serverless/serverless/issues
     Issues:        forum.serverless.com
 
  Your Environment Information ---------------------------





