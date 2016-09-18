from flask import Flask, jsonify

from Probe import Probe
from RepeatedTimer import RepeatedTimer

app = Flask(__name__)

REFRESH_RATE = 1 # in minutes

probe_1 = Probe('lmao')
probe_2 = Probe('xd')

@app.route('/')
def get_data():
	return jsonify({'probes': probe_1})

def refresh_data():
	print "Hello"
	return

if __name__ == '__main__':
	rt = RepeatedTimer(REFRESH_RATE*60, refresh_data)
	app.run(host='0.0.0.0')