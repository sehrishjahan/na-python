
hostname csrv2
!
boot-start-marker
boot-end-marker
!
!
enable secret 5 $1$3Kd1$WuyBQcTlEP2kRGc9S0DS91
!
no aaa new-model
!
!
!
!         
!
!
!


ip domain name csrv.local
!
!
!
!
!
!
!
!
!
!
subscriber templating
multilink bundle-name authenticated
!
!
license udi pid CSR1000V sn 9T1MN22XONT
!
username cisco secret 5 $1$AKcC$/Us2EFcOOBOQWZWJLQKc11
!
redundancy
 mode none
!
!
!
ip ssh version 2
!
!
!
!
interface GigabitEthernet2
 description MGMT
 ip address 192.168.2.12 255.255.255.0
 negotiation auto
!
interface GigabitEthernet3
 description to_CSRV1_for_BGP
 ip address 192.168.1.12 255.255.255.0
 negotiation auto
!
interface GigabitEthernet6
 description to_SRX1_for_OSPF
 ip address 192.168.4.30 255.255.255.0
 negotiation auto
!
router ospf 100
 router-id 2.2.2.2
 priority 127
 passive-interface GigabitEthernet3
 network 192.168.1.0 0.0.0.255 area 0
 network 192.168.4.0 0.0.0.255 area 0
!
!
virtual-service csr_mgmt
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
!
!
!
control-plane
!         
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 logging synchronous
 login local
 transport input ssh
!
!
end
