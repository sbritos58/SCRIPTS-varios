import time, urllib2
 
def gethtml(url):
    try:
        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()
    except Exception, e:
        time.sleep(2)
        return ''
        url = 'http://charly.geocom.com.uy/'
        print gethtml(url)