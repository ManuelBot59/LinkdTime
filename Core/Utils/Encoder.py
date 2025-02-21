# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import base64

class Convert:

    @staticmethod
    def Get(list,encoded_l):
        for element in list:
            encoded = base64.b64encode(element)
            enco = "data:image/png;base64, " + str(encoded).replace("b'","").strip("'")
            encoded_l.append(enco)
