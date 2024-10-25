"""
The core of the 10xTranslator
"""

import random

# I dont know what kind of linter it is but it claims its unable to import 'utils',
#even if the program runs correctly :P
from utils import translate_once, LANGUAGE_CODES, print_loading_bar

def main():
    """
    the main funcion
    """
    translate("You've reached the website for Arch Linux, a lightweight and flexible Linux® distribution that tries to Keep It Simple. Currently we have official packages optimized for the x86-64 architecture. We complement our official package sets with a community-operated package repository that grows in size and quality each and every day. Our strong community is diverse and helpful, and we pride ourselves on the range of skillsets and uses for Arch that stem from it. Please check out our forums and mailing lists to get your feet wet. Also glance through our wiki if you want to learn more about Arch.", "en")

def translate(text, destination, iterations = 200):
    """
    * The method for text translating
    * text is the string to be translated
    * destination is the desired output language
    * iterations will basically increase the accuracy of the translation,
    but will also make wait time longer. Values of 50-200 are in reasonable range,
    depending on your goal
    """
    # print(f"Translating text: {text}")
    dst = ""
    i = iterations
    while i > 0:
        if i == 1:
            dst = destination
        else:
            dst = random.choice(LANGUAGE_CODES)

        print_loading_bar(i, iterations)
        try:
            text = translate_once(text, dst)
        except Exception as e:
            print(f"Failed to translate due to an error: {e}")
            continue

        i -= 1

    print(text)

if __name__ == '__main__':
    main()
