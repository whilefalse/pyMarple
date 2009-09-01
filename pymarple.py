import urllib

url = "http://ernestmarples.com/"

def find(postcode):
    resource = "%s?%s" % (url, urllib.urlencode([('p',postcode), ('f','csv')]))
    resource = urllib.urlopen(resource)
    if resource.info()['Content-Type'] != "text/csv":
        raise Exception()

    p, lat, long = resource.read().split(',')
    return float(lat), float(long)
    
