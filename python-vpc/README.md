## Creating aws python app
sls create --template aws-python

## we have used vpc by creating security groups in AWS VPC and getting the subnets.

### Configuration is as follows

```
  vpc:
    securityGroupIds:
      - sg-031d82eb144ffbfd6
    subnetIds:
      - subnet-19822446
      - subnet-558a2a74

```
we can set this at global level and each function level.