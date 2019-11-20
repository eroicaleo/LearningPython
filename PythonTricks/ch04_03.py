#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

def handle_validation_error(err):
    if type(err) == NameTooShortError:
        print('Got an NameTooShortError:', err)

try:
    validate('joe')
except BaseValidationError as err:
    handle_validation_error(err)
