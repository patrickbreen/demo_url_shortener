import boto3
from flask import Flask,request,jsonify
from datetime import datetime
import simplejson as json

app = Flask(__name__)

@app.route('/', methods =['GET'])
def predict():
    try:        
        short_url = request.args.get('short_url')       
        
        try:
            dynamo = boto3.client('dynamodb')
            tables = str(dynamo.list_tables())
            #table = dynamo.Table('demo_url_shortener')
            return jsonify({
                    "info": "got tables",
                    "tables": tables})
        except Exception as exception:
            return jsonify({"error":str(exception),
                    "info": "Aws variables not set properly!!!",
                    })
        try:
            # fetching the items from the table with a certain id
            url_record = table.get_item(Key={ 'Customer_ID' : short_url })
        except:
            raise Exception("No such table")
    except Exception as exception:
        return jsonify({"error":str(exception)})
    else:
        output = json.dumps(url_record)
        return output

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)