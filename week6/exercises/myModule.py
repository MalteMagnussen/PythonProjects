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
import concurrent
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
            if filename not in self._url_list:
                self._url_list.append(filename)

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

        # We can use a with statement to ensure threads are cleaned up promptly
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(url_list)) as executor:
            # Start the load operations and mark each future with its URL
            future_to_url = {executor.submit(
                download, url): url for url in url_list}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    # print(data)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                else:
                    print('%r page is %d bytes' % (url, len(data)))
