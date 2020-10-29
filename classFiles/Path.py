import urllib
from urllib.request import urlopen


class Path:
    """This class is responsible for reading the file from the given URL"""
    def __init__(self, path):
        self.path = path

    def readFile(self):
        try:
            page = urlopen(self.path)
            file_content = page.read().decode('utf-8')
            return file_content
        except urllib.error.URLError as e:
            print(e.reason)