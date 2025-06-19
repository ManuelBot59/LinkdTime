# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0
# Fork by Manuel Travezaño — Improvement: Changed the default time zone (GMT+2:00) to automatically detect the system's local time zone.

from Core.Utils import Colors
from Core.Utils import Clear
import random

class GET_BANNER:

    @staticmethod
    def Banner(clear_mode):
        if clear_mode == 1:
            Clear.SCREEN.Clear()
            banner_list = ["Banners/Banner.txt","Banners/Banner2.txt"]
            choice = random.choice(banner_list)
            f = open(choice, "r", newline=None)
            for line in f:
                  print(Colors.Color.PURPLE + line.replace("\n", ""))
            f.close()
            print(Colors.Color.WHITE + "\nA Linkedin Activity date Finder  Coded by Lucksi")
            print(Colors.Color.PURPLE2 + "____________________________________________________")
            print(Colors.Color.PURPLE2 + "|" + Colors.Color.WHITE + " Instagram:lucks_022" +
                  Colors.Color.PURPLE2 + "                              |")
            print(Colors.Color.PURPLE2 + "|" + Colors.Color.WHITE + " Email:lukege287@gmail.com" +
                  Colors.Color.PURPLE2 + "                        |")
            print(Colors.Color.PURPLE2 + "|" + Colors.Color.WHITE + " GitHub:Lucksi" +
                  Colors.Color.PURPLE2 + "                                    |")
            print(Colors.Color.PURPLE2 + "|" + Colors.Color.WHITE + " Twitter:@Lucksi_22" +
                  Colors.Color.PURPLE2 + "                               |")
            print(Colors.Color.PURPLE2 + "|" + Colors.Color.WHITE +
                  " Linkedin:https://www.linkedin.com/in/lucksi" + Colors.Color.PURPLE2 + "      |")
            print(Colors.Color.PURPLE2 + "----------------------------------------------------")
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} to stop the program".format(Colors.Color.GREEN + "Exit" + Colors.Color.WHITE))
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} to clear the screen".format(Colors.Color.GREEN + "Clear" + Colors.Color.WHITE))
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} to create a timeline".format(Colors.Color.GREEN + "timeline" + Colors.Color.WHITE))
            """print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} for assign a default name for each timeline element".format(Colors.Color.GREEN + "--autoname" + Colors.Color.WHITE))
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} for assign a description for each timeline element".format(Colors.Color.GREEN + "--description" + Colors.Color.WHITE))"""
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} to see advanced options".format(Colors.Color.GREEN + "help" + Colors.Color.WHITE))
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Insert {} to convert the date in a specific timezone (Default is local time zone)".format(Colors.Color.GREEN + "--timezone" + Colors.Color.WHITE))