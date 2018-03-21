
if __name__ == '__main__':

    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<FileName>'):
                line = f.readline().strip()  # type: str
                if line.endswith('.pcap'):
                    line = line[0:-5]
                file_name = line
                break

    l1 = []
    l2 = []
    l3 = []
    uav_id = None
    time = None
    xy = None
    delta_t = None
    with open(file_name + '_[2]' + '.txt', 'rt') as f:
        for line in f:
            if line.startswith('U:'):
                uav_id = eval(line[2:])
            elif line.startswith('T:'):
                time = eval(line[2:])
            elif line.startswith('M:'):
                xy = eval(line[2:])

                if uav_id == 3:
                    if len(l1) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l1[-1][1]
                    l1.append((uav_id, time, xy, delta_t))
                elif uav_id == 5:
                    if len(l2) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l2[-1][1]
                    l2.append((uav_id, time, xy, delta_t))
                elif uav_id == 6:
                    if len(l3) == 0:
                        delta_t = 0
                    else:
                        delta_t = time - l3[-1][1]
                    l3.append((uav_id, time, xy, delta_t))

    with open(file_name + '_[3]' + '.txt', 'wt') as f:
        print(l1, file=f)
        print(l2, file=f)
        print(l3, file=f)

    with open(file_name + '_[3]' + '.txt', 'rt') as f:
        line = f.readline()
        l1 = eval(line)
        line = f.readline()
        l2 = eval(line)
        line = f.readline()
        l3 = eval(line)