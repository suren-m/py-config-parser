# py-config-parser
* config_loader_app contains below modules
    * main.py - entry point and contains load_config function
    * config_validator - a simple validator to check to catch most obvious syntax errors in config
    * config_builder - constructs the Config object
        * config object has group object attributes
        * group object has section attributes
        * Both Config and Group are subclassed from `Dict` and implement __getattr__, __getitem__ and __setattr__ data model methods
    * config_parser - contains a generator that takes a list of raw config items and yields a tuple with group_name and a group dict
    * section_value_parser - contains a parser to convert the section value to respective type
    * config_rules - contains tokens and accepted values for config file
    * config_cache - a very primitive cache with a `decorator` as a proof of concept. LRU would be ideal for both group and section level queries
* Have also added comments and doc strings as applicable
* tests folder contains a set of tests addressing most common queries
* only uses standard library

#### Requirements

* python 3x (3.6 and above preferably)
* On Windows, ensure the project folder is added to PythonPath in case of module import exceptions from vs code

#### To run unit tests that test given specs against example file

* cd config_loader_app/tests
* python -m unittest

#### Test Results ( 9 out of 9 passing)

```
$ python -m unittest
loading config from D:\config-loader\config_loader_app\tests\config_file_example
using overrides ['staging']
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```
    

#### To pass in custom filepaths and overrides from python shell

* from config_loader_app import main
* config = main.load_config(file_path, overrides)

#### To run using example config file in tests folder

* cd config_loader_app
* python -m config_loader_app.config_loader_main

#### Possible Improvements / Next Steps

* Caching - A custom `LRU cache` can help boost retrieval time of sections without having to traverse Group object again
* File Read efficiency - Maybe using a generators-like approach can reduce memory footprint when reading large files
* It's possible to reduce number of operations in config_parser. Group objects can then either be lazily loaded or created directly without needing a nested dict.
* Unit tests for Validator and handle exceptions for cases such as config.unknownGroup.unkownSection
* `UserDict` or `MutableMapping` instead of subclassing from `Dict`
* Regex pattern matching for extracting data between tokens instead of string split() and partition()
