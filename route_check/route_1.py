import dpkt
import socket
import time


def stol(s):
    l = [-1, -1, -1, -1]
    lines = s.splitlines()

    for i in range(2, len(lines)):
        ips = lines[i].split()
        if ips[0][-1] == '2':
            l[0] = eval(ips[1][-1])
        elif ips[0][-1] == '3':
            l[1] = eval(ips[1][-1])
        elif ips[0][-1] == '5':
            l[2] = eval(ips[1][-1])
        elif ips[0][-1] == '0':
            l[3] = eval(ips[1][-1])
    return l


def compare(s1, s2):
    l1 = stol(s1)
    l2 = stol(s2)
    flag = True
    for i in range(4):
        if l1[i]!=l2[i]:
            flag = False
            break
    if flag:
        return True
    else:
        return False


if __name__ == '__main__':

    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<FileName>'):
                line = f.readline().strip()     # type: str
                if line.endswith('.pcap'):
                    line = line[0:-5]
                file_name = line

            if line.startswith('<IP>'):
                line = f.readline().strip()     # type: str
                IP = line

            if line.startswith('<port>'):
                line = f.readline().strip()     # type: str
                port = line

    with open(file_name + '.pcap', 'rb') as file:
        f = open(file_name + '.txt', 'w')
        pcap = dpkt.pcap.Reader(file)
        r = ''
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            # print ('Timestamp: ', str(datetime.datetime.utcfromtimestamp(ts)))
            # print ('Ethernet Frame: ', mac_addr(eth.src), ' --> ', mac_addr(eth.dst), ' | ', eth.type)

            if not isinstance(eth.data, dpkt.ip.IP):
                #print ('Non IP Packet type not supported %s\n' %eth.data.__class__.__name__)
                continue
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)

            if not (src == IP or dst == IP):
                # print('not 192.168.1.4')
                continue

            if not isinstance(ip.data, dpkt.udp.UDP):
                # print ('Non UDP Packet type not supported %s\n' %ip.data.__class__.__name__)
                continue

            udp = ip.data
            sport = udp.sport
            dport = udp.dport

            if not (str(dport) == port):
                # print('not 14550')
                continue

            s = str(udp.data[8:], encoding='utf-8')
            if not compare(r, s):
                print(time.asctime(time.localtime(ts)), file=f)
                print(s, file=f)
                r = s
