import os
import hashlib

import boto3
from flask import Flask, request, jsonify, redirect, render_template, send_from_directory


app = Flask(__name__, static_url_path='')


def get_dynDB_client():
    IS_LOCAL_DYNDB = os.getenv('IS_LOCAL_DYNDB')
    if IS_LOCAL_DYNDB:
        return boto3.client(
            'dynamodb',
            endpoint_url="http://dynamodb-local:8000",
            region_name="local")
    else:
        return boto3.client('dynamodb', region_name="us-east-1")


def get_dynDB_resource():
    IS_LOCAL_DYNDB = os.getenv('IS_LOCAL_DYNDB')
    if IS_LOCAL_DYNDB:
        return boto3.resource(
            'dynamodb',
            endpoint_url="http://dynamodb-local:8000",
            region_name="local")
    else:
        return boto3.resource('dynamodb', region_name="us-east-1")


# create table if not exists:
def create_url_shortener_table_if_not_exists():
    client = get_dynDB_client()
    try:
        response = client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'slug',
                    'AttributeType': 'S'
                },
            ],
            TableName='url_shortener',
            KeySchema=[
                {
                    'AttributeName': 'slug',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },
        )
    except client.exceptions.ResourceInUseException as e:
        pass


def delete_url_shortener_table():
    client = get_dynDB_client()
    client.delete_table(TableName="url_shortener")


# the 'hello' endpoint just shows that the webserver is working, and has
# no DynamoDB dependencies
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"success": "hello"})


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


# get the long URL for a provided short url
@app.route('/info/url/<slug>', methods=['GET'])
def url_info(slug):

    # get the database and the table, otherwise return 500 server error "could
    # not connect to DB"
    try:
        dynamo = get_dynDB_resource()
        table = dynamo.Table('url_shortener')

        response = table.get_item(Key={"slug": slug})

        # try to get the record, and return it as json, otherwise return 400
        # not found "the short URL wasn't found"
        if "Item" in response:
            return jsonify({"success": response["Item"]})
        else:
            return jsonify({"error": "provided slug does not exist"})

    except Exception as e:
        return jsonify({"error": str(e)})


# try to get the record, and return it as json, otherwise return 400 not
# found "the short URL wasn't found"
@app.route('/url/<slug>', methods=['GET'])
def redirect_to_long_url(slug):
    try:
        dynamo = get_dynDB_resource()
        table = dynamo.Table('url_shortener')
        response = table.get_item(Key={"slug": slug})

        if "Item" in response:
            return redirect(response["Item"]["long_url"])
        else:
            return jsonify({"error": "provided slug does not exist"})

    except Exception as e:
        # actually want to return an error page
        return jsonify({"error": str(e)})


def hash_url(url):
    return hashlib.md5(url.encode()).hexdigest()[:10]


@app.route('/url', methods=['POST'])
def create():
    try:
        print("begin")
        create_url_shortener_table_if_not_exists()

        dynamo = get_dynDB_resource()
        table = dynamo.Table('url_shortener')
        print("setup complete")

        # create a short url for a long url and return it
        # test the post:
        # curl -H "Content-Type: application/json" -X POST -d
        # "{\"url\":\"http://google.com\"}" http://localhost:4000/url

        url = request.json["url"]

        if not url.startswith("http://"):
            url = "http://" + url

        item = {
            "slug": hash_url(url),
            "long_url": url,
        }
        response = table.put_item(
            Item=item
        )
        return jsonify({"success": "/url/" + str(item["slug"])})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})

    except Exception as e:
        # actually want to return an error page
        return jsonify({"error": str(e)})


# serve an index html that contains a form to create a shortened url
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':

    # You probably don't ever want to run this directly in development (depending on what you want to do)
    # Use docker-compose up

    # for testing and development
    if os.getenv('IS_LOCAL_DYNDB') is None:
        os.environ['IS_LOCAL_DYNDB'] = '1'
    app.run(host='0.0.0.0', port=4000)
