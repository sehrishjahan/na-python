from datetime import datetime

from netmiko import ConnectHandler
import getpass

#from devices import csrv, csrv2, csrv3

csrv1 = {    
    'device_type': 'cisco_ios',
    'ip': '192.168.2.11',
    'username': 'csrv',
    'password': 'telnet',
    'secret': 'cisco'
}

csrv2 = {    
    'device_type': 'cisco_ios',
    'ip': '192.168.2.12',
    'username': 'cisco',
    'password': 'cisco1234',
    'secret': 'cisco1234'
}

csrv3 = {    
    'device_type': 'cisco_ios',
    'ip': '192.168.2.13',
    'username': 'cisco',
    'password': 'cisco1234',
    'secret': 'cisco1234'
}

def check_bgp(net_connect, cmd='show run | inc router bgp'):
    """Check whether BGP is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'bgp' in output

def remove_bgp_config(net_connect, cmd='no router bgp', as_number=''):
    """Remove BGP from the config"""
    bgp_cmd = "{} {}".format(cmd, str(as_number))
    cmd_list = [bgp_cmd]
    output = net_connect.send_config_set(cmd_list)
   # if net_connect.device_type == 'cisco_xr_ssh':
    #    output += net_connect.commit()
    print output

def configure_bgp(net_connect, file_name=''):
    """Configure BGP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        #if net_connect.device_type == 'cisco_xr_ssh':
         #   output += net_connect.commit()
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv1, csrv2, csrv3]
#     file_list = ['bgp_csrv1.txt', 'bgp_csrv2.txt', 'bgp_csrv3.txt'] 
    

    for a_device in device_list:
       # as_number = a_device.pop('as_number')
        as_number = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_bgp(net_connect):
            print "BGP currently configured"
            remove_bgp_config(net_connect, as_number=as_number)
        else:
            print "No BGP"
        # Construct file name 
        file_name = "bgp_" + a_device + ".txt"
        # Check BGP is now gone
        if check_bgp(net_connect):
            raise ValueError("BGP configuration still detected")
    
    # Configure BGP
        bgpconfig = configure_bgp(net_connect, file_name)
        print bgpconfig
#         bgpconfig2 = configure_bgp(net_connect, 'bgp_csrv2.txt')
#         print bgpconfig2
#         bgpconfig3 = configure_bgp(net_connect, 'bgp_csrv3.txt')
#         print bgpconfig3
        
if __name__ == "__main__":
    main()
