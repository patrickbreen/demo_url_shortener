# do a build
docker-compose build
docker-compose up -d

# do python tests
python3.8 -m pytest .

docker-compose down