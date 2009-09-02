import urllib

url = "http://ernestmarples.com/"

class PostcodeNotFound(Exception):
    pass

def find(postcode):
    resource = "%s?%s" % (url, urllib.urlencode({'p':postcode,'f':'csv'}))
    
    try:
        #Get location
        resource = urllib.urlopen(resource)
        #Make sure it's in csv format. If it's not, we were redirected to home page
        assert resource.info()['Content-Type'] == "text/csv"
        #Split it on commas
        values = resource.read().split(',')
        #Make sure it's in the format postcode, lat, long
        assert len(values) == 3
        #Return the lat and long
        return [float(v) for v in values[1:]]
    except (IOError, AssertionError, ValueError):
        raise PostcodeNotFound()
    
