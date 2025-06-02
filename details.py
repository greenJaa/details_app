from src.details.app import app

HOST='127.0.1.1'
DEBUG=False
PORT=8080

app.run(host=HOST,port=PORT,debug=DEBUG)