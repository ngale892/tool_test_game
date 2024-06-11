import json

from poco.drivers.unity3d import UnityPoco

from utility import Constanst
from utility.Constanst import DEVICE_ID


def get_device_id():
    print(Constanst.ROOT_DIR)
    data = read_json_file("D:"+Constanst.CONFIG_FILE)
    return data[DEVICE_ID]

def get_element(name):
    poco = UnityPoco()
    names = name.split('/')
    for i in range(len(names)):
        if i == 0:
            a = poco(names[i])
        else:
            a = a.child(names[i])

def read_json_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def write_json_file(jsonStr, key, value, path):
    jsonStr[key] = value

    with open(path, "w") as outfile:
        outfile.write(json.dumps(jsonStr))
