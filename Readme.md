# Project and Module Base

Good base practices for creating modules and setting up a project

# Structure of Modules
Modules should be in their own directories within the project. Each module should have an `__init__.py` file to load the module contents.

## __init__
```
from .fileName import *
from . import math 
```


## Logging
Logging is handled by a root logger and child loggers that are attached to the root logger.

Each module should configure it's own logger; each program should configure it's own logger and then manage
logging from child modules.

### Modules
These will become child loggers of the root logger from the main program
* Create modules in a sub directory
* Create a global logger for each module: `logger = logging.getLogger(__name__)`
    * Make logging calls as such: `logger.info('This is a message')`
        * This will ensure that any program that uses this module will receive the logging messages 
        from this logger

### Main Program
The main program will create the root logger and attach all modules as child loggers
* Configure the basic logger configuration at the global level:
```
logging.basicConfig(level=logging.INFO, 
               format='%(asctime)s %(name)s:%(funcName)s %(levelname)s:%(message)s',
               datefmt='%Y.%m.%d %H:%M.%S')
```
    * setting this at the global level makes it tidier when developing in Jupyter as it does not 
    attempt to reconfigure the basicConfig over and over (this **should** have no affect, but Jupyter does not
    always handle this well).
* Within the `main()` function, set the logging levels for the ROOT and LOCAL loggers:

```
    def main():
        # set a local logger for this program
        logger = logging.getLogger(__name__)

        # set the log level for the root logger - this will affect all of the other child loggers
        # that are pulled from other modules loaded through imports, but NOT the local logger
        logger.root.setLevel('WARNING')

        # set the log level for this particular logger
        logger.setLevel('DEBUG')
```

Example Output:
```
# this log line comes from the local logger and is affected by logger.setLevel()
2020.06.30 13:37.15 LOGGER:__main__ FUNC:main DEBUG:creating adder
# this log line comes from a loaded module and is affected by the root logger: logger.root.setLevel()
2020.06.30 13:37.15 LOGGER:root FUNC:vals WARNING:no values were set. Setting to default of []
# this comes from the local logger
2020.06.30 13:37.15 LOGGER:__main__ FUNC:main INFO:getting ready to set some numbers: [1, 345, 23, 3.4, 66, 1, -100]
```


```python
%alias md_convert /Users/aaronciuffo/bin/develtools/mdconvert Readme.ipynb
%md_convert
```

    [NbConvertApp] Converting notebook Readme.ipynb to markdown



```python

```
