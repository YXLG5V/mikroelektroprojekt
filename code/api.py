from flask import Flask, json
from flask_cors import CORS, cross_origin
import redis

db = redis.Redis("localhost")
DATA = [0, {"celsius": 0, "farenheit": 0, "status": "LOW/HIGH"}]
stream_name="mystream"

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

@api.route('/gettemp', methods=['GET'])
@cross_origin()
def get_temp():
  DATA = db.xrevrange(stream_name, "+", "-", count=10)
  senddata = []
  for x in reversed(DATA):
        x = json.dumps(x[1])
        x = json.loads(x)
        senddata.append(float(x["celsius"]))
  print(json.dumps(senddata))
  return json.dumps(senddata)

if __name__ == '__main__':
    api.run()
