from bottle import route, run
import settings, os, requests

@route('/bus/<channel>', methods=['POST'])
def post_message(channel):
    if channel in settings.channels:
        # TODO: Sanitize input
        requests.post("http://conduit:5000/bus/%s" % channel, data=json.dumps(request.json))
    return jsonify({"message": "received", "status": "success"})

if __name__ == '__main__':
    run(host='0.0.0.0')
