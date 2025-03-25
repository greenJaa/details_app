from src.details.app import app

HOST='0.0.0.0'
DEBUG=True
PORT=8000

app.run(host=HOST,port=PORT,debug=DEBUG)