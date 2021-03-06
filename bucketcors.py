#!/usr/bin/env python
"""
    bucketcors.py
    Copyright (C) 2013  Owen Morris <owenmorris@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see [http://www.gnu.org/licenses/].
"""

import boto
import sys
import webbrowser

if __name__ == '__main__':

    s3 = boto.connect_s3()
    
    rs = s3.get_all_buckets()
    buckets = []
    for bucket in rs:
        buckets.append(bucket)

    for bucket in range(len(buckets)):
        print "[%d]: %s" % (bucket+1, buckets[bucket].name)
    print "[%d]: %s" % (len(buckets)+1, "Create new bucket")

    bucketchoice = raw_input("Enter number: ")
    bucketchoice = int(bucketchoice)

    if bucketchoice <= len(buckets):
        buckettoenable = buckets[bucketchoice-1]
    else:
        newname = raw_input("Enter domain name: ")
        print "Creating bucket %s" % (newname)
        try:
            buckettoenable = s3.create_bucket(newname)
        except boto.exception.S3CreateError:
            print "Could not create bucket %s" % (newname)
            sys.exit(1)

    print "CORS enabling bucket %s " % (buckettoenable.name)
    cors = boto.s3.cors.CORSConfiguration()
    cors.add_rule(['PUT', 'POST', 'DELETE'], "http://fargo.io", allowed_header='*', max_age_seconds=300)
    cors.add_rule('GET', '*')
    buckettoenable.set_cors(cors)
    
    print "Setting ACL on bucket %s" %(buckettoenable.name)
    buckettoenable.set_acl('public-read')

    print "Configuring bucket %s as website" % (buckettoenable.name)
    buckettoenable.configure_website(suffix='index.html')
     
    if not buckettoenable.get_key('index.html'):
    	print 'Uploading index file'
        index = boto.s3.key.Key(buckettoenable)
        index.key = 'index.html'
        index.set_contents_from_filename('index.html')
        index.set_acl('public-read')
    else:
	print 'Bucket already has index file, skipping upload'
        index = buckettoenable.get_key('index.html')
    
    indexurl = index.generate_url(expires_in=0, query_auth=False, force_http=True)
    print 'Launching site: %s' %(indexurl)
    webbrowser.open(indexurl, 1)
    print 'Done!'

