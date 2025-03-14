# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core import Start
from Core.Utils import Web_Request
from Core.Utils import Encoder
from time import sleep
import datetime
import os
import shutil

class CREATE:

    @staticmethod
    def Html_Timeline(name):
        name = name + ".html"
        date = datetime.datetime.now()
        content = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Timeline</title>
    <script>
      function Show_Bar(){
        document.getElementById("data5").style.display="Block";
        document.getElementById("button").setAttribute("onclick","javascript: Close_Bar()");
        document.getElementById("button").setAttribute("title","Click here to hide this text");
        document.getElementById("button").innerText="-";
        document.getElementById("meta").style.marginBottom="none";
        document.getElementById("meta").style.marginTop="10px";
        document.getElementById("meta").style.marginLeft="0%";
        document.getElementsByClassName("timeline")[0].style.marginTop="10px"
      }
      function Close_Bar(){
        document.getElementById("meta").style.display="inline-flex";
        document.getElementById("button").setAttribute("onclick","Show_Bar()")
        document.getElementById("button").innerText="+";
        document.getElementById("button").setAttribute("title","Click here to show the text");     
        document.getElementById("data5").style.display="None";
        document.getElementById("meta").style.marginLeft="40%";
        document.getElementsByClassName("timeline")[0].style.marginTop="50px"
      }
    </script>
    <style>
     body{
        background-color:gray;
      }
      #meta{
        margin-left: auto;
        margin-right: auto;
        display: inline-flex;
      }
      #meta button{
        position: absolute;
        width: 50px;
        height: 50px;
        font-size: larger;
        font-weight: bolder;
        color: white;
        border: 3px solid black;
        border-radius: 2px;
        background-color: green;
        margin-top: 5px;
        margin-left: none;
      }
      .desc1{
        width: 500px;
        margin-left: auto;
        margin-right: auto;
      }
      .desc{
        background-color: aliceblue;
        border: 3px solid black;
        width: 500px;
        margin-left: auto;
        margin-right: auto;
      }
      .desc p{
        text-align: center;
        color: black;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
      }
      .timeline{
        position: absolute;
        justify-content: center;
        margin-top: 10px;
        margin-left: 8px;
        display: inline-block;
      }
      .summary{
        display: block;
      }
      .summary p{
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        color: black;
      }
      #line{
        display: inline-block;
        position: relative;
        color: black;
        border: 2px solid black;
        width: 90px;
        margin-bottom: 67px;
        margin-left: none;
        margin-right: -26px;
      }
      .element{
        margin-top: 10px;
        margin-left: 20px;
        display: inline-block;
        min-width: 100px ;
        max-width: 344px;
        height: fit-content;
        background-color: white;
        border: 3px solid black;
        word-wrap: break-word;
        overflow: auto;
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
    <div class = "desc1">
      <div id = "meta">
        <button onclick="Close_Bar()" id = "button" title = "Click here to hide this text">-</button>
      </div>
      <div class = "desc" id = "data5">
        <p>Timeline created with LinkdTime</p>
        <p>Download Link https://github.com/Lucksi/LinkdTime</p>
      </div>
    </div>
    <div class="timeline">
"""
        f = open(name,"w")
        f.write(content)
        f.close()
        return name

    @staticmethod
    def Create_Timeline(name):
        name = name + ".txt"
        date = datetime.datetime.now()
        f = open(name,"w")
        f.write("----------------------------------------------\n")
        f.write("| Created with LinkdTime                     |\n")
        f.write("| Link: https://github.com/Lucksi/LinkdTime  |\n")
        f.write("| Date: {}           |\n".format(date))
        f.write("----------------------------------------------\n\n")
        f.close()
        return name

    @staticmethod
    def Write_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone,orig_conversion,descriptions):
        j = 1
        f = open(timel_name,"a")
        f.write("Earliest Event: {} {} Latest Event: {} {}\n\n".format(str(fixed_earliest),timezone,str(fixed_latest),timezone))
        for element in ordinated:
            f.write("Number° {}\r\n".format(str(j)))
            orig_index = orig_conversion.index(element)
            f.write("Element Title: {}\r\n".format(titles[orig_index]))
            if users[orig_index] != "" and types[orig_index] != "Profile-Picture" and types[orig_index] != "Company-Logo" and types[orig_index] != "Profile-Background-Image":
                f.write("Author: {}\r\n".format(users[orig_index]))
            if len(descriptions):
              f.write("Description: {}\r\n".format(descriptions[orig_index]))
            f.write("Type: {}\r\n".format(types[orig_index]))
            if types[orig_index] == "Profile-Picture" or types[orig_index] == "Company-Logo" or types[orig_index] == "Profile-Background-Image":
                f.write("Added on date: {} {}\r\n".format(conversion[orig_index],timezone))
            else:
                f.write("Posted on date: {} {}\r\n".format(conversion[orig_index],timezone))
            f.write("Url: {}\r\n\n".format(reader[orig_index].lstrip().rstrip()))
            j = j + 1
        f.close()
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Timeline Saved on: {}".format(Colors.Color.GREEN + str(timel_name)))
    
    @staticmethod
    def Write_Html_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone,orig_conversion,b_64,descriptions,images):
        j = 1
        b = 0
        f = open(timel_name,"a")
        f.write("<div class = 'summary'><p>Earliest Event <font color = '#00ffff'>{} {}</font> Latest Event <font color = '#00ffff'>{} {}</font></p></div>".format(str(fixed_earliest),timezone,str(fixed_latest),timezone))
        n_element = len(ordinated)
        for element in ordinated:
            f.write("<div class = 'element'>\r\n<div class = 'title'>")
            orig_index = orig_conversion.index(element)
            f.write("<p>Element Title: {}</p>\r\n</div><hr>\r\n<div class = 'user'>".format(titles[orig_index]))
            if users[orig_index] != "" and types[orig_index] != "Profile-Picture" and types[orig_index] != "Company-Logo" and types[orig_index] != "Profile-Background-Image":
              f.write("<p>Author: {}</p></div><hr>\r\n<div class = 'user'>".format(users[orig_index]))
            else:
              f.write("<p>Author: None</p></div><hr>\r\n<div class = 'user'>")
            if len(descriptions):
              f.write("<p>Description: {}</p></div><hr>\r\n<div class = 'user'>".format(descriptions[orig_index]))
            f.write("<p>Type: {}</p></div><hr><div class = 'date'>\r\n".format(types[orig_index]))
            if types[orig_index] == "Profile-Picture" and types[orig_index] == "Company-Logo" and types[orig_index] == "Profile-Background-Image":
              f.write("<p>Added on date: {} {}</p>\r\n</div><hr><div class = 'links'>".format(conversion[orig_index],timezone))
            else:
              f.write("<p>Posted on date: {} {}</p>\r\n</div><hr><div class = 'links'>".format(conversion[orig_index],timezone))
            if j<n_element:
              if len(b_64):
                if types[orig_index] == "Profile-Picture" or types[orig_index] == "Company-Logo" or types[orig_index] == "Profile-Background-Image" or types[orig_index] == "Image" or types[orig_index] == "Background-Image":
                  b_index = images.index(reader[orig_index])
                  if b_64[b_index] != "None":
                    f.write("<p>Url: <a href = '{}' target = 'blank'>Click_Here</a> Image_Base64: <a href = '{}' target = 'blank'>Click_Here</a></p>\r\n\n</div></div><div id = 'line'></div>\r\n".format(reader[orig_index].lstrip().rstrip(),b_64[b_index].lstrip().rstrip()))
                  else:
                    f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div><div id = 'line'></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
                  b = b + 1
                else:
                 f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div><div id = 'line'></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
              else:
                f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div><div id = 'line'></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
            else:
              if len(b_64):
                if types[orig_index] == "Profile-Picture" or types[orig_index] == "Company-Logo" or types[orig_index] == "Profile-Background-Image" or types[orig_index] == "Image" or types[orig_index] == "Background-Image":
                  b_index = images.index(reader[orig_index])
                  if b_64[b_index] != "None":
                    f.write("<p>Url: <a href = '{}'  target = 'blank'>Click_Here</a> Image_Base64: <a href = '{}' target = 'blank'>Click_Here</a></p>\r\n\n</div></div>\r\n".format(reader[orig_index].lstrip().rstrip(),b_64[b_index].lstrip().rstrip()))
                  else:
                    f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
                  b = b + 1
                else:
                    f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
              else:
                f.write("<p>Url: <a href = '{}'>Click_Here</a></p>\r\n\n</div></div>\r\n".format(reader[orig_index].lstrip().rstrip()))
            j = j + 1
        f.write("</div></body></html>")
        f.close()
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Html-Timeline Saved on: {}".format(Colors.Color.GREEN + str(timel_name)))
    
    @staticmethod
    def Timeline(path,timel_name2,auto,timezone,description,save,downl):
        fold_name = "Timelines/{}".format(timel_name2)
        if os.path.exists(fold_name):
          shutil.rmtree(fold_name)
          os.mkdir(fold_name)
        else:
         os.mkdir(fold_name)
        timel_name = "{}/{}".format(fold_name,timel_name2,timel_name2)
        html = CREATE.Html_Timeline(timel_name)
        txt = CREATE.Create_Timeline(timel_name)
        users = []
        conversion = []
        orig_conversion = []
        ordinated = []
        types = []
        titles = []
        links_l = []
        b_64 = []
        images = []
        descriptions_l = []
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
                if description == 1:
                  description_s = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline-Element description" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                  if description_s == "" or description_s == " ":
                    description_s = "None"
                  descriptions_l.append(description_s)
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
                if len(descriptions_l):
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Description: {}".format(Colors.Color.GREEN + descriptions_l[orig_index]))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE +  "Type: {}".format(Colors.Color.GREEN + types[orig_index]))
                if types[orig_index] == "Profile-Picture" or types[orig_index] == "Company-Logo" or types[orig_index] == "Profile-Background-Image":
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Added on date: {} {}".format(Colors.Color.GREEN + conversion[orig_index] + Colors.Color.WHITE,timezone))
                else:
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Posted on date: {} {}".format(Colors.Color.GREEN + conversion[orig_index] + Colors.Color.WHITE,timezone))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Url: {}\n".format(Colors.Color.GREEN + reader[orig_index].lstrip().rstrip()))
                if "/dms/image" in reader[orig_index]:
                    images.append(reader[orig_index])
                j = j + 1
            if save == 1:
              f = 0
              if len(images):
                image_fold = fold_name + "/Images"
                os.mkdir(image_fold)
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Getting and encoding images...")
                for element in images:
                  image_name = image_fold + "/{}".format(str(f))
                  error = Web_Request.GET.Content(element,links_l,image_name,downl)
                  if error == "None":
                    print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Image encoded: success")
                  else:
                    print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "Image encoded failed : {}".format(error))
                  f = f+1
                Encoder.Convert.Get(links_l,b_64)
                print()
              else:
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "No images found\n")
            CREATE.Write_Timeline(users,conversion,ordinated,types,titles,reader,txt,fixed_earliest,fixed_latest,timezone,orig_conversion,descriptions_l)
            CREATE.Write_Html_Timeline(users,conversion,ordinated,types,titles,reader,html,fixed_earliest,fixed_latest,timezone,orig_conversion,b_64,descriptions_l,images)
        else:
            print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "File: {} not found".format(Colors.Color.GREEN + path + Colors.Color.WHITE)) 