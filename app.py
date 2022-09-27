import configparser

CONFIG_FILENAME = 'conf.ini'


def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)


if __name__ == '__main__':
    main()
