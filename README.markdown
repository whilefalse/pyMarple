# pyMarple

This is a Python helper library for postcode lookup using the [Ernest Marple API](http://ernestmarples.com/).

## Usage

    import pymarple
 
    try:
        lat, lng = pymarple.find('b27 6eg')
    except pymarple.PostcodeNotFound:
        pass


## Tests

To run the tests, do...

    $ python tests.py