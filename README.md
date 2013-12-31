bucketcors.py
============

This program creates a new S3 bucket for a domain (or updates an existing one) so 
it can act as a website and so that Fargo can write to it via CORS requests.

It is licensed via the GPL. 

Installation
============

If not already present on your machine install python, pip and virtualenv.
Python can be downloaded from <http://python.org>.

Once python is installed:

    easy_install pip virtualenv

Change to the directory where you downloaded this software.

    virtualenv bucketcors 
    cd bucketcors 
    pip install requirements.txt

Running the software
====================

Create a file called .boto in your home directory with contents as below:


	[Credentials]
	aws_access_key_id = <your key here>
	aws_secret_access_key = <your secret key here>

Run it with python - from the console:
    
    python bucketcors.py

