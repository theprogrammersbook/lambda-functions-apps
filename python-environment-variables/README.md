## Creating aws python app
sls create --template aws-python

## We have set environment variables
  -  Global environment variables
      environment:
        variable1: value1
        variable2: value1
        FIRST_NAME: "Nagaraju"
    
 
  - Local Einvironment variables
    environment:
      FIRST_NAME: "Mark"


## Now Deploy app 
sls deploy -v 

## Now run the app in AWS Console or in Our Console
sls invoke -f <functionName> -l (logging the output )