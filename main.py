#!/usr/bin/env python3

import sys
from derinet import derinet_reader as derinet
from vallex import derivatives_finder

# Default values (optional)
params = {
    'suffix': '',
    'vallex_path': ''
}

# Parse command-line arguments
for arg in sys.argv[1:]:
    if '=' in arg:
        key, value = arg.split('=', 1)
        params[key] = value

# Read DeriNet data
derinet.read("./data_sources/derinet-2-3.tsv")

# Use parsed parameters
derivatives_finder.find_derivatives(suffix=params['suffix'], vallex_path=params['vallex_path'])