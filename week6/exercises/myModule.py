# Handin Exercise 6
# Create a module containing a class with the following methods:

# init(self, url_list)
# download(url,filename) raises NotFoundException when url returns 404
# multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
# iter() returns an iterator
# next() returns each of the downloaded files
# filelist_generator(url_list) returns a generator to loop through the filenames
# avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
import requests
#import NotFoundException
import threading
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import os
from urllib.parse import urlparse


class download():
    def __init__(self, url_list: list(string)):
        self._url_list = url_list

    def download(self, url, filename):
        # Raises NotFoundException when url returns 404

        class NotFoundException(Exception):
            pass

        if filename is None:
            result = urlparse(url)
            filename = os.path.basename(result.path)

        try:
            response = requests.get(url)

            status_code = response.status_code
            if status_code == 404:
                raise NotFoundException(response.raise_for_status())

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')
            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)

    def multi_download(self, url_list: list(string)):
        # multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
        self._url_list = url_list
        with ThreadPoolExecutor(len(url_list)) as executor:
            future = executor.map(download, url_list)
            print(future.result())
