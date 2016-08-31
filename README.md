## Synopsis

These two simple scripts convert a Python2 shelve into a Python3 shelve. The objects in your shelve have to be jsonifyable

## Code Example

> python2 shelve_to_json.py python2shelve
takes your Python 2 shelve and crates python2shelve.json
> python3 json_tp_shelve.py python2shelve.json
takes your json and creates python2shelve.json.p3.shelve

## Motivation

Switched from Python version 2.7 to 3.4 during development and had to convert some shelves.

## License

license? haha, just use it, i wont guarantee anything ...