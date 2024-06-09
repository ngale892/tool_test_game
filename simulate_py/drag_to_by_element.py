# -*- encoding=utf8 -*-
__author__ = "Monkey"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from poco.drivers.unity3d import UnityPoco

from utility import Constanst, LogicHandle

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["android://127.0.0.1:5037/" + LogicHandle.get_device_id() + "?touch_method=MAXTOUCH&", ])
@app.route('/drag_to', methods=['GET'])
@cross_origin(origins='*')
def drag_to_elem():
    poco = UnityPoco()
    print("start...")
    index_from = int(request.args.get('index_from'))
    index_to = int(request.args.get('index_to'))
    print(index_from)
    print(index_to)
    poco("wooden tray").child("LettersContainer").child(request.args.get('from'))[index_from].drag_to(
    poco("Wooden Table").child("LettersHolderContainer").child(request.args.get('to'))[index_to])
    print("end...")
    return 'drag!!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='6868')

#example game drag letters to build word: http://127.0.0.1:6868/drag_to?from=E&to=E

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
