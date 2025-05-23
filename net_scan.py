#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    ansvered_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=False)[0]


    clients_list=[]
    for element in ansvered_list:
        clients_dict={"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Addres\n---------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


scan_result=scan("192.168.1.1/24")
print_result(scan_result)
