#!/usr/bin/env python

from datetime import datetime

from netmiko import ConnectHandler
from devices import csrv, csrv2, csrv3


def main():
    device_list = [csrv, csrv2, csrv3]
    start_time = datetime.now()
    print
    for device in device_list:
        net_connect = ConnectHandler(**csrv)
        print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
    print "Time elapsed: {}\n".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
