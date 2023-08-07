# sopel-http
[![PyPi Version](https://img.shields.io/pypi/v/sopel-http.svg)](https://pypi.python.org/pypi/sopel-http)

Interact with your [Sopel](https://github.com/sopel-irc/sopel) bot over HTTP

## Setup
Only developers should need to install this package directly, but they can do
so with a simple `pip install sopel-http`.

## Configuration
You can change which IP addresses and ports `sopel-http` binds to in your Sopel
configuration. For example, to bind to port 80 on all IPs (including public!):
```ini
[http]
bind = "[::]:80"
```

## Usage
See the example plugin,
[sopel-http-example](https://github.com/half-duplex/sopel-http-example).

Once you've created and registered the flask
[Blueprint](https://flask.palletsprojects.com/en/2.1.x/blueprints/)
as shown in the example, you can use it more or less like any other flask
application.
