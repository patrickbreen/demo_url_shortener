# URL Shortener


## The purpose of this project is to learn AWS, and provide a bit of self documentation (to myself) of a simple use case for the core AWS services.

Everything is incremental. As I learn more AWS, I can keep expanding this project slowly. This project can serve as reference for me ;).


## Major components: Python, Flask, Docker, Dynamo DB, AWS

## Important: make sure not to commit AWS credentials to this repositiory!!
## Important: all scripts and commands assume that the working directory is the root of this repository

`./script/<script>.sh`




## Documentation
TODO

very important AWS documentation to read  - https://docs.aws.amazon.com/index.html

## Test

Run integration tests locally (with docker). From root of repository: `./scripts/integration_tests.sh`


## Auto Format

`./scripts/auto_format.sh`

## Use Docker Locally

 - build - `docker-compose build`
 - run locally in development `./scripts/run_dev.sh`

## Deployment - EC2

 TODO
 - User data script just build and/or run docker container in EC2.
 - Make a cloudformation template that can launch the EC2 infrastructure

## Deplyment - ECS
 
 TODO: ECS or fargate deployment - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html

## Deployment - Elastic Beanstock 
 TODO (there is a flask example elastic beanstock deployment on AWS docs)



### I've given up on trying to do good git hygiene - branching and squashing. I may interactive rebase and squash from time to time if I get OCD, but this is a small hobby project for learning AWS  with one user and one developer. No reason to impose unessisary overhead that takes away fun.


Tasks:

 1. Finish getting Dev environment set up.
    - [1] cloud watch logging (going to use watchtower, even though I want to be learning boto3)
      - dynamically mount .aws config and creds in docker application in development
    - [*] refactor to use correct HTTP error codes

 2. Deploy to EC2
    - make run_production.sh, ec2_user_data.sh (just use docker to install and run within EC2)
    - make cloud formation provisioning
    - Put HTTPS on Application ELB
    - Deploy to EC2 VPC via CLI
    - Integrate CI/CD to auto deploy
    - Use SSM


 3. Deploy to Elastic Beanstock via CLI
    - [2] CLI deployment of docker application
    - [3] CI/CD
    - [4] HTTPS

 4. Deploy to ECS or Fargate with CLI, DNS, HTTPS,
    - [5] CLI deployment
    - [6] CI/CD
    - [7] DNS and HTTPS (this is the only one with DNS)


 
 - Virtual Private Cloud and Security stuff (document or describe this?? or cloud formation??)
 - Logging/Monitoring with cloud watch
 - Cloud Formation / AWS CLI scripts

 - github CI/DC integration. https://vocal.media/01/ci-cd-using-git-hub-actions






## Resources:

blog:
 - https://medium.com/@janhaviC/restapi-using-flask-and-aws-dynamodb-and-deploying-the-image-to-docker-hub-eff1305c15a

dynamodb:
 - https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=demo_url_shortener;tab=overview
 - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

url shortener:
 - https://www.youtube.com/watch?v=gq5yubc1u18
