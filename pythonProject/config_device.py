from ppadb.client import Client as AdbClient
import adbutils

client = AdbClient(host="127.0.0.1", port=5037)

def get_device_id():
    global id
    devices = client.devices()
    for device in devices:
        id = (device.serial)
    return id

def wait_for_device(serial):
    try:
        # Wait for device to be detected by ADB
        print(f"Waiting for device {serial} to become available...")
        output = client.shell(f"adb -s {serial} wait-for-device")
        print(f"Device {serial} is now available.")
    except Exception as e:
        print(f"Error waiting for device {serial}: {e}")

def get_prop(serial):
    device = client.device(serial)
    if device:
        prop_value = device.shell("getprop ro.build.version.sdk")
        print(f"Property 'ro.build.version.sdk' value on device {serial}: {prop_value}")
        return prop_value.strip()  # Remove leading/trailing whitespaces
    else:
        print(f"Device {serial} not found.")
        return None


def forward_no_rebind(serial):
    try:
        device = client.device(serial)
        if not device:
            raise ValueError(f"Device {serial} not found.")

        # List existing port forwards using adb command
        result = device.shell("adb forward --list")
        forwards = result.splitlines()

        # Check if the desired forward already exists
        forward_exists = any(f"tcp:14738 tcp:5001" in forward for forward in forwards)

        if forward_exists:
            print(f"Port tcp:14738 -> tcp:5001 already forwarded for device {serial}")
        else:
            device.forward("tcp:14738", "tcp:5001")
            print(f"Port forwarded successfully for device {serial} without rebinding")
    except Exception as e:
        print(f"Error forwarding port for device {serial}: {e}")

def forward_device(serial):
    device = client.device(serial)
    if device:
        device.forward("tcp:8342", "tcp:8342")
        print(f"Port forwarded successfully for device {serial}")
    else:
        print(f"Device {serial} not found.")

def dump_logcat(connection):
    while True:
        data = connection.read(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    connection.close()
def log_cat(serial):
    device = client.device(serial)
    device.shell("logcat",handler=dump_logcat)

