# sentiment-analysis-web-app
Using Amazon's SageMaker service to build, test, and deploy a sentiment inference web application.


## Memo
AWS Lambda test event 1 -  

**To insert...**
```
"body": "The movie was great! I love it so much..."
```

Response
```
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "text/plain",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "1"
}
```

Function Logs
```
START RequestId: 3c4f105d-41a9-43ce-822e-52a64f896fe6 Version: $LATEST
END RequestId: 3c4f105d-41a9-43ce-822e-52a64f896fe6
REPORT RequestId: 3c4f105d-41a9-43ce-822e-52a64f896fe6	Duration: 808.09 ms	Billed Duration: 809 ms	Memory Size: 128 MB	Max Memory Used: 73 MB
```
