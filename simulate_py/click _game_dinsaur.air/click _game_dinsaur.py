# -*- encoding=utf8 -*-
__author__ = "dotua"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

poco("Vp0").click()


