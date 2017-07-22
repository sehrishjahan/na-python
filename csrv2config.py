
hostname csrv2
!
ip domain name csrv.local
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
!

