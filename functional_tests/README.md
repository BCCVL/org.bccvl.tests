Install Instructions
=========================

From this directory run:

	virtualenv .
	./bin/pip install distribute --upgrade
	./bin/pip install -r requirements.txt

Run Tests
===============

You need to set three environmental variables:
    - BCCVL_TEST_USERNAME
    - BCCVL_TEST_PASSWORD
    - BCCVL_TEST_URL

From this directory run:

	./bin/python -m nose
