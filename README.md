# Hao-Ji-You, for a life time.

A voice recognition system prototype for voice based programming.

It utilizes Google Speech Recognition API on Chrome as a frontend for speech
recognition. A Javascript programming running on Chrome initializes the speech
recognition engine, and then whatever recognized to a remote server over web
socket API.

A python backend application is included in this package as well, which
currently only echo what ever received.

## Usage
1. start backend server
```bash
$ cd desktop-backend
$ python haojiyou.py
```

2. start frontend, note that directly open the html file in the browser would
not have access to the microphone. A workaround is to use a simple http server
like python SimpleHttpServer.
```bash
$ cd browser-frontend
$ python -m SimpleHTTPServer
```

3. In Chrome, open http://localhost:8000/
