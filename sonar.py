from flask import Flask, jsonify, request
import settings, os, requests

app = Flask(__name__)


@app.route('/bus/<channel>', methods=['POST'])
def post_message(channel):
    if channel in settings.channels:
        # TODO: Sanitize input
        requests.post("http://conduit:5000/bus/%s" % channel, data=json.dumps(request.json))
    return jsonify({"message": "received", "status": "success"})

if __name__ == '__main__':
    print os.environ
    app.run(host='0.0.0.0')
