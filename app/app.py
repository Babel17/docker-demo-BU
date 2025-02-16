from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    redis_client.incr("visits")
    visits = redis_client.get("visits") or 0
    return jsonify({"message": "Hello! This is Dockerised Flask!", "visits": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)