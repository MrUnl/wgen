#! python

import os
import sys
import time
import string
import argparse
import itertools
import colors,alert
chars = string.ascii_letters + "1234567890"
def createWordList(chrs, min_length, max_length, output):
    """
    :param `chrs` is characters to iterate.
    :param `min_length` is minimum length of characters.
    :param `max_length` is maximum length of characters.
    :param `output` is output of wordlist file.
    """
    if min_length > max_length:
        alert.error_alert("Please `min_length` must smaller or same as with `max_length`",True)
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    alert.succes_alert("Creating wordlist at `%s`..." % output,True)
    alert.info_alert("Starting time: %s" % time.strftime("%H:%M:%S"),True)

    output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write(alert.succes_msg('saving character `%s`' % chars))
            sys.stdout.flush()
    output.close()
    alert.info_alert("End time: %s"% time.strftime('%H:%M:%S'),True,True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Wordlist Generator')
    parser.add_argument(
        '-c', '--chars',
        default=chars, help='characters to iterate')
    parser.add_argument(
        '-min', '--minimum', type=int,
        default=1, help='minimum length of characters')
    parser.add_argument(
        '-max', '--maximum', type=int,
        default=2, help='maximum length of characters')
    parser.add_argument(
        '-o', '--output',
        default='output/wordlist.txt', help='output of wordlist file.')

    args = parser.parse_args()
    createWordList(args.chars, args.minimum, args.maximum, args.output)
