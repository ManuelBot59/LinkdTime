# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import urllib
import urllib.request
import urllib.error

class GET:

    @staticmethod
    def Content(url,list):
        try:
            open = urllib.request.urlopen(url).read()
            list.append(open)
        except urllib.error.URLError:
            pass