# -*- encoding=utf8 -*-
__author__ = "Monkey"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/SSIRZH6PKFIB89QK?touch_method=MAXTOUCH&",])

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
print("start...")
poco("wooden tray").child("LettersContainer").child("R")[1].drag_to(poco("Wooden Table").child("LettersHolderContainer").child("R")[1])
# script content
print("end...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)