# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import urllib
import urllib.request
import urllib.error
from configparser import ConfigParser

class GET:

    @staticmethod
    def Content(url,list,im_name,downl):
        error = "None"
        config_file = "Configuration/Configuration.ini"
        parser = ConfigParser()
        parser.read(config_file)
        useragent = parser["Settings"]["USER-AGENT"]
        auto_dwn = parser["Settings"]["AUTO-DOWNLOAD"]
        auto_dwn = str(auto_dwn)
        try:
            request = urllib.request.Request(url)
            request.add_header("User-Agent",useragent)
            content= urllib.request.urlopen(request).read()
            list.append(content)
            if auto_dwn == "True" or downl == 1:
                if b"PNG" in content:
                    extension = ".png"
                elif b"GIF87a" in content or b"GIF89a" in content:
                    extension = ".gif"
                else:
                    extension = ".jpg"
                im_name = im_name + extension
                save = open(im_name,"wb")
                save.write(content)
                save.close()
        except urllib.error.URLError as e:
            list.append("None")
            error = str(e)
        return error