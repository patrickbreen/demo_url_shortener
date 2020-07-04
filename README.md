# URL Shortener


## Python, Flask, Docker, Dynamo DB

## Resources:

blog:
 - https://medium.com/@janhaviC/restapi-using-flask-and-aws-dynamodb-and-deploying-the-image-to-docker-hub-eff1305c15a

dynamodb:
 - https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=demo_url_shortener;tab=overview
 - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

url shortener:
 - https://www.youtube.com/watch?v=gq5yubc1u18



## Deploy with Docker, Fargate, ECS, and EC2 with load balancer


## Current status:
Basically works how I want it to locally in development

## TODO:

### From now on, I'm going to try to make each of these tasks a branch and do good git hygeine (interactive rebase and squash) - just for more practice.

 - Finish getting working locally with docker and docker compose (because why not?)
 - Unit testing, integration testing with docker (will be integrated into CI)
 - CI/CD (also local dev build with code formater and tests.)
 - Deployment on ECS (with docker manually), ECS, and Fargate

 - DNS - Route 53
 - HTTPS
 - Virtual Private Cloud and Security
 - Logging
 - Monitoring
 - Cloud Formation




Everything is incremental. As I learn more AWS, I can keep expanding this project slowly. This project can serve as reference for me ;).