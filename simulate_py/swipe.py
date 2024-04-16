# -*- encoding=utf8 -*-
__author__ = "dotua"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from jinja2.compiler import generate

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["android://127.0.0.1:5037/7cbc1b6a?touch_method=MAXTOUCH&",], project_root="D:/tool_test_game/simulate_py")



from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
swipe([1000,400],[400,400])

# script content
print("start...")
