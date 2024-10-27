#!/bin/python3

"""
The core of the 10xTranslator
"""

from os import error
import sys
import random
import argparse

import logger as l

if __name__ == "__main__":
    # If you are using python linters, you'll probably get an error here. Simply ignore it.
    from utils import translate_once, LANGUAGE_CODES, print_loading_bar, load_file_contents
else:
    from .utils import translate_once, LANGUAGE_CODES, print_loading_bar, load_file_contents


QUIET_MODE = False


def main():
    """
    the main funcion
    gets the program arguments and initiates translation if successful
    """
    parser = argparse.ArgumentParser(description='The best translator currently available.')
    parser.add_argument('-q', '--quiet', action='store_true', help='Print only final translation or critical errors.')
    parser.add_argument('-v', '--verbosity', help='set logger verbosity')

    parser.add_argument('-i', '--iterations', nargs='?', help='Set the "accuracy" of the translation.')
    parser.add_argument('-e', '--errors_limit', nargs='?', help='Set the maximum number of errors before program gives up. Setting this to -1 removes limit.')
    parser.add_argument('lang', nargs='?', help='target language')
    parser.add_argument('file', nargs='?', help='File containing text to translate.')

    args = parser.parse_args()

    file = '/path/to/file.txt'
    text = 'sample_text'
    language = 'lang'
    iterations = 50
    max_errors = 10

    if args.quiet:
        l.toggle_logging(False)
        QUIET_MODE = True

    if args.verbosity:
        l.log_deb(f"Logger verbosity set to {args.verbosity}")
        l.set_verbosity(int(args.verbosity))

    if args.iterations:
        l.log_deb(f"Iteration count set to {args.iterations}.")
        iterations = args.iterations

    if args.errors_limit:
        l.log_deb(f"Error limit set to {args.errors_limit}.")
        max_errors = args.errors_limit

    if args.lang:
        l.log_deb(f"Target language set to '{args.lang}'.")
        language = args.lang
    else:
        l.log_err("No language specified. Aborting.", override_prior=True)
        sys.exit(1)

    if args.file:
        l.log_deb(f"File path set to '{args.file}'.")
        file = args.file
    else:
        l.log_err("No file specified. Aborting.", override_prior=True)
        sys.exit(1)

    text = load_file_contents(file)

    if not text:
        l.log_err("Failed to load file.", override_prior=True)
        sys.exit(1)

    translate(text, language, iterations=iterations, errors_limit=max_errors)

def translate(text, destination, iterations = 50, errors_limit=10):
    """
    * The method for text translating
    * text is the string to be translated
    * destination is the desired output language
    * iterations will basically increase the 'accuracy' of the translation,
    but will also make wait time longer. Values of 50-200 are in reasonable range,
    depending on your goal
    """
    l.log_deb("Starting translation...")
    dst = ""
    i = int(iterations)
    errors = int(errors_limit)
    while i > 0:
        if i == 1:
            dst = destination
        else:
            dst = random.choice(LANGUAGE_CODES)

        if not QUIET_MODE:
            print_loading_bar(i, int(iterations))

        try:
            text = translate_once(text, dst)
        except Exception as e:
            if errors_limit != -1:
                errors += 1
            l.log_err(f"\nFailed to translate due to an error: {e}")

            if errors < errors_limit:
                continue
            l.log_err("Too many errors occured, aborting.")
            return text

        i -= 1

    print(text)
    return text

if __name__ == '__main__':
    main()
