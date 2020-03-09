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
# import NotFoundException
import threading
import concurrent
import multiprocessing
import os
from urllib.parse import urlparse


class download():
    def __init__(self, url_list):
        self._url_list = url_list
        self.high = len(url_list)
        self.current = 0

    def singleDownload(self, url, filename=None):
        # Raises NotFoundException when url returns 404

        class NotFoundException(Exception):
            # How do you implement an exception? What is it supposed to do, and how do you make it do it?
            # print("NotFoundException: File wasn't found. ¯\_(ツ)_/¯")

            def __init__(self, *args, **kwargs):
                Exception.__init__(self, *args, **kwargs)

        if filename is None:
            #result = urlparse(url)
            filename = os.path.basename(urlparse(url).path)
            if url not in self._url_list:
                self._url_list.append(url)
                self.high += 1

        try:
            response = requests.get(url)

            status_code = response.status_code
            if status_code == 404:
                raise NotFoundException(response.raise_for_status())

            # If the response was successful, no Exception will be raised
            response.raise_for_status()

            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)

        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')

            # with open(filename, 'wb') as fd:
            #     for chunk in response.iter_content(chunk_size=1024):
            #         fd.write(chunk)

    def multi_download(self, url_list):
        # multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
        self._url_list = url_list
        self.high = len(url_list)

        # We can use a with statement to ensure threads are cleaned up promptly
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(url_list)) as executor:
            # Start the load operations and mark each future with its URL
            future_to_url = {executor.submit(
                self.singleDownload, url): url for url in url_list}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    future.result()
                    # print(data)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                else:
                    print(url)

    def getUrlList(self):
        return self._url_list

    def __iter__(self):
        # iter() returns an iterator
        return self

    def __next__(self):  # Python 2: def next(self)
        # next() returns each of the downloaded files
        self.current += 1
        if self.current < self.high:
            item = self.getUrlList()
            filename = os.path.basename(urlparse(item[self.current]).path)
            with open(filename, encoding="utf-8") as file:  #
                print("in __next__ with open("+filename+")")
                return (filename, file.read())
        raise StopIteration

    def filelist_generator(self, url_list):
        # filelist_generator(url_list)
        # returns a generator to loop through the filenames
        yield (url for url in self.getUrlList())

    def avg_vowels(self, text):
        # avg_vowels(text) - a rough estimate on readability
        # returns average number of vowels in the words of the text
        import re
        vowels = len(re.findall(r'[aeiouæøå]', text, flags=re.IGNORECASE))
        words = len(text.split())
        return words/vowels

    def hardest_read(self):

        # hardest_read() returns the filename of the text with the
        # highest vowel score
        # (use all the cpu cores on the computer for this work.)
        import multiprocessing
        with multiprocessing.Pool(len(self.getUrlList())) as pool:

            #iterable = iter(self.iter())

            data = ()
            for file in self.__iter__():
                filename = file[0]
                filetext = file[1]
                #print("In for file in self.__iter__(): "+filetext)
                data = (
                    *data, (filename, pool.apply(self.avg_vowels, args=[filetext])))

            # pool.join()

            highestRead = ""
            highestScore = 0

            for element in data:
                if element[1] > highestScore:
                    highestScore = element[1]
                    highestRead = element[0]

            return highestRead
