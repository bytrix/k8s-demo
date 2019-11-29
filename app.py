from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello</h1><p>This is a test page demostrating for Kubernates.</p><p>{}</p>'.format(
		time.strftime('%Y-%m-%d %H:%M:%S')
	)

app.run(host='0.0.0.0')
