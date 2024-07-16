# -*- encoding=utf8 -*-
__author__ = "Monkey"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/R9JRB0DTABT?cap_method=ADBCAP&touch_method=MAXTOUCH&",])

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
#poco("wooden tray").child("LettersContainer").child("i").click()
poco("wooden tray").child("LettersContainer").child("I").drag_to(poco("Wooden Table").child("LettersHolderContainer").child("I"))




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
