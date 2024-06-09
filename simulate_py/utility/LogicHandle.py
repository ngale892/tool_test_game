from poco.drivers.unity3d import UnityPoco
def get_device_id():
    return 'SSIRZH6PKFIB89QK'

def get_element(name):
    poco = UnityPoco()
    names = name.split('/')
    for i in range(len(names)):
        if i == 0:
            a = poco(names[i])
        else:
            a = a.child(names[i])
