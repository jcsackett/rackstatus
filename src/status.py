# Copyright 2011 j.c.sackett
# Free to use, free to copy.
# No guarantees, you're on your own.

import urllib2
import sys

from BeautifulSoup import BeautifulSoup


RACKSPACE = "http://status.apps.rackspace.com/"

def notify(groups):
    sys.exit(len(groups))

def main():
    request = urllib2.Request(RACKSPACE)
    response = urllib2.urlopen(request)

    html = response.read()

    soup = BeautifulSoup(html)

    groups = soup.findAll('div', 'row-group')
    groups = [g for g in groups if not g.find('img', 'status-1')]

    notify(groups)

if __name__ == '__main__':
    main()
