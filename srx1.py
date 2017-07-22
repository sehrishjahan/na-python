from netmiko import ConnectHandler

srx1 = {
'device_type':'juniper',
'ip': '192.168.2.14',
'username': 'juniper',
'password':'cisco1234',
}


def main():
    device_list = [csrv, csrv2, csrv3]
    start_time = datetime.now()
    print
    for a_device in device_list:
        net_connect = ConnectHandler(**csrv)
        print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
    print "Time elapsed: {}\n".format(datetime.now() - start_time)


if __name__ == "__main__":
main()
