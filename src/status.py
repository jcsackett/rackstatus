# Copyright 2011 j.c.sackett
# Free to use, free to copy.
# No guarantees, you're on your own.

import urllib2

RACKSPACE = "http://status.apps.rackspace.com/"

def main():
    """Main application loop."""
    request = urllib2.Request(RACKSPACE)
    response = urllib2.urlopen(request)
    html = response.read()

    print html

if __name__ == '__main__':
    main()
