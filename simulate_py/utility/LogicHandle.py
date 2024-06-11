from poco.drivers.unity3d import UnityPoco
def get_device_id():
    data = read_json_file(Constanst.ROOT_DIR+Constanst.CONFIG_FILE)
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
