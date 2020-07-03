from genie.testbed import load
from genie.metaparser.util.exceptions import *
import json


# read from the devices.yaml as testbed file:
testbed = load('devices.yaml')
devices = testbed.devices

class Collectors:

    @staticmethod
    def get_errors():
        returndata = {}

        # Counters to look for:
        counters = [
        "in_errors",
        "in_crc_errors",
        "in_frame",
        "in_overrun",
        "in_ignored",
        "in_with_dribble",
        "out_underruns",
        "out_errors",
        "out_interface_resets",
        "out_collision",
        "out_unknown_protocl_drops",
        "out_babble",
        "out_late_collision",
        "out_deferred",
        "out_lost_carrier",
        "out_no_carrier",
        "out_buffer_failure",
        "out_buffers_swapped"]

        for dev in devices:
            device = testbed.devices[dev]
            returndata[device.name] = {}

            # connect to the device:
            print(device)
            device.connect(log_stdout=False)

            # collect data
            data = device.parse('show interfaces')

            # iterate through each interface and look for errors
            for intf in data:
                for counter in data[intf]['counters']:
                    if counter in counters:
                        if data[intf]['counters'][counter] > 0:
                            returndata[device.name].update({counter: data[intf]['counters'][counter]})

        return returndata


