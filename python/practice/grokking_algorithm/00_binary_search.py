#! /usr/bin/env python

import os
import logging

from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler

fmt = logging.Formatter(
    '%(levelname)s %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)
fmt_rich = logging.Formatter(datefmt='[%X]')

stderr = RichHandler(show_path=False)
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt_rich)

logfile = RotatingFileHandler(
    f'{os.path.basename(__file__).split(".")[0]}.log',
    maxBytes=5000,
    backupCount=5,
)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(fmt)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(stderr)
log.addHandler(logfile)


class BinarySearch:
    @staticmethod
    def search_iterative(sorted_list, item):
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(sorted_list) - 1
        log.info(f'{sorted_list=}')
        log.info(f'{item=}, {low=}, {high=}')

        # While you haven't narrowed it down to one element ...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            log.info(f'mid = (low + high) // 2: {mid=}')
            guess = sorted_list[mid]
            log.info(f'guess = sorted_list[mid] {guess=}')
            # Found the item.
            if guess == item:
                log.info(f'return {mid=}, {sorted_list[mid]=}')
                return mid
            # The guess was too high.
            if guess > item:
                high = mid - 1
                log.info(f'if guess {guess} > item {item}: {high=}')
            # The guess was too low.
            else:
                low = mid + 1
                log.info(f'else: {low=}')

        # Item doesn't exist
        return None

    def search_recursive(self, list, low, high, item):
        # Check base case
        if high >= low:
            mid = (high + low) // 2
            guess = list[mid]

            # If element is present at the middle itself
            if guess == item:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif guess > item:
                return self.search_recursive(list, low, mid - 1, item)

            # Else the element can only be present in right subarray
            else:
                return self.search_recursive(list, mid + 1, high, item)

        else:
            # Element is not present in the array
            return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative([i for i in range(1, 111, 4)], 93))  # => 1

    # 'None' means nil in Python.
    # We use to indicate that the item wasn't found.
    # print(bs.search_iterative(my_list, -1))  # => None
