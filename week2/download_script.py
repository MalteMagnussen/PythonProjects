#   1. Write a program `download_script.py`, which downloads a set of files from the internet.
#      The files to download are given as arguments to your program on the command-line as illustrated in the following:

#   ```bash
#   $ python download_script.py http://www.gutenberg.org/files/2701/2701-0.txt http://www.gutenberg.org/cache/epub/27525/pg27525.txt
#   Downloading file to ./2701-0.txt
#   Downloading file to ./pg27525.txt
#   ```

#     Reuse your `webget` module from exercises in notebook: 02-0c Modules.

#   2. Modify the above program, so that it can download a list of files from stdin.
#      That is, so that you can reuse the output of one CLI command as input to your program.

#   ```bash
#   $ cat list_of_files.txt | python download_script.py
#   ```

import webget
import sys
from urllib.parse import urlparse
# import logging # We haven't learned this yet?
