# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET:

    @staticmethod
    def Format(string):
        user = ""
        f_string = string.split("_",1)[0]
        char_count = f_string.count("/")
        try:
            first = f_string.replace("/"," ",char_count-1)
            user = first.rsplit("/",1)[1].rstrip().lstrip()
            if "urn:li:" in user:
                user = ""
            else:
                user = user
        except Exception as e:
            pass
        return user