Install Instructions
=========================

From this directory run:

	virtualenv .
	source bin/activate
	./bin/pip install -r requirements.txt

Run Tests
===============

You need to set three environmental variables:

* BCCVL_TEST_USERNAME - the username to use when logging into the bccvl (must have admin rights)
* BCCVL_TEST_PASSWORD - the password to use when logging into the bccvl
* BCCVL_TEST_URL - the base URL to the bccvl site to test
* BCCVL_TEST_VIRTUAL_DISPLAY - true to use a virtual display (xvfb) while executing tests, false otherwise.
* BCCVL_TEST_IMPLICIT_WAIT (optional) - The number of seconds to wait while selenium is looking for web elements

From this directory run:

    source bin/activate
	./bin/nosetests
