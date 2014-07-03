#!/bin/sh

###
# Builds and runs the BCCVL functional tests.
#
# The following environment variables must be exported:
#   BCCVL_TEST_URL - the base URL to the bccvl site to test
#   BCCVL_TEST_USERNAME - the username to use when logging into the bccvl (must have admin rights)
#   BCCVL_TEST_PASSWORD - the password to use when logging into the bccvl
#   BCCVL_TEST_IMPLICIT_WAIT (optional) - The number of seconds to wait while selenium is looking for web elements
###


# Setup virtual env
virtualenv .
source ./bin/activate

# Install dependencies
./bin/pip install -r requirements.txt

# Run tests
./bin/nosetests --with-xunit

# Return the exit status of the tests. Causes the Jenkins build to pass/fail accordingly
exit $?