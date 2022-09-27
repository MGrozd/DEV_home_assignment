import configparser

CONFIG_FILENAME = 'conf.ini'

def simple_strategy():
    pass

def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)


if __name__ == '__main__':
    main()
