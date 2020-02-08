import os
import urllib.request as req
from urllib.parse import urlparse
from PythonProjects.utils import checkFile


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
        fileName = to
        if (fileName != None):
            if(checkFile.checkFile(fileName)):
                return
            req.urlretrieve(url, fileName)
        else:
            fileName = os.path.basename(result.path)
            if(checkFile.checkFile(fileName)):
                return
            req.urlretrieve(url, fileName)
        print("Attempting to retrieve doc from: "+url)
    else:
      # IS NOT URL
        print("Wrong url format: " + url)
