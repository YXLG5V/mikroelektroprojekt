from flask import Flask, json
import redis

db = redis.Redis("localhost")
DATA = [0, {"celsius": 0, "farenheit": 0, "status": "LOW/HIGH"}]
stream_name="mystream"

api = Flask(__name__)

@api.route('/gettemp', methods=['GET'])
def get_temp():
  DATA = db.xrevrange(stream_name, "+", "-", count=1)
  print(json.dumps(DATA[0][1]))
  return json.dumps(DATA[0][1])

if __name__ == '__main__':
    api.run()
