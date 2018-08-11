# CachetHQ-monit-bridge

This is simple project made for purpose of status.fair.coop  
Its set of python scripts built while Summer Work Camp.

# Install

virtualenv venv
. venv/bin/activate
pip install -r requirements.txt

# Usage

python get-cachet-components.py && ./monit -c monitrc -I -l /dev/stdout
