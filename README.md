[![Build Status](https://travis-ci.org/mindphluxnet/cowrie-logviewer.svg?branch=master)](https://travis-ci.org/mindphluxnet/cowrie-logviewer)

# cowrie-logviewer

A simple log viewer for the cowrie honeypot.

Since the JSON logs are split by day, you can select the log to view in the top right corner
of the page. Some rudimentary statistics are available as well. Uploaded payloads can also be
viewed and downloaded via the "Uploaded files" page.

Attacker IPs are run against a local MaxMind GeoIP database to find out which country they belong to. The results
are cached in a sqlite database. 

# Installation

Assuming you installed cowrie into your home directory:

```
su cowrie
cd ~/../cowrie
git clone https://github.com/mindphluxnet/cowrie-logviewer
cd cowrie-logviewer
```

If you want, you can make the script executable:

```
chmod +x cowrie-logviewer.py
```

# Prerequisites

```
pip install -r requirements.txt
```

# MaxMind GeoLite 2 Country database setup

```
mkdir maxmind
cd maxmind
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
gunzip GeoLite2-City.mmdb.gz
rm GeoLite2-City.mmdb.gz
```

# Configuration

Edit cowrie-logviewer.py to configure the script. There are several variables at the top of
the file you can change:

- "log_path" - the path to the cowrie log directory
- "dl_path" - the path to the cowrie dl (downloads) directory
- "maxmind_path" - the path to the MaxMind GeoLite 2 Country database. Default is "maxmind/GeoLite2-Country.mmdb"
- "bind_host" - the IP address the web server should bind to, default 0.0.0.0
- "bind_port" - the port the web server should listen to, default 5000
- "min_upload_size" - min. file size in bytes to be to be listed on the "Uploaded files" page. Default is 1024
- "debug" - if you want debug messages, set this to True. Default "False"
- "use_gzip" - if you don't want gzip compression, set this to False. Default "True"
- "filter_events" - a list of log events to filter. Default "[ 'cowrie.direct-tcpip.request', 'cowrie.direct-tcpip.data' ]"

# Usage

```
python cowrie-logviewer.py
```

or (if you made the script executable)

```
./cowrie-logviewer.py
```

Once it's running, open 

http://yourhostname:yourport 

in the web browser of your choice. The default port is 5000.

# Event filtering

Some log events can be quite annoying since they provide very little insight into what's actually
happening but take up huge amounts of log lines. By default, cowrie-logviewer filters out
events related to tcp/ip forwarding. I implemented this after having some idiot attempt to
abuse my honeypot for some kind of tcp/ip forwarding exploit for about 24 hours straight. This
caused the logs to become almost unreadable. Filtering these events removes that annoyance.
Of course, the actual log files still contain these events so nothing is lost.

# Local network connections

Since local network IPs aren't in the MaxMind database for obvious reasons, there's no flag icon
attached to these connections. This isn't a bug, it's a feature.
