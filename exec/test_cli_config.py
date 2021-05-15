"""
This script accepts configuration from user as a command line argument and commits it to the router.

How to run?
script run exec <path> test_xr_config.py arguments <configuration>
eg: script run test_xr_config.py arguments "hostname ios" 

How to verify:
show run | i <configuration>
check for syslog: 'SCRIPT : Configuration succeeded'
""" 
import argparse
import pprint
from iosxr.xrcli.xrcli_helper import *
from cisco.script_mgmt import xrlog

syslog = xrlog.getSysLogger('sample_script')
helper = XrcliHelper(debug = True)

def test_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="single line string command",type=str)
    args = parser.parse_args()
    config = args.cmd
    result = helper.xr_apply_config_string(config)
    if result['status'] == 'success':
        syslog.info('SCRIPT : Configuration succeeded')
    else:
        syslog.error('SCRIPT : Configuration failed')
    

if __name__ == '__main__':
    test_config()
