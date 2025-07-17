#!/usr/bin/env python3

import sys
from derinet import derinet_reader as derinet
from vallex import derivatives_finder

# Default values (optional)
params = {
    'suffix': '',
    'vallex_path': '',
    'compounding': '',
    'filter_suffixes': []          # ← default is now an empty list
}

# Parse command‑line arguments
for arg in sys.argv[1:]:
    if '=' in arg:
        key, value = arg.split('=', 1)

        if key == 'filter_suffixes':
            # Expect something like "[telny,iny]" (with or without spaces)
            value = value.strip()
            if value.startswith('[') and value.endswith(']'):
                value = value[1:-1]          # drop the [ and ]
            # Split on commas, strip whitespace, ignore empty pieces
            params[key] = [v.strip() for v in value.split(',') if v.strip()]
        else:
            params[key] = value


# Read DeriNet data
derinet.read("./data_sources/derinet-2-3.tsv")

# Use parsed parameters
derivatives_finder.find_derivatives(suffix=params['suffix'], vallex_path=params['vallex_path'],
                                    compounding=params['compounding'],filter_suffixes=params['filter_suffixes'])