# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET:

    @staticmethod
    def Formatted(string):
        string = str(string)
        sign_val = []
        dec = 0
        i = 0
        for i in range(41):
            sign_val.append(string[i])
        join_str = ''.join(sign_val)
        for element in join_str:
            dec = dec *2 + int(element)
        return dec