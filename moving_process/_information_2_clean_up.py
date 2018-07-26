
if __name__ == '__main__':

    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<FileName>'):
                line = f.readline().strip()  # type: str
                if line.endswith('.pcap'):
                    line = line[0:-5]
                file_name = line
                break

    p = None
    with open(file_name + '_[1]' + '.txt', 'rt') as f_r:
        with open(file_name + '_[2]' + '.txt', 'wt') as f_w:
            for line in f_r:
                if line.startswith('U:'):
                    f_w.write(line)
                    p = 'u'
                elif line.startswith('M:'):
                    f_w.write(line)
                    p = 'm'
                elif line.startswith('T:'):
                    if p != 't':
                        f_w.write(line)
                        p = 't'
