### Functionality

I have created a python template aws lambda.

- Have modified the handler.js file to read list of lambda functions from AWS by using boot3 package.
- Deployed the app into AWS lambda 
- tested the app in AW Lambda console then  I got the following error.
 
 ```
"errorType": "ClientError",
  "errorMessage": "An error occurred (AccessDeniedException) " +
   "when calling the ListFunctions operation: User: arn:aws:sts::323728230337:assumed-role/python-iam-lambda-dev-us-east-1-lambdaRole/python-iam-lambda-dev-hello-iam-example is not authorized to perform: lambda:ListFunctions on resource: *" 
```

The above error is bacause we are trying to access lambda functions. 
So ,we need to add iam roles to the serverlessyml file

```
# you can add statements to the Lambda function's IAM Role here
  iamRoleStatements:
   - Effect: "Allow"
     Action:
       - "lambda:*"
     Resource: "*"

```
### After updating the above Iam details Now the applicaiton will run in the AWS Console.
### You can check these in IAM Roles selection by selecting the servicce name ,which is listed on the roles.
    - can verify the roles in its policy 