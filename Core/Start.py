# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0
# Fork by Manuel Travezaño — Improvement: Changed the default time zone (GMT+2:00) to automatically detect the system's local time zone.

from Core.Utils import Colors
from Core.Utils import Decimal
from Core.Modules import Binary
from Core.Modules import User
from Core.Modules import Timestamp
from Core.Modules import Timeline
from Core.Utils import Banner

class MAIN:

    @staticmethod
    def Options():
        print(Colors.Color.PURPLE2 + "----------------------------------------------------------------------------------------")
        print(Colors.Color.PURPLE2 + "|" + Colors.Color.GREEN + "--autoname: " + Colors.Color.WHITE + "Assign a default name for each timeline element 'Timeline only'" + Colors.Color.PURPLE2 + "           |")
        print(Colors.Color.PURPLE2 + "|" + Colors.Color.GREEN + "--description: " + Colors.Color.WHITE + "Assign a description for each timeline element 'Timeline only'" + Colors.Color.PURPLE2 + "         |")
        print(Colors.Color.PURPLE2 + "|" + Colors.Color.GREEN + "--save: " + Colors.Color.WHITE + "Save images in base64 format 'Timeline only'" + Colors.Color.PURPLE2 + "                                  |")
        print(Colors.Color.PURPLE2 + "|" + Colors.Color.GREEN + "--download: " + Colors.Color.WHITE + "Download images 'Timeline only'" + Colors.Color.PURPLE2 + "                                           |")
        print(Colors.Color.PURPLE2 + "----------------------------------------------------------------------------------------")
    
    @staticmethod
    def Scan(string,timeline,users,conversions,types,timezone,t_conversions):
        if string.startswith("https://www.linkedin.com") == False and string.startswith("https://media.licdn.com") == False:
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Please insert a Linkedin link")
            MAIN.String(2)
        else:
            user = User.GET.Format(string)
            if "posts" in string:
                param = "Post"
                binary_string = Binary.GET.Format(string,"post")
            elif "commentUrn" in string:
                if "reply" in string:
                    param = "Comment/Reply"
                else:
                    param = "Comment"
                binary_string = Binary.GET.Format(string,"comment")
            elif "/dms/image" in string:
                if "profile-displayphoto" in string:
                    param = "Profile-Picture"
                elif "company-logo" in string:
                    param = "Company-Logo"
                elif "profile-displaybackgroundimage" in string:
                    param = "Background-Image"
                else:
                    param = "Image"
                user = ""
                formatted = Binary.GET.Format(string,"image")
            else:
                param = "Activity"
                binary_string = Binary.GET.Format(string,"other")
            try:
                if param != "Image" and param != "Profile-Picture" and param != "Company-Logo" and param != "Background-Image":
                    formatted = Decimal.GET.Formatted(binary_string)
                converted, t_converted, real_timezone = Timestamp.GET.Date(formatted, timezone)
                if timeline == "True":
                    users.append(user)
                    conversions.append(converted)
                    t_conversions.append(t_converted)
                    types.append(param)
                if user != "" and param != "Image" and param != "Profile-Picture" and param != "Company-Logo":
                    print(Colors.Color.PURPLE2 + "\n[v]" + Colors.Color.WHITE + "Linkedin {} Author: {} Posted on date: {} {}".format(param,Colors.Color.GREEN + user + Colors.Color.WHITE,Colors.Color.GREEN + converted + Colors.Color.WHITE, real_timezone))
                elif param == "Profile-Picture" or param == "Company-Logo" :
                    print(Colors.Color.PURPLE2 + "\n[v]" + Colors.Color.WHITE + "Linkedin {} Added on date: {} {}".format(param,Colors.Color.GREEN + converted + Colors.Color.WHITE, real_timezone))
                else:
                    print(Colors.Color.PURPLE2 + "\n[v]" + Colors.Color.WHITE + "Linkedin {} Posted on date: {} {}".format(param,Colors.Color.GREEN + converted + Colors.Color.WHITE, real_timezone))
            except Exception as e:
                print("\nSomething Went Wrong: " + str(e))
    
    @staticmethod
    def String(b_flag):
        Banner.GET_BANNER.Banner(b_flag)
        while True:
            try:
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Linkedin Activity Url" + "\n\n" + Colors.Color.PURPLE2 + "[-Link-]" + Colors.Color.WHITE + "-->"))
                if string.lower() == "clear":
                    Banner.GET_BANNER.Banner(1)
                elif string.lower() == "help":
                    MAIN.Options()
                elif string.lower() == "exit":
                    print("\nProgram stopped\n\n")
                    exit(0)
                else:
                    auto = "--autoname" in string
                    descr = "--description" in string
                    save = "--save" in string
                    downl = "--download" in string
                    timezone_n = "auto"
                    if "--timezone" in string:
                        try:
                            timezone_n = string.split("--timezone", 1)[1].split(" ", 1)[1].split(" ", 1)[0]
                            string = string.replace(" --timezone", "--timezone").replace("--timezone", "")
                            string = string.replace("{}".format(timezone_n), "")
                        except:
                            timezone_n = "auto"
                    if "timeline" in string:
                        timel_name = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline name" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                        while not timel_name.strip():
                            timel_name = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline name" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                        string = string.replace(" timeline","timeline")
                        folder = string.split("timeline",1)[1].split(" ",1)[1].split(" ",1)[0]
                        Timeline.CREATE.Timeline(folder,timel_name,auto,timezone_n,descr,save,downl)
                    else:
                        MAIN.Scan(string,"None","","","",timezone_n,"")
            except Exception as e:
               print("\nSomething went wrong: {}".format(str(e)))
