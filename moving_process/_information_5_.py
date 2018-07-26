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
        l4 = eval(f_r.readline())

        begin_end_time_list = []
        if l1:
            begin_end_time_list.append(l1[0][1])
            begin_end_time_list.append(l1[-1][1])
        if l2:
            begin_end_time_list.append(l2[0][1])
            begin_end_time_list.append(l2[-1][1])
        if l3:
            begin_end_time_list.append(l3[0][1])
            begin_end_time_list.append(l3[-1][1])
        if l4:
            begin_end_time_list.append(l4[0][1])
            begin_end_time_list.append(l4[-1][1])
        st = min(begin_end_time_list)
        et = max(begin_end_time_list)

        with open(file_name + '_[5]' + '.txt', 'wt') as f_w:

            if l1:
                # l1
                f_w.write('l1 = [')
                for i in l1:
                    lat = i[2][0]
                    lng = i[2][1]
                    f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
                f_w.write('];\n')
                # st1
                st1 = st
                f_w.write('st1 = %f;\n' % st1)
                # et1
                et1 = et
                f_w.write('et1 = %f;\n' % et1)
                # lt1
                tl1 = [0]
                f_w.write('tl1 = [0, ')
                j = 1
                for i in range(1, 100):
                    t = st1 + i * (et1 - st1) / 100
                    while l1[j][1] <= t:
                        if j == len(l1)-1:
                            break
                        j += 1
                    tl1.append(j-1)
                    f_w.write('%d, ' % tl1[i])
                tl1.append(len(l1)-1)
                f_w.write('%d];\n' % tl1[100])

            if l2:
                # l2
                f_w.write('l2 = [')
                for i in l2:
                    lat = i[2][0]
                    lng = i[2][1]
                    f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
                f_w.write('];\n')
                # st2
                st2 = st
                f_w.write('st2 = %f;\n' % st2)
                # et2
                et2 = et
                f_w.write('et2 = %f;\n' % et2)
                # tl2
                tl2 = [0]
                f_w.write('tl2 = [0, ')
                j = 1
                for i in range(1, 100):
                    t = st2 + i * (et2 - st2) / 100
                    while l2[j][1] <= t:
                        if j == len(l2)-1:
                            break
                        j += 1
                    tl2.append(j - 1)
                    f_w.write('%d, ' % tl2[i])
                tl2.append(len(l2) - 1)
                f_w.write('%d];\n' % tl2[100])
            if l3:
                # l3
                f_w.write('l3 = [')
                for i in l3:
                    lat = i[2][0]
                    lng = i[2][1]
                    f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
                f_w.write('];\n')
                # st3
                st3 = st
                f_w.write('st3 = %f;\n' % st3)
                # et3
                et3 = et
                f_w.write('et3 = %f;\n' % et3)
                # tl3
                tl3 = [0]
                f_w.write('tl3 = [0, ')
                j = 1
                for i in range(1, 100):
                    t = st3 + i * (et3 - st3) / 100
                    while l3[j][1] <= t:
                        if j == len(l3)-1:
                            break
                        j += 1
                    tl3.append(j - 1)
                    f_w.write('%d, ' % tl3[i])
                tl3.append(len(l3) - 1)
                f_w.write('%d];\n' % tl3[100])
            if l4:
                # l4
                f_w.write('l4 = [')
                for i in l4:
                    lat = i[2][0]
                    lng = i[2][1]
                    f_w.write('\t{lat: %f, lng: %f},' % (lat, lng))
                f_w.write('];\n')
                # st4
                st4 = st
                f_w.write('st4 = %f;\n' % st4)
                # et4
                et4 = et
                f_w.write('et4 = %f;\n' % et4)
                # tl4
                tl4 = [0]
                f_w.write('tl4 = [0, ')
                j = 1
                for i in range(1, 100):
                    t = st4 + i * (et4 - st4) / 100
                    while l4[j][1] <= t:
                        if j == len(l4)-1:
                            break
                        j += 1
                    tl4.append(j - 1)
                    f_w.write('%d, ' % tl4[i])
                tl4.append(len(l4) - 1)
                f_w.write('%d];\n' % tl4[100])

