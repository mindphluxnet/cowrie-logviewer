# cowrie-logviewer

A simple log viewer for the cowrie honeypot.

This is my first python project so the code might or might not be terrible, but it works well 
enough for me. So far, the only working feature is the actual log viewer. Since logs are split
by day, you can select the log to view in the top right corner of the page.

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

# Setup

With the exception of the log file path, everything's preconfigured and ready to run.
Edit cowrie-logviewer.py and change the 'log_path' variable accordingly. If you cloned
to the cowrie parent directory, you can just leave the path.

If you don't want debug messages, please change the 'debug' variable to False.

You can run the integrated web server on any port you desire. It's preconfigured to run
on port 5000. You can also bind it to any IP address, just change the 'bind_host' variable.

# Usage

```
python3 cowrie-logviewer.py
```

Once it's running, open 

http://yourhostname:5000 

in the web browser of your choice.
