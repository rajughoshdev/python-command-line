##How to run ops script
create a new python3 virtualenv
```
python3 -m venv .venv
```
activate it
```
source .venv/bin/activate
```
install the deps
```
pip install -r requirements.txt
```
run the script
```
python ops.py -h
```

Basic pattern to create python command line tools with docopt as example `hellp.py` :
```
"""HELLO CLI

Usage:
    hello.py
    hello.py <name>
    hello.py -h|--help
    hello.py -v|--version

Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -v --version  Show version.
"""

from docopt import docopt

def say_hello(name):
    return("Hello {}!".format(name))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')
    if arguments['<name>']:
        print(say_hello(arguments['<name>']))
    else:
        print(arguments)
```
