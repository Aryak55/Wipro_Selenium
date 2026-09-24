import configparser


class ConfigReader:

    @staticmethod
    def get_base_url():
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        return config["DEFAULT"]["base_url"]