import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """Download a remote file specified by a URL to a
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename
        to the file storing the contents of the remote file.
    """

    result = urlparse(url)

    if result.scheme and result.netloc and result.path:
        # IS URL
        if (to == None):
            fileName = os.path.basename(result.path)
            # Should perhaps contain a check for whether or not the file exists locally already.
            req.urlretrieve(url, fileName)
        elif (to):
            req.urlretrieve(url, to)
        print("Attempting to retrieve doc from: "+url)
    else:
      # IS NOT URL
        print("Wrong url format: " + url)
