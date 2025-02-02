import pathlib

import json

class MainSettings:

    def __init__(self, width, height, bg_color, frequency):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.frequency = frequency
