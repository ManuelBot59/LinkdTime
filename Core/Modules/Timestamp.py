import datetime
import re

class GET:

    @staticmethod
    def Timestamp(url):
        match = re.search(r'(\d{10})', url)
        if match:
            return int(match.group(1))
        else:
            return "None"
