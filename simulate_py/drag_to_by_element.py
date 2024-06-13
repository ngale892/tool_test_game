# -*- encoding=utf8 -*-
__author__ = "Monkey"

from poco.drivers.unity3d import UnityPoco

auto_setup(__file__)

    print("start...")
    poco("wooden tray").child("LettersContainer").child(request.args.get('from'))[0].drag_to(
        poco("Wooden Table").child("LettersHolderContainer").child(request.args.get('to'))[0])
    print("end...")


# example game drag letters to build word: http://127.0.0.1:6868/drag_to?from=E&to=E

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
