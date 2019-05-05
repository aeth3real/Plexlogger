#!/usr/bin/python3
#Plex logger V 0.01b by aeth3real
#Updated on 2019 - 05 - 05
#Please create an empty log file in destination directory

import xml.etree.ElementTree as xml
import requests
import time
import datetime

host = 'hostip'
port = '32400'
token = 'hosttoken'
plexurl = 'http://{0}:{1}/status/sessions?X-Plex-Token={2}'.format(host,port,token)
logpath = "absolute/path"
xmlpath = "absolute/path"
debugMode = False

def getnow():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def loadplex(plexurl):

    response = requests.get(plexurl)
    xml = response.content
    xmlfile = open(xmlpath, 'wb')
    xmlfile.write(xml)
    xmlfile.close()
    return xml

def xmlbuffer(plexurl):

    response = requests.get(plexurl)
    xmlb = response.content
    return xmlb

def parseXML():
    xmlfile = open(xmlpath, 'r')
    tree = xml.parse(xmlfile)
    root = tree.getroot()

    for track in root.findall('Track'):
        title = track.get('grandparentTitle')
        song = track.get('title')
        album = track.get('parentTitle')
    for media in root.iter('Media'):
        codec = media.get('audioCodec')
        bitrate = media.get('bitrate')
    try:
        inplay = 'Artist : "{1}" Track : "{0}" Album : "{2}" Codec : {3} {4} kbps'.format(song,title,album,codec,bitrate)
    except UnboundLocalError:
        inplay = ''
        pass
    return inplay

    xmlfile.close()

def logentry(inplay):
    if not inplay:
        pass
    else:
        started = getnow()
        log = open(logpath, 'a')
        newentry = started + " " + inplay + "\n"
        log.write(str(newentry))
        log.close()

def main():

    #Init Main Loop
    lastplay = ""
    lastxml = ""
    mainService = True
    loadplex(plexurl)
    currentxml = loadplex(plexurl)
    inplay = parseXML()
    lastplay = inplay
    logentry(str(inplay))

    #Entering Main Loop
    while mainService == True:
        lastxml = xmlbuffer(plexurl)
        inplay = parseXML()
        time.sleep(1)
        #Check the Buffer Before Rewrite
        if lastxml[72:110] != currentxml[72:110]:
            if debugMode:
                print("XML not Equal : Rewriting... ")
            loadplex(plexurl)
            currentxml = loadplex(plexurl)
            lastxml = currentxml
            if debugMode:
                print(currentxml[72:110])
                print(lastxml[72:110])
            pass
        #Check if Track Change and Write
        if inplay != lastplay:
            lastplay = inplay
            logentry(str(inplay))
            pass


if __name__ == "__main__":

    # calling main function
    main()
