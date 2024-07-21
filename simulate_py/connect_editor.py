# -*- encoding=utf8 -*-
__author__ = "dotua"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

#if not cli_setup():
    #auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.device import UnityEditorWindow

# specify to work on UnityEditor in this way
dev = UnityEditorWindow()

# make sure your poco-sdk component listens on the following port.
# Default value will be 5001. Change to any other if you like.
# IP is not used for now
addr = ('127.0.0.1', 5001)

# Specify the device object to initialize unity Poco
poco = UnityPoco(addr, device=dev)

#ui = poco('Vietnam')
#ui.click()
poco('Lesson_4').drag_to(poco('Lesson_2'))