iperf3 -s -D -I ./iperf3.pid --logfile ./iperf3.log --bind-dev eth0

pkill -F ./iperf3.log

* have button switch to dhcp mode (display this on lcd)

journalctl -u isc-dhcp-server.service
sudo nano /etc/default/isc-dhcp-server


```

pmard@rpi-alpha:~ $ cd ethtester/
pmard@rpi-alpha:~/ethtester $ source ethtest/bin/activate
(ethtest) pmard@rpi-alpha:~/ethtester $

```


running isc-dhcp-server


```
pmard@rpi-alpha:~/ethtester $ cat /etc/default/isc-dhcp-server
# Defaults for isc-dhcp-server (sourced by /etc/init.d/isc-dhcp-server)

# Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
DHCPDv4_CONF=/etc/dhcp/dhcpd.conf
#DHCPDv6_CONF=/etc/dhcp/dhcpd6.conf

# Path to dhcpd's PID file (default: /var/run/dhcpd.pid).
DHCPDv4_PID=/var/run/dhcpd.pid
#DHCPDv6_PID=/var/run/dhcpd6.pid

# Additional options to start dhcpd with.
#       Don't use options -cf or -pf here; use DHCPD_CONF/ DHCPD_PID instead
#OPTIONS=""

# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
#       Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACESv4="eth0"
#INTERFACESv6=""
```


```
pmard@rpi-alpha:~/ethtester $ cat /etc/dhcp/dhcpd.conf
# dhcpd.conf

subnet 10.0.0.0 netmask 255.255.255.0 {
   authoritative;
   range 10.0.0.1 10.0.0.254;
   default-lease-time 3600;
   max-lease-time 3600;
   option subnet-mask 255.255.255.0;
   option broadcast-address 10.0.0.255;
   option routers 10.0.0.0;
   option domain-name-servers 8.8.8.8;
   option domain-name "example.com";
}
```



```
iperf3 -c 10.0.0.1 -B 10.0.0.2
```

random note: max tcp throughput is ~94% (940-950 Mbps, where M=10^6)

