import boto3
from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
import hashlib




app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


# get the long URL for a provided short url
@app.route('/url-info/<short_url>', methods =['GET'])
def url_info(short_url):

    # get the database and the table, otherwise return 500 server error "could not connect to DB"
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('demo_url_shortener')

        response = table.get_item(Key={"short_url": short_url})
        
        # try to get the record, and return it as json, otherwise return 400 not found "the short URL wasn't found"
        if "Item" in response:
            return jsonify({"success": response["Item"]})
        else:
            return jsonify({"error": "provided short_url does not exist"})


    except Exception as e:
        return jsonify({"error":str(e)})


# try to get the record, and return it as json, otherwise return 400 not found "the short URL wasn't found"
@app.route('/url/<short_url>', methods =['GET'])
def redirect_to_long_url(short_url):
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('demo_url_shortener')
        response = table.get_item(Key={"short_url": short_url})

        if "Item" in response:
            return redirect(response["Item"]["long_url"])
        else:
            return jsonify({"error": "provided short_url does not exist"})


    except Exception as e:
        # actually want to return an error page
        return jsonify({"error": str(e)})


def hash_url(url):
    return hashlib.md5(url.encode()).hexdigest()[:10]

@app.route('/url', methods =['POST'])
def create():
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('demo_url_shortener')

        # create a short url for a long url and return it
        # test the post:
        # curl -H "Content-Type: application/json" -X POST -d "{\"url\":\"http://google.com\"}" http://localhost:4000/url

        url = request.json["url"]
        item = {
                "short_url": hash_url(url),
                "long_url": url,
            }
        response = table.put_item (
            Item = item
        )
        return jsonify({"success": "localhost:4000/url/" + str(item["short_url"])})



    except Exception as e:
        # actually want to return an error page
        return jsonify({"error": str(e)})



# TODO serve an index html that contains a form to create a shortened url
@app.route('/', methods =['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)