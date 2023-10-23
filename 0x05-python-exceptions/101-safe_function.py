#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as errors:
        import sys
        print("Exception: {}".format(errors), file=sys.stderr)
        return None
