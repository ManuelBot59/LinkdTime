from configparser import ConfigParser

class GET:

    @staticmethod
    def Date_format():
        config_file = "Configuration/Configuration.ini"
        parser = ConfigParser()
        parser.read(config_file)
        format = parser["Settings"]["DATE-FORMAT"]
        if format == "Eu":
            dateformat = "%d/%m/%Y %H:%M:%S"
        elif format == "Us":
            dateformat = "%m/%d/%Y %H:%M:%S"
        elif format == "As":
            dateformat = "%Y/%m/%d %H:%M:%S"
        else:
            dateformat = "%d/%m/%Y %H:%M:%S"
        return dateformat