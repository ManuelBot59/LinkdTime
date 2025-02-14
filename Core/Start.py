# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core.Utils import Decimal
from Core.Modules import Binary
from Core.Modules import User
from Core.Modules import Timestamp
from Core.Modules import Timeline
from Core.Utils import Banner

class MAIN:

    @staticmethod
    def Scan(string,timeline,users,conversions,types):
        if string.startswith("https://www.linkedin.com") == False:
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Please insert a Linkedin link")
            MAIN.String(2)
        else:
            user = User.GET.Format(string)
            if "posts" in string:
                param = "Post"
                binary_string = Binary.GET.Format(string,"post")
            elif "comment" in string:
                if "reply" in string:
                    param = "Comment/Reply"
                else:
                    param = "Comment"
                binary_string = Binary.GET.Format(string,"comment")
            else:
                param = "Activity"
                binary_string = Binary.GET.Format(string,"other")
            try:
                formatted = Decimal.GET.Formatted(binary_string)
                converted = Timestamp.GET.Date(formatted)
                if timeline == "True":
                    users.append(user)
                    conversions.append(converted)
                    types.append(param)
                if user != "":
                    print(Colors.Color.PURPLE2 + "\n[v]" + Colors.Color.WHITE + "Linkedin {} Author: {} Posted on date: {} GMT+2".format(param,Colors.Color.GREEN + user + Colors.Color.WHITE,Colors.Color.GREEN + converted))
                else:
                    print(Colors.Color.PURPLE2 + "\n[v]" + Colors.Color.WHITE + "Linkedin {} Posted on date: {} GMT+2".format(param,Colors.Color.GREEN + converted))
            except Exception as e:
                print("\nSomething Went Wrong: " + str(e))
    
    @staticmethod
    def String(b_flag):
        Banner.GET_BANNER.Banner(b_flag)
        while True:
            try:
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Linkedin Activity Url" + "\n\n" + Colors.Color.PURPLE2 + "[-Link-]" + Colors.Color.WHITE + "-->"))
                if string == "clear" or string == "Clear" or string == "CLEAR":
                    Banner.GET_BANNER.Banner(1)
                else:
                    if "--autoname" in string or " --autoname" in string:
                        string = string.replace("--autoname"," --autoname")
                        auto = 1
                    else:
                        auto = 0
                    if "timeline" in string or " timeline" in string:
                        timel_name = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline name" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                        while timel_name == "" or timel_name == "":
                            timel_name = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline name" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                        string = string.replace(" timeline","timeline")
                        folder = string.split("timeline",1)[1].split(" ",1)[1].split(" ",1)[0]
                        timel_name = timel_name + ".txt"
                        Timeline.CREATE.Timeline(folder,timel_name,auto)
                    else:
                        MAIN.Scan(string,"None","","","")
            except Exception as e:
                print("\nSomething went wrong: {}".format(str(e)))