import files
from music21 import *


def getStream(filename):
    return converter.parse(files.current_directory+'\sheet-music\\' + filename)


def getFlatStream(filename):
    s = converter.parse(files.current_directory+'\sheet-music\\' + filename)
    return s.flat