# Plexlogger
Track your tracks with Plexlogger.

Not sure what songs you recently played in Plex Media Player? Plexlogger will create a log file with the date & time of your music history.

## Installation

Clone this Repo somewhere

```bash
git clone https://github.com/aeth3real/Plexlogger.git
```

Enter your plex variables

```python

host = 'hostip'
port = '32400'
token = 'hosttoken'

```
Wonder how to find your token ? Go to Plex [Support](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)

Enter you log and XML buffer path

```python

logpath = "absolute/path/logplex.txt"
xmlpath = "absolute/path/xmlplex.xml"

```

Python Requests lib

```bash
pip3 install requests
```

Create the log file 

```bash
touch logplex.txt
```

## Run Plexlogger as a Systemd service

Create a service into /etc/systemd/system

```bash
cd /etc/systemd/system
```

Prepare the service

```bash
nano plexlogger.service
```

Copy this template and fill it with your path

```bash
[Unit]
Description=Music Log For Plex Media Player
After=multi-user.target

[Service]
WorkingDirectory=/your/path/to/working/directory
User=youruserid
Type=idle
ExecStart=/usr/bin/python3 /your/path/to/plexlogger.py
[Install]
WantedBy=multi-user.target
```
Then make it executable

```bash
sudo chmod 644 plexlogger.service
```
