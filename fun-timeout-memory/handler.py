import time

def hello(event, context):
    print("Checking time waiting the method for 4 seconds")
    time.sleep(4)
    return "hello world"