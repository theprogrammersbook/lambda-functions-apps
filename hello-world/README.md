### Deploy app
sls deploy -v 

### Check in AWS Console 
Got to AWS Console and check in the lambada functions Node: region is us-east-1

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



