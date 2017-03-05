# cowrie-logviewer

A simple log viewer for the cowrie honeypot.

This is my first python project so the code might or might not be terrible, but it works well 
enough for me. Since logs are split by day, you can select the log to view in the top right corner
of the page. Some rudimentary statistics are available as well. Uploaded payloads can also be
viewed and downloaded via the "Uploaded files" page.

Attacker IPs are run against ipapi.co to find out which country they belong to. The results
are cached in a sqlite database. The first time you open a log file, this can cause some
delay if your internet connection is slow. Don't worry, it'll load much faster once the IPs
have been cached.

# Prerequisites

Since this is my first python project, I don't even know if this works with python2 as well.
I guess it does, but I wouldn't know anything about that. I used python3 so if you don't please
change the following commands accordingly.

Install python3 if you don't have it already:

```
sudo apt-get install python3
```
Then, install the required python modules:

```
sudo pip3 install flask
sudo pip3 install ipapi
sudo pip3 install pycountry
sudo pip3 install path.py
```

# Installation

```
git clone https://github.com/mindphluxnet/cowrie-logviewer
```

# Configuration

Edit cowrie-logviewer.py to configure the script. There are several variables at the top of
the file you can change:

- "log_path" - the path to the cowrie log directory
- "dl_path" - the path to the cowrie dl (downloads) directory
- "bind_host" - the IP address the web server should bind to, default 0.0.0.0
- "bind_port" - the port the web server should listen to, default 5000
- "min_upload_size" - min. file size in bytes to be to be listed on the "Uploaded files" page. Default is 1024
- "debug" - if you want debug messages, set this to True. Default "False"

# Usage

```
python3 cowrie-logviewer.py
```

Once it's running, open 

http://yourhostname:5000 

in the web browser of your choice.
