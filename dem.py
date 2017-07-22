from netmiko import ConnectHandler
from ospfdevices import csrv2

def check_bgp(net_connect, cmd='show run | inc router ospf'):
    """Check whether BGP is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'ospf' in output




