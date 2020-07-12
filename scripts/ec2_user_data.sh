# This should be able to be copied into an EC2 debian buster machine to install and run the webserver
# TODO


# clone code from github
git clone http://github.com/patrickbreen/demo_url_shortener
cd demo_url_shortener

# install dependencies
./scripts/install.sh # docker, AWS

# test
./scripts/integration_tests

# run - change the docker configuration to run just the web server and use the non-local dynamoDB
./scripts/run_production.sh