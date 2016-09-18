from flask import Flask, jsonify

from Probe import Probe
from RepeatedTimer import RepeatedTimer

app = Flask(__name__)

REFRESH_RATE = 1 # in minutes

DEVICE_ID_KEY = 'device_id'
HUMIDITY_KEY = 'humidity'
MOISTURE_KEY = 'moisture'
TEMP_KEY = 'temp'

probe_1 = Probe('lmao')
probe_2 = Probe('xd')

@app.route('/data')
def get_data():
	probes = list()
	probe_1_json = dict()
	probe_1_json[DEVICE_ID_KEY] = probe_1.device_id
	probe_1_json[HUMIDITY_KEY] = probe_1.humidity
	probe_1_json[MOISTURE_KEY] = probe_1.moisture
	probe_1_json[TEMP_KEY] = probe_1.temp

	probe_2_json = dict()
	probe_2_json[DEVICE_ID_KEY] = probe_2.device_id
	probe_2_json[HUMIDITY_KEY] = probe_2.humidity
	probe_2_json[MOISTURE_KEY] = probe_2.moisture
	probe_2_json[TEMP_KEY] = probe_2.temp

	probes.append(probe_1_json)
	probes.append(probe_2_json)

	return jsonify({'devices': probes})

def refresh_data():
	return

if __name__ == '__main__':
	rt = RepeatedTimer(REFRESH_RATE*60, refresh_data)
	app.run(host='0.0.0.0')