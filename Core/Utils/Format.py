# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from configparser import ConfigParser

class GET:

    @staticmethod
    def Hour_format():
        config_file = "Configuration/Configuration.ini"
        parser = ConfigParser()
        parser.read(config_file)
        format = parser["Settings"]["CLOCK-FORMAT"]
        if format == "24":
            hour_format = 1
        elif format == "12":
            hour_format = 2
        else:
            hour_format = 1
        return hour_format

    @staticmethod
    def Date_format():
        config_file = "Configuration/Configuration.ini"
        parser = ConfigParser()
        parser.read(config_file)
        format = parser["Settings"]["DATE-FORMAT"]
        if format == "Eu":
            dateformat = "%d-%m-%Y %H:%M:%S"
        elif format == "Us":
            dateformat = "%m-%d-%Y %H:%M:%S"
        elif format == "As":
            dateformat = "%Y-%m-%d %H:%M:%S"
        else:
            dateformat = "%d-%m-%Y %H:%M:%S"
        return dateformat