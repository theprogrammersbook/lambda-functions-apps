### Deploy app
sls deploy -v 

### Check in AWS Console 
Got to AWS Console and check in the lambada functions Node: region is us-east-1 (region is important)

### Running in Our Console
 - Here -f is function 
 - Here -l is the log file (showing in console)   
sls invoke -f hello -l
"hello - world"
--------------------------------------------------------------------
START RequestId: 08530049-287b-4b8a-a2a4-8ff0ff3573b3 Version: $LATEST
hi
END RequestId: 08530049-287b-4b8a-a2a4-8ff0ff3573b3
REPORT RequestId: 08530049-287b-4b8a-a2a4-8ff0ff3573b3  Duration: 0.31 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 35 MB  


## Update the function only and check the updated one..

### Step 1: update the function body  as 
```python

def hello(event, context):
    print("First Update")
    return "hello - world"

```
### Step 2: run  sls deploy -v 
### Step 3: run sls invoke -f hello -l  (we have already deployed so that now , invoking)
nagaraju@nagaraju:~/Technology/Repository/theprogrammersbook/lambda-functions-apps/hello-world$ sls invoke -f hello -l
"hello - world"
--------------------------------------------------------------------
START RequestId: 94123772-8271-4a7c-937f-daf8478cc35d Version: $LATEST
First Update
END RequestId: 94123772-8271-4a7c-937f-daf8478cc35d
REPORT RequestId: 94123772-8271-4a7c-937f-daf8478cc35d  Duration: 0.27 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 34 MB  Init Duration: 0.86 ms    



## Second Update
### Step 1: update the function body  as 
```python

def hello(event, context):
    print("Second Update")
    return "hello - world"

```
### Step 2: run :  sls deploy function -f hello  
Now ,sls will deploy only the funciton.
### Step 3: run : sls invoke -f hello -l 
## To remove the lamba funcitons
 (removes the function and logs from CloudWatch, removes all the functions)
sls remove 

@justin.m.chase suggested:

Simply remove the function in serverless.yml, then run full deploy

sls deploy
the function is removed (Lambda + API Gateway). Perfecto!

