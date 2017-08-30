#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
#
# We want element request line
# We need to write them out to standard output

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, datetime, tz, method, page, http_version, status, content_size = data
        filename = page.split('/')[-1]
	print "{0}\t{1}".format(page, filename)
