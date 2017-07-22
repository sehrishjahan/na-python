




def configure_bgp(net_connect, file_name=''):
    """Configure BGP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        if net_connect.device_type == 'cisco_xr_ssh':
            output += net_connect.commit()
        return output
    except IOError:
print "Error reading file: {}".format(file_name)
