bucketcors.py
============

This program creates a new S3 bucket for a domain (or updates an existing one) so 
it can act as a website and so that Fargo can write to it via CORS requests.  At 
present to use it you need to have already created an AWS account and to have
knowledge of your AWS access keys.

It is licensed via the GPL. It is also very very rough - consider it v0.001; if 
it breaks things you get to keep both pieces.

Installation
============

If not already present on your machine install python, pip and virtualenv.
Python can be downloaded from <http://python.org>.

Once python is installed:

    easy_install pip virtualenv

Change to the directory where you downloaded this software.

    virtualenv bucketcors 
    cd bucketcors 
    source ./bin/activate
    pip install -r requirements.txt

Running the software
====================

Create a file called .boto in your home directory with contents as below:


	[Credentials]
	aws_access_key_id = <your key here>
	aws_secret_access_key = <your secret key here>

Run it with python - from the console:
    
    python bucketcors.py

The script should list all of your existing buckets and give you the option to create a new 
one.  Enabling an existing bucket:

    python bucketcors.py
    [1]: owenmorris-git
    [2]: owenmorris.org.uk
    [3]: Create new bucket
    Enter number: 2
    CORS enabling bucket owenmorris.org.uk 
    Setting ACL on bucket owenmorris.org.uk
    Configuring bucket owenmorris.org.uk as website
    Uploading index file
    Launching site: http://owenmorris.org.uk.s3.amazonaws.com/index.html
    Done!

Creating a new bucket:

    python bucketcors.py
    [1]: owenmorris-git
    [2]: owenmorris.org.uk
    [3]: Create new bucket
    Enter number: 3
    Enter domain name: owenmorris.me.uk
    Creating bucket owenmorris.me.uk
    CORS enabling bucket owenmorris.me.uk 
    Setting ACL on bucket owenmorris.me.uk
    Configuring bucket owenmorris.me.uk as website
    Uploading index file
    Launching site: http://owenmorris.me.uk.s3.amazonaws.com/index.html
    Done!

The script will open a new web browser pointing to your new CORS enabled bucket.
