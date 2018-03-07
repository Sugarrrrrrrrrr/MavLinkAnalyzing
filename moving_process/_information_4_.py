if __name__ == '__main__':

    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<FileName>'):
                line = f.readline().strip()  # type: str
                if line.endswith('.pcap'):
                    line = line[0:-5]
                file_name = line
                break

    with open(file_name + '_[3]' + '.txt', 'rt') as f_r:
        l1 = eval(f_r.readline())
        l2 = eval(f_r.readline())
        l3 = eval(f_r.readline())
        with open(file_name + '_[4]' + '.txt', 'wt') as f_w:

            f_w.write('l1 = [')
            for i in l1:
                lat = i[2][0]
                lng = i[2][1]
                f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
            f_w.write('];\n')

            f_w.write('l2 = [')
            for i in l2:
                lat = i[2][0]
                lng = i[2][1]
                f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
            f_w.write('];\n')

            f_w.write('l3 = [')
            for i in l3:
                lat = i[2][0]
                lng = i[2][1]
                f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
            f_w.write('];\n')