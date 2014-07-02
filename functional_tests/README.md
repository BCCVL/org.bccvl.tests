Install Instructions
=========================

From this directory run:

	virtualenv .
	source bin/activate
	./bin/pip install -r requirements.txt

Run Tests
===============

You need to set three environmental variables:
    - BCCVL_TEST_USERNAME
    - BCCVL_TEST_PASSWORD
    - BCCVL_TEST_URL

From this directory run:

    source bin/activate
	./bin/nosetests
