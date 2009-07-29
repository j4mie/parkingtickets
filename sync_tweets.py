import os
from optparse import OptionParser

usage = "usage: %prog -s SETTINGS | --settings=SETTINGS"
parser = OptionParser(usage)
parser.add_option('-s', '--settings', dest='settings', metavar='SETTINGS',
                  help="The Django settings module to use")
(options, args) = parser.parse_args()
if not options.settings:
    parser.error("You must specify a settings module")

os.environ['DJANGO_SETTINGS_MODULE'] = options.settings

from twitter_search_sync.sync import SearchSyncr

s = SearchSyncr('"parking+ticket"+-rt+-via&rpp=100')

created_count = s.syncSearch()

print "done, created:", created_count