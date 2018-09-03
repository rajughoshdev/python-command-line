"""
Command line python operation script.

Usage:
    ops.py list
    ops.py update <server>
    ops.py add  <server>
    ops.py remove <server>
"""
from docopt import docopt
import boto3

serverName = [ "server1", "server2", "server3" ]

if __name__ == "__main__":
#    print(docopt(__doc__, version='ops 1.0'))
    argument =  docopt(__doc__, version='ops 1.0')
    if argument['list']:
       for name in serverName:
           print(name)

    if argument['add']:
        serverName.append(argument['<server>'])
        print(serverName)

    if argument['remove']:
       try:
          serverName.remove(argument['<server>'])
          print(serverName)
       except ValueError:
         pass
