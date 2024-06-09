# -*- encoding=utf8 -*-
__author__ = "dotua"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from jinja2.compiler import generate

from utility import LogicHandle

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["android://127.0.0.1:5037/SSIRZH6PKFIB89QK?touch_method=MAXTOUCH&",], project_root="D:/tool_test_game/simulate_py")


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
#swipe([1000,400],[400,400])
print("start...")
name = "CanvasPlayGame/wooden tray/LettersContainer/H"
a = LogicHandle.get_element(name)
 

a[0].drag_to(poco("Wooden Table").child("LettersHolderContainer").child('H')[0])
print("end...")

