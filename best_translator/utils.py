"""
utils for 10xTranslator
"""

import sys
import os

from deep_translator import GoogleTranslator
import logger as l

LANGUAGE_CODES = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mni-Mtei', 'lus', 'mn', 'my', 'ne', 'no', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

def translate_once(text, dst, src='auto'):
    """
    translate text to desired language
    optionally specify the source language
    """
    translator = GoogleTranslator(source=src, target=dst)
    return translator.translate(text)

def print_loading_bar(iteration, iterations_total, length = 30, fill = '#'):
    """
    Method used to quickly create loading bars
    """
    percent =(int)(100 - (100 * (iteration / iterations_total)))
    filled_length = int(length * percent / 100)
    loading_bar = fill * filled_length + '-' * (length - filled_length)

    print(f'\r[{loading_bar}] ({percent}%)', end='')
    sys.stdout.flush()

def load_file_contents(file_path):
    """
    loads file based on specified path and returns its contents
    """
    expanded_path = os.path.expanduser(file_path)

    try:
        with open(expanded_path, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        l.log_err(f"The file at '{expanded_path}' does not exist.", override_prior=True)
    except IOError as e:
        l.log_err(f"An error occurred while reading the file: {e}", override_prior=True)
    return None
