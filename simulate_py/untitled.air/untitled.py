# -*- encoding=utf8 -*-
__author__ = "Monkey"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
p = poco("ShadowOwl(Clone)_0").get_position()[0]
print(p)