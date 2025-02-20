# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core import Start
from time import sleep
import datetime
import os

class CREATE:

    @staticmethod
    def Html_Timeline(name):
        name = name.replace(".txt",".html")
        content = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Timeline</title>
    <style>
      body{
        background-color:gray;
      }
      .timeline{
        position: absolute;
        justify-content: center;
        margin-top: 10px;
        display: inline-block;
      }
      .summary{
        display: block;
      }
      .summary p{
        text-align: center;
      }
      #line{
        display: inline-block;
        position: relative;
        color: black;
        border: 2px solid black;
        width: 90px;
        margin-bottom: 67px;
        margin-left: none;
        margin-right: -5px;
      }
      .element{
        margin-top: 10px;
        display: inline-block;
        min-width: 100px ;
        max-width: fit-content;
        height: fit-content;
        background-color: white;
        border: 3px solid black;
      }
      .element p{
        text-align: center;
      }
      .element a{
        text-align: center;
      }
      .title p{
        text-align: center;
        text-decoration: none;
        font-size: small;
        font-weight: bolder;
        color: red;
        font-family: 'Courier New', Courier, monospace;
      }
      .user p{
        text-decoration: none;
        font-size: small;
        font-family: 'Courier New', Courier, monospace;
      }
      .date p{ 
        text-decoration: none;
        font-size: small;
        font-family: 'Courier New', Courier, monospace;
      }
      .links p{ 
        text-decoration: none;
        font-size: small;
        font-family: 'Courier New', Courier, monospace;
      }
      .links a{
        text-decoration: none ;
        color: green;
        font-size: small;
        font-family: 'Courier New', Courier, monospace;
      } 
    </style>
  </head>
  <body>
    <center><h1>Linkedin Timeline</h1></center>
    <div class="timeline">
"""
        f = open(name,"w")
        f.write(content)
        f.close()
        return name

    @staticmethod
    def Create_Timeline(name):
        date = datetime.datetime.now()
        f = open(name,"w")
        f.write("----------------------------------------------\n")
        f.write("| Created with LinkdTime                     |\n")
        f.write("| Link: https://github.com/Lucksi/LinkdTime  |\n")
        f.write("| Date: {}           |\n".format(date))
        f.write("----------------------------------------------\n\n")
        f.close()

    @staticmethod
    def Write_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone,orig_conversion):
        j = 1
        f = open(timel_name,"a")
        f.write("Earliest Event: {} {} Latest Event: {} {}\n\n".format(str(fixed_earliest),timezone,str(fixed_latest),timezone))
        for element in ordinated:
            f.write("Number° {}\r\n".format(str(j)))
            orig_index = orig_conversion.index(element)
            f.write("Element Title: {}\r\n".format(titles[orig_index]))
            if users[orig_index] != "" and types[orig_index] != "Profile-Picture" and types[orig_index] != "Company-Logo" and types[orig_index] != "Profile-Background-Image":
                f.write("Author: {}\r\n".format(users[orig_index]))
            f.write("Type: {}\r\n".format(types[orig_index]))
            if types[orig_index] == "Profile-Picture" and types[orig_index] == "Company-Logo" and types[orig_index] == "Profile-Background-Image":
                f.write("Added on date: {} {}\r\n".format(conversion[orig_index],timezone))
            else:
                f.write("Posted on date: {} {}\r\n".format(conversion[orig_index],timezone))
            f.write("Url: {}\r\n\n".format(reader[orig_index].lstrip().rstrip()))
            j = j + 1
        f.close()
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Timeline Saved on: {}".format(Colors.Color.GREEN + str(timel_name)))
    
    @staticmethod
    def Write_Html_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone,orig_conversion):
        j = 1
        f = open(timel_name,"a")
        f.write("<div class = 'summary'><p>Earliest Event <font color = '#00ffff'>{} {}</font> Latest Event <font color = '#00ffff'>{} {}</font></p></div>".format(str(fixed_earliest),timezone,str(fixed_latest),timezone))
        for element in ordinated:
            f.write("<div class = 'element'>\r\n<div class = 'title'>")
            orig_index = orig_conversion.index(element)
            f.write("<p>Element Title: {}</p>\r\n</div><hr>\r\n<div class = 'user'>".format(titles[orig_index]))
            if users[orig_index] != "" and types[orig_index] != "Profile-Picture" and types[orig_index] != "Company-Logo" and types[orig_index] != "Profile-Background-Image":
                f.write("<p>Author: {}</p></div><hr>\r\n<div class = 'user'>".format(users[orig_index]))
            else:
                f.write("<p>Author: None</p></div><hr>\r\n<div class = 'user'>")
            f.write("<p>Type: {}</p></div><hr><div class = 'date'>\r\n".format(types[orig_index]))
            if types[orig_index] == "Profile-Picture" and types[orig_index] == "Company-Logo" and types[orig_index] == "Profile-Background-Image":
                f.write("<p>Added on date: {} {}</p>\r\n</div><hr><div class = 'links'>".format(conversion[orig_index],timezone))
            else:
                f.write("<p>Posted on date: {} {}</p>\r\n</div><hr><div class = 'links'>".format(conversion[orig_index],timezone))
            f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div><div id = 'line'></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
            j = j + 1
        f.write("</div></body></html>")
        f.close()
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Html-Timeline Saved on: {}".format(Colors.Color.GREEN + str(timel_name)))
    
    @staticmethod
    def Timeline(path,timel_name,auto,timezone):
        timel_name = "Timelines/{}".format(timel_name)
        html = CREATE.Html_Timeline(timel_name)
        CREATE.Create_Timeline(timel_name)
        users = []
        conversion = []
        orig_conversion = []
        ordinated = []
        types = []
        titles = []
        earliest = ""
        t_i = 1
        if os.path.isfile(path):
            f = open(path,"r",newline=None)
            reader = f.readlines()
            f.close()
            num = len(reader)
            for element in reader:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Url: {}".format(Colors.Color.GREEN + element.replace("\n","")))
                if auto == 0:
                    title = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline-Element title" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                    while title == "" or title == " ":
                        title = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline-Element title" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                else:
                    title = "Element n°{}".format(t_i)
                    t_i = t_i + 1
                titles.append(title)
                Start.MAIN.Scan(element,"True",users,conversion,types,timezone,orig_conversion)
                sleep(1)
            fixed_earliest = min(orig_conversion)
            fixed_latest = max(orig_conversion)
            earliest_l = orig_conversion.index(fixed_earliest)
            latest_l = orig_conversion.index(fixed_latest)
            fixed_earliest = conversion[earliest_l]
            fixed_latest = conversion[latest_l]
            temp = orig_conversion.copy()
            for i in range(num):
                earliest = min(temp)
                ordinated.append(earliest)
                temp.remove(earliest)
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Creating Timeline\n")
            sleep(2)
            print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Earliest Event: {} {}  Latest Event: {} {}\n".format(Colors.Color.GREEN + str(fixed_earliest), Colors.Color.WHITE + timezone + Colors.Color.WHITE,Colors.Color.GREEN + str(fixed_latest),Colors.Color.WHITE + timezone))
            j = 1
            for element in ordinated:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Number° {}".format(Colors.Color.GREEN + str(j)))
                orig_index = orig_conversion.index(element)
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE +  "Element Title: {}".format(Colors.Color.GREEN + titles[orig_index]))
                if users[orig_index] != "" and types[orig_index] != "Profile-Picture" and types[orig_index] != "Company-Logo" and types[orig_index] != "Profile-Background-Image":
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Author: {}".format(Colors.Color.GREEN + users[orig_index]))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE +  "Type: {}".format(Colors.Color.GREEN + types[orig_index]))
                if types[orig_index] == "Profile-Picture" and types[orig_index] == "Company-Logo" and types[orig_index] == "Profile-Background-Image":
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Added on date: {} {}".format(Colors.Color.GREEN + conversion[orig_index] + Colors.Color.WHITE,timezone))
                else:
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Posted on date: {} {}".format(Colors.Color.GREEN + conversion[orig_index] + Colors.Color.WHITE,timezone))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Url: {}\n".format(Colors.Color.GREEN + reader[orig_index].lstrip().rstrip()))
                j = j + 1
            CREATE.Write_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone,orig_conversion)
            CREATE.Write_Html_Timeline(users,conversion,ordinated,types,titles,reader,html,fixed_earliest,fixed_latest,timezone,orig_conversion)
        else:
            print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "File: {} not found".format(Colors.Color.GREEN + path + Colors.Color.WHITE)) 