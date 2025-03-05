# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import base64

class Convert:

    @staticmethod
    def Get(list,encoded_l):
        for element in list:
            if element == "None":
                enco = "None"
            else:
                encoded = base64.b64encode(element)
                if b"PNG" in element:
                    enco = "data:image/png;base64, " + str(encoded).replace("b'","").strip("'")
                elif b"GIF87a" in element or b"GIF89a" in element:
                    enco = "data:image/gif;base64, " + str(encoded).replace("b'","").strip("'")
                else:
                    enco = "data:image/jpg;base64, " + str(encoded).replace("b'","").strip("'")
            encoded_l.append(enco)
