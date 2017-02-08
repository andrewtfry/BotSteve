nick = 'GuestBot'
password = ''
host = 'Your.IRC.Server'
channels = ['#channel']
owner = 'Owner'
# googleapikey:  Google API key
googleapikey = 'google-API-key'
# googleapikey:  Google SEID
google_seid = 'google-SEID'

# These are people who will be able to use admin.py's functions...
admins = [owner, 'someoneyoutrust']
# But admin.py is disabled by default, as follows:
exclude = ['admin']

# If you want to enumerate a list of modules rather than disabling
# some, use "enable = ['example']", which takes precedent over exclude
# 
# enable = []

# Directories to load user modules from
# e.g. /path/to/my/modules
extra = []

# Services to load: maps channel names to white or black lists
external = { 
  '#liberal': ['!'], # allow all
  '#conservative': [], # allow none
  '*': ['!'] # default whitelist, allow all
}

# Configuration for the nicktracker module.
nicktracker = {
# The time for loaded data to expire, and we should reload it. In seconds.
    'expiry': 30*60,
}

# EOF

