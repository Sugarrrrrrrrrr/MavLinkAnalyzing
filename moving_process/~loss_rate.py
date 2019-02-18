import sys
sys.path.append('..')

from moving_process import mavutil
from moving_process._information_1_extraction import WriteLine


def do_1(file_name, IP, ports):
    # new file
    with open('loss_rate/' + file_name + '_[1]' + '.txt', 'w') as f:
        pass

    # file name to write in
    with open('temp.txt', 'w') as f:
        f.write('loss_rate/' + file_name)

    # writeLine obj
    p_WL = WriteLine()

    for port in ports:

        mf = mavutil.mavlink_connection('../data/' + file_name + '.pcap', ip_list=[IP], port=eval(port), p_wl=p_WL)
        line = 'U:' + port[4]
        p_WL.write(line)

        index = -1
        total = 0
        recieve = 0
        loss = 0
        while True:
            try:
                m = mf.recv_msg()
                if m.get_srcSystem() != 0:
                    if index == -1:
                        total = 1
                        recieve = 1
                        loss = 0
                    else:
                        should_get = m.get_seq() - index
                        if should_get < 0:
                            should_get += 256
                        total += should_get
                        recieve += 1
                        loss += should_get - 1
                        # print(should_get)

                    index = m.get_seq()
                    line = 'L:' + str((total, loss))
                    p_WL.write(line)
                    print(index, total, recieve, loss)
                    # print(m.get_srcSystem(), m.get_srcComponent(), m.get_seq())
            except Exception as e:
                print(e)
                break

def do_2(file_name, IP=None, ports=None):
    p = None
    with open('loss_rate/' + file_name + '_[1]' + '.txt', 'rt') as f_r:
        with open('loss_rate/' + file_name + '_[2]' + '.txt', 'wt') as f_w:
            for line in f_r:
                if line.startswith('U:'):
                    f_w.write(line)
                    p = 'u'
                elif line.startswith('L:'):
                    if p != 'l':
                        f_w.write(line)
                        p = 'l'
                elif line.startswith('T:'):
                    if p != 't':
                        f_w.write(line)
                        p = 't'

def do_3(file_name, IP=None, ports=None):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    uav_id = None
    time = None
    xy = None
    delta_t = None
    n = 0
    with open('loss_rate/' + file_name + '_[2]' + '.txt', 'rt') as f:
        for line in f:
            if line.startswith('U:'):
                uav_id = eval(line[2:])
            elif line.startswith('T:'):
                time = eval(line[2:])
            elif line.startswith('L:'):
                xy = eval(line[2:])
                n += 1

                if uav_id == 2:
                    if len(l1) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l1[-1][1]
                    l1.append((uav_id, time, xy, delta_t))
                elif uav_id == 3:
                    if len(l2) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l2[-1][1]
                    l2.append((uav_id, time, xy, delta_t))
                elif uav_id == 5:
                    if len(l3) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l3[-1][1]
                    l3.append((uav_id, time, xy, delta_t))
                elif uav_id == 0 or uav_id == 6:
                    if len(l4) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l4[-1][1]
                    l4.append((uav_id, time, xy, delta_t))

    with open('loss_rate/' + file_name + '_[3]' + '.txt', 'wt') as f:
        print(l1, file=f)
        print(l2, file=f)
        print(l3, file=f)
        print(l4, file=f)


if __name__ == '__main__':

    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<FileName>'):
                line = f.readline().strip()  # type: str
                file_names = line.split()

            if line.startswith('<IP>'):
                line = f.readline().strip()  # type: str
                IP = line

            if line.startswith('<port>'):
                line = f.readline().strip()  # type: str
                ports = line.split()

    for file_name in file_names:
        if file_name.endswith('.pcap'):
            file_name = file_name[0:-5]

            do_1(file_name, IP, ports)
            do_2(file_name, IP, ports)
            do_3(file_name, IP, ports)




