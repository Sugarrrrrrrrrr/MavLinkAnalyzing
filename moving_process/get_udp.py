# -*- coding: UTF-8 -*-

import pcap
import dpkt
import datetime
import socket
from dpkt.compat import compat_ord

from moving_process._information_1_extraction import WriteLine


def mac_addr(address): #转换mac地址为字符串
    return ':'.join('%02x' % compat_ord(b) for b in address)


def inet_to_str(inet): #转换ip地址为字符串
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)


def get_udp_from_dev(network='10.168.103.0', port='14550'):
    devs = pcap.findalldevs()
    pc = None
    for dev in devs:
        try:
            t = inet_to_str(pcap.lookupnet(bytearray(dev, 'utf-8'))[0])
        except Exception as e:
            print(e)
        if t == network:
            pc = pcap.pcap(dev)
    if not pc:
        return False

    pc.setfilter('udp')    #设置监听过滤器,这里指定port 'udp port 54915'
    for ts, buf in pc:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            print ('Non IP Packet type not supported %s\n' %eth.data.__class__.__name__)
            continue
        ip = eth.data
        if isinstance(ip.data, dpkt.udp.UDP):
            udp = ip.data
            print('[+] Src:', udp.sport, ' --> Dst:', udp.dport)

        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK
        print ('Timestamp: ', str(datetime.datetime.utcfromtimestamp(ts)))
        print ('Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)
        print ('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)' % \
(inet_to_str(ip.src),inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,fragment_offset))


def get_udp_from_network(filename='192.168.1.0', ip_list=['192.168.1.4'], port=14550):
    devs = pcap.findalldevs()
    pc = None
    for dev in devs:
        try:
            t = inet_to_str(pcap.lookupnet(bytearray(dev, 'utf-8'))[0])
        except Exception as e:
            print(e)
            continue
        if t == filename:
            pc = pcap.pcap(dev)
    if not pc:
        return False

    pc.setfilter('ip host %s and udp port %d' % (ip_list[0], port))
    # print('ip host %s and udp port %d' % (ip_list[0], port))

    for ts, buf in pc:
        # print(buf)

        eth = dpkt.ethernet.Ethernet(buf)

        if not isinstance(eth.data, dpkt.ip.IP):
            continue

        ip = eth.data
        src = socket.inet_ntoa(ip.src)
        dst = socket.inet_ntoa(ip.dst)

        if not (src in ip_list or dst in ip_list):
            print('not %s' % ip_list[0])
            print(src, dst)
            continue

        if not isinstance(ip.data, dpkt.udp.UDP):
            print('Non UDP Packet type not supported %s\n' %ip.data.__class__.__name__)
            continue

        udp = ip.data
        sport = udp.sport
        dport = udp.dport

        if not (sport == port or dport == port):
            print('not %d' % port)
            print(sport, dport)
            continue

        # print(udp.data)
        src_addr = (src, sport)
        yield (udp.data, src_addr)


def get_udp_from_file(filename='../data/test.pcap', ip_list=['192.168.1.4'], port=14550, p_wl=None):
    with open(filename,'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        # pcap.setfilter('udp port 14550')
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            #print ('Timestamp: ', str(datetime.datetime.utcfromtimestamp(ts)))
            #print ('Ethernet Frame: ', mac_addr(eth.src), ' --> ', mac_addr(eth.dst), ' | ', eth.type)
            line = 'T:' + str(ts)
            p_wl.write(line)

            if not isinstance(eth.data, dpkt.ip.IP):
                #print ('Non IP Packet type not supported %s\n' %eth.data.__class__.__name__)
                continue
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)

            if not (src in ip_list or dst in ip_list):
                #print('not 192.168.1.4')
                continue

            if not isinstance(ip.data, dpkt.udp.UDP):
                #print ('Non UDP Packet type not supported %s\n' %ip.data.__class__.__name__)
                continue
            
            udp = ip.data
            sport = udp.sport
            dport = udp.dport

            if not (dport==port):
                #print('not 14550')
                continue

            yield udp.data

from PyQt5.QtCore import QThread
import threading
class get_udp(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        get_udp_from_dev()

if __name__ == '__main__':
    #ip_list = ['192.168.1.4']
    #port = 14550

    #for data in udp_data_from_file(ip_list, port):
        #print(data)
        #input()
    gu = get_udp()
