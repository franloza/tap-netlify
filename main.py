"""Main entrypoint of the application for debugging purposes"""

import sys
from tap_netlify.tap import TapNetlify

if __name__ == '__main__':
    TapNetlify.cli(sys.argv[1:])
