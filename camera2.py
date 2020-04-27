'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import time
import random

Builder.load_string('''
<CameraClick>:
    orientation: 'horizontal'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
        allow_stretch: True
''')

class CameraClick(BoxLayout):


    def __init__(self, **kwargs):
        super(CameraClick, self).__init__(**kwargs)





class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()