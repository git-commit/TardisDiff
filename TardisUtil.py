import configparser
import os

class TardisOptions:

    """
    Class for handling options.
    Has a getter and setter for every property and saves changes automatically.

    Current keys are:
    - start_time
    """

    def __init__(self, optionFileName=".tardisrc"):
        self.config = TardisOptions.generateDefaultConfig()

        #Make path
        home_dir = os.path.expanduser("~")
        self._optionFilePath = os.path.join(home_dir, optionFileName)
        #Try to load config file
        filesLoaded = self.config.read(self._optionFilePath)
        if len(filesLoaded) == 0:  # No option file found
            self._saveOptionFile()
        self.options = self.config['TardisDiff']

    def isStartTimeAuto(self):
        return self._getOption('start_time') == 'auto'

    def getStartTime(self):
        return self._getOption('start_time')

    def setStartTime(self, start_time):
        self._setOption('start_time', start_time)

    def _setOption(self, option_name, option_value):
        self.options[option_name] = option_value
        self._saveOptionFile()

    def _getOption(self, option_name):
        return self.options[option_name]

    def _saveOptionFile(self):
        with open(self._optionFilePath, 'w') as configFile:
            self.config.write(configFile)

    @staticmethod
    def generateDefaultConfig():
        config = configparser.ConfigParser()
        config['TardisDiff'] = {'start_time': 'auto',

                                }
        return config