#!/usr/bin/env python3
"""
python_script.py
    Example Python Script used as template

    Runs on Python 3.6
"""


import argparse


def main():
    """ main function """

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store_true', dest='test', required=True)
    args = parser.parse_args()

    if args.test:
        val = example_function()
        print(val)

    print('Python Script')


def example_function():
    """
        Example function
    """

    return "value"


if __name__ == "__main__":
    main()
