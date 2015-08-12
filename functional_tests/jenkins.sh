#!/bin/sh

###
# Builds and runs the BCCVL functional tests.
#
# The following environment variables must be exported:
#   BCCVL_TEST_URL - the base URL to the bccvl site to test
#   BCCVL_TEST_USERNAME - the username to use when logging into the bccvl (must have admin rights)
#   BCCVL_TEST_PASSWORD - the password to use when logging into the bccvl
#   BCCVL_TEST_VIRTUAL_DISPLAY - true to use a virtual display while executing tests, false otherwise.
#   BCCVL_TEST_IMPLICIT_WAIT (optional) - The number of seconds to wait while selenium is looking for web elements
###

# Setup virtual env
virtualenv .

# Install dependencies
./bin/pip install -r requirements.txt

# Run tests
#./bin/nosetests -v --nologcapture --with-xunit
xvfb-run --server-args="-screen 0 1280x800x8" ./bin/pybot robot

# Return the exit status of the tests. Causes the Jenkins build to pass/fail accordingly
exit $?
