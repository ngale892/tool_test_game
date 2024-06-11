import config_device
from utility import LogicHandle

if __name__ == '__main__':
   path = "D:\\tool_test_game\\config\\config.json"
   device_id = config_device.get_device_id()
   print(f"Start ...")
   print(f"Set up device ... {device_id}")
   config_device.wait_for_device(device_id)
   config_device.forward_device(device_id)
   config_device.get_prop(device_id)
   config_device.forward_no_rebind(device_id)
   print(f"Save device ID ...")
   json = LogicHandle.read_json_file(path)
   LogicHandle.write_json_file(json,"device_id",device_id,path)
   print("End ...")
