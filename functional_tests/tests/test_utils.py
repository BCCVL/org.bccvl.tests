import time

#
# Contains methods to help with testing
#


# Generates a unique timestamp of the format YYYYMMDDHHmmSS so we can name things uniquely
def generate_timestamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())