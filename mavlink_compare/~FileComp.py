# data/_debug1
#   to_str:     'to' 飞机发地面站
#   from_str:   'from' 地面站发飞机
# data/_Wireshark1
#   uav_ip
#   groundstation_ip


import json

class DebugFile:
    def __init__(self, file_name, to_str, from_str):
        self.d_list = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if lines[i].startswith(to_str) or lines[i].startswith(from_str):
                    if lines[i].startswith(to_str):
                        i += 1
                        type = 'to'
                        list = lines[i].split()
                    elif lines[i].startswith(from_str):
                        i += 1
                        type = 'from'
                        list = lines[i].split()
                    for i in range(len(list)):
                        if eval('0x' + list[i]) < 16:
                            list[i] = '0' + list[i]

                    self.d_list.append((type, list))

class WireSharkFile:
    def __init__(self, file_name, uav_ip, groundstation_ip):
        self.w_list = []
        with open(file_name, 'r') as file:
            jsons = json.load(file)
            for i in range(len(jsons)):
                if '_source' in jsons[i]:
                    if 'layers' in jsons[i]['_source']:
                        if 'ip' in jsons[i]['_source']['layers']:

                            # type
                            if jsons[i]['_source']['layers']['ip']['ip.src_host'] == uav_ip:
                                data_type = 'to'
                            elif jsons[i]['_source']['layers']['ip']['ip.src_host'] == groundstation_ip:
                                data_type = 'from'
                            else:
                                data_type = 'none'

                            if 'udp' in jsons[i]['_source']['layers']:
                                if 'data' in jsons[i]['_source']['layers']:
                                    if 'data.data' in jsons[i]['_source']['layers']['data']:
                                        data_list = jsons[i]['_source']['layers']['data']['data.data'].split(':')
                                    else:
                                        print('----- no data.data -----')
                                else:
                                    data_list = ['NULL']
                                    # print('----- no data -----')
                            else:
                                print('----- no udp -----')
                        else:
                            print('----- no ip -----')
                    else:
                        print('----- no layers -----')
                else:
                    print('----- no _source -----')

                self.w_list.append((data_type, data_list))


def comp(d, w):
    d_now = d[1]
    w_now = w[1]

    flag = True
    if not d[0] == w[0]:
        flag = False
    else:
        if not len(d_now) == len(w_now):
            flag = False
        else:
            for i in range(len(d_now)):
                if not d_now[i] == w_now[i]:
                    flag = False
    return flag


def _to(n, uav_ip, groundstation_ip, to_str, from_str):
    df = DebugFile('data/_debug%d' % n, to_str, from_str)
    wf = WireSharkFile('data/_Wireshark%d' % n, uav_ip, groundstation_ip)

    lost_list = []
    n_to = 0
    for i in range(len(df.d_list)):
        if df.d_list[i][0] == 'to':
            n_to += 1
        f = False
        for j in range(len(wf.w_list)):
            if comp(df.d_list[i], wf.w_list[j]):
                f = True
                wf.w_list.pop(j)
                break
        if not f:
            lost_list.append((i, df.d_list[i]))
            # print(i, df.d_list[i])

    return n_to, lost_list


def _from(n, uav_ip, groundstation_ip, to_str, from_str):
    df = DebugFile('data/_debug%d' % n, to_str, from_str)
    wf = WireSharkFile('data/_Wireshark%d' % n, uav_ip, groundstation_ip)

    lost_list = []
    n_from = 0
    for i in range(len(wf.w_list)):
        if wf.w_list[i][0] == 'from':
            n_from += 1
        f = False
        for j in range(len(df.d_list)):
            if comp(wf.w_list[i], df.d_list[j]):
                f = True
                df.d_list.pop(j)
                break
        if not f:
            lost_list.append((i, wf.w_list[i]))
            # print(j, wf.w_list[i])

    return n_from, lost_list


def main():

# --------------------------------------------------#
    n = 30107
    uav_ip = '192.168.1.254'
    groundstation_ip = '192.168.1.7'
    to_str = 'to'
    from_str = 'from'
# --------------------------------------------------#
    
    
    n_to, to_lost_list = _to(n, uav_ip, groundstation_ip, to_str, from_str)
    n_from, from_lost_list = _from(n, uav_ip, groundstation_ip, to_str, from_str)

    with open('%d.txt'% n, 'w') as file:
        file.write('''%d UDP to %s in debug
%d lost in wireshark

%d UDP from %s in wireshark
%d lost in debug

------------------------------
''' % (n_to, groundstation_ip, len(to_lost_list), n_from, groundstation_ip, len(from_lost_list)))

        file.write('to %s lost list:'% groundstation_ip)
        file.write('\n\n')
        for item in to_lost_list:
            file.write('%d UDP from debug' % item[0])
            file.write('\n')
            file.write(str(item[1]))
            file.write('\n\n')

        file.write('from %s lost list:'% groundstation_ip)
        file.write('\n\n')
        for item in from_lost_list:
            file.write('%d UDP from wireshare' % item[0])
            file.write('\n')
            file.write(str(item[1]))
            file.write('\n')
            file.write('\n\n')


if __name__ == '__main__':
    main()
