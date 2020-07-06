# URL Shortener


## The purpose of this project is to learn AWS, and provide a bit of self documentation (to myself) of a simple use case for the core AWS services.

Everything is incremental. As I learn more AWS, I can keep expanding this project slowly. This project can serve as reference for me ;).


## Major components: Python, Flask, Docker, Dynamo DB, AWS

## Important: make sure not to commit AWS credentials to this repositiory!!




## Documentation
TODO

very important AWS documentation to read  - https://docs.aws.amazon.com/index.html

## Test

 - run unit tests locally TODO
 - run integration tests locally (with docker) TODO

## Docker

 - build - `docker build --tag=myapi .`
 - run locally - TODO
 - docker compose - because `docker compose up` is the best
 - ECS or fargate deployment - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html


 ## Elastic Beanstock Deployment
 TODO (there is a flask example elastic beanstock deployment on AWS docs)

 ## EC2 Deployment
 TODO

 - Make a cloudformation template that can launch the EC2 infrastructure





## Current status:
Basically works how I want it to locally in development from a UX perspective, and docker is basically there on a dev perspective, I need to finish tests, style checking, logging, and refactor.

Then add AWS deployments/services as I learn them.




### I've given up on trying to do good git hygiene - branching and squashing. I may interactive rebase and squash from time to time if I get OCD, but this is a small hobby project for learning AWS  with one user and one developer. No reason to impose unessisary overhead that takes away fun.


Tasks:

 1. Finish getting Dev environment set up: tests, code style formatting, logging, refactor, HTTP error messages/codes
 2. Deploy to Elastic Beanstock via CLI, with DNS and HTTPS
 3. Deploy to EC2 in VPC via CLI, with DNS and HTTPS
 4. Deploy to ECS or Fargate with CLI, DNS, HTTPS,
 5. Add cloudformation
 6. Add cloud watch
 7. Add CI/CD


 - CI/CD (also local dev build with code formater and tests.)
 - DNS - Route 53
 - HTTPS
 - Virtual Private Cloud and Security stuff (document or describe this?? or cloud formation??)
 - Logging
 - Monitoring
 - Cloud Formation / AWS CLI scripts









## Resources:

blog:
 - https://medium.com/@janhaviC/restapi-using-flask-and-aws-dynamodb-and-deploying-the-image-to-docker-hub-eff1305c15a

dynamodb:
 - https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=demo_url_shortener;tab=overview
 - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

url shortener:
 - https://www.youtube.com/watch?v=gq5yubc1u18
