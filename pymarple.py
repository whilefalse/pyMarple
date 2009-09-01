import urllib

url = "http://ernestmarples.com/"

class PostcodeNotFound(Exception):
    pass

def find(postcode):
    resource = "%s?%s" % (url, urllib.urlencode({'p':postcode,'f':'csv'}))
    
    try:
        resource = urllib.urlopen(resource)
    except IOError:
        raise PostcodeNotFound()    

    if resource.info()['Content-Type'] != "text/csv":
        raise PostcodeNotFound()

    return [float(x) for x in resource.read().split(',')[1:]]
    
