from Probe import Probe

probe1 = Probe('lol')

probes = list()
probe1_json = dict()
probe1_json['humidity'] = probe1.humidity
probes.append(probe1_json)
print probes