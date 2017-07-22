from datetime import datetime

from netmiko import ConnectHandler
from ospfdevices import csrv2, csrv3


def check_bgp(net_connect, cmd='show run | inc router bgp'):
    """Check whether BGP is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'bgp' in output

def main():
    device_list = [csrv2, csrv3]
    start_time = datetime.now()
    print

    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        net_connect.enable()
        print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_bgp(net_connect):
            print "BGP currently configured"
        else:
            print "No BGP"
        print

    print "Time elapsed: {}\n".format(datetime.now() - start_time)


if __name__ == "__main__":
main()
