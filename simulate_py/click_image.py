# -*- encoding=utf8 -*-
__author__ = "Monkey"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/7cbc1b6a?touch_method=MAXTOUCH&",])


# script content
print("start...")

# image = Image.open("D:/tool_test_game/config/image/unit1/apple.png")
# touch(image)
#unit1

touch(Template(r"apple.png", record_pos=(0.246, -0.142), resolution=(1600, 720)))


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)