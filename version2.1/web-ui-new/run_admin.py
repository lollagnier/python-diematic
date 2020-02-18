#!/usr/bin/python3

from gevent.pywsgi import WSGIServer
from admin_ui import app

if __name__ == "__main__":
#    http_server = WSGIServer(('', 5000), app)
#    http_server.serve_forever()
    app.run(port=5001, debug=app.config['DEBUG'])
