#: A simple log viewer for cowrie 
#: Copyright 2017 by Richard 'mindphluxnet' Kämmerer (richard@richardkaemmerer.de)

from flask import Flask, render_template, send_from_directory
import json
import ipapi
import sqlite3
import dateutil.parser
import pycountry
from path import Path

#: change stuff here
sqlite_file = 'ip2country.sqlite'
log_path = '../cowrie/log'
bind_host = '0.0.0.0'
bind_port = 5000
debug = True

#: don't change stuff beyond this line

version = '0.1'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#: setup sqlite db

try:
	c.execute('CREATE TABLE ip2country (ipaddress TEXT, countrycode TEXT)')
except sqlite3.OperationalError:
	pass
try:
	c.execute('CREATE INDEX ipindex ON ip2country(ipaddress)')
except sqlite3.OperationalError:
	pass

conn.commit()
conn.close()

#: flask routes

app = Flask(__name__, static_url_path = '')

@app.route('/images/<path:path>')
def send_image(path):
	return send_from_directory('images', path)

@app.route('/log/<string:logfile>')
def show_log( logfile ):
	return render_log(logfile)

@app.route('/')
def index():
	return render_log('cowrie.json')

@app.route('/stats')
def show_stats():
	
	conn = sqlite.connect(sqlite_file)
	c = conn.cursor()


	return render_template('stats.html', stats = stats)

def render_log(logfile):

	#: find all json log files

	files = []
	d = Path(log_path)
	for f in d.files('*.json*'):
		files.append(str(f.name))
	
	#: connect ip2country db

	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	#: parse json log
	data = []
	with open(log_path + '/' + logfile) as f:
		for line in f:
			j = json.loads(line)			
			
			#: check if IP address is already in database first

			c.execute("SELECT countrycode FROM ip2country WHERE ipaddress='" + str(j['src_ip']) + "'")
			ip_exists = c.fetchone()
			if ip_exists:	
				j['country'] = ip_exists[0]
			else:
				#: look up IP via ipapi
				j['country'] = ipapi.location(j['src_ip'], None, 'country')			
				#: add ip/country pair to db
				c.execute("INSERT OR IGNORE INTO ip2country(ipaddress, countrycode) VALUES ('" + str(j['src_ip']) + "', '" + j['country'] + "')")
				conn.commit()

			#: fix date/time to remove milliseconds and other junk
			j['datetime'] = str(dateutil.parser.parse(j['timestamp']))
			tmp = j['datetime'].split('.')
			j['datetime'] = tmp[0]

			#: convert country code to human readable
			country = pycountry.countries.get(alpha_2=j['country'])
			j['country_name'] = str(country.name)

			data.append(j)
	
	conn.close();					
	return render_template('index.html', json = data, files = files, logfile = logfile, version = version)

if __name__ == '__main__':
	app.run(debug = debug, host = bind_host, port = bind_port)
