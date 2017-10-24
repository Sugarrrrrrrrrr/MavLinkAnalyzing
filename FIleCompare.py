import json


class DebugFile:
    def __init__(self, file_name):
        self.d_list = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if lines[i].startswith("to") or lines[i].startswith("from"):
                    if lines[i].startswith("to"):
                        i += 1
                        type = 'to'
                        list = lines[i].split()
                    elif lines[i].startswith("from"):
                        i += 1
                        type = 'from'
                        list = lines[i].split()
                    for i in range(len(list)):
                        if eval('0x' + list[i]) < 16:
                            list[i] = '0' + list[i]

                    self.d_list.append((type, list))

class WireSharkFile:
    def __init__(self, file_name):
        self.w_list = []
        with open(file_name, 'r') as file:
            jsons = json.load(file)
            for i in range(len(jsons)):
                if '_source' in jsons[i]:
                    if 'layers' in jsons[i]['_source']:
                        if 'ip' in jsons[i]['_source']['layers']:

                            # type
                            if jsons[i]['_source']['layers']['ip']['ip.src_host'] == '10.1.10.3':
                                type = 'to'
                            elif jsons[i]['_source']['layers']['ip']['ip.src_host'] == '192.168.1.3':
                                type = 'from'
                            else:
                                type = 'none'

                            if 'udp' in jsons[i]['_source']['layers']:
                                if 'data' in jsons[i]['_source']['layers']:
                                    if 'data.data' in jsons[i]['_source']['layers']['data']:
                                        list = jsons[i]['_source']['layers']['data']['data.data'].split(':')
                                    else:
                                        print('----- no data.data -----')
                                else:
                                    list = ['NULL']
                                    print('----- no data -----')
                            else:
                                print('----- no udp -----')
                        else:
                            print('----- no ip -----')
                    else:
                        print('----- no layers -----')
                else:
                    print('----- no _source -----')

                self.w_list.append((type, list))


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

if __name__ == "__main__":
    n = 1
    df = DebugFile('_debug%d' % n)
    wf = WireSharkFile('_Wireshark%d' % n)

    i = 0
    j = 0
    while i<len(df.d_list) and j<len(wf.w_list):
        if comp(df.d_list[i], wf.w_list[j]):
            print(df.d_list[i])
            print(wf.w_list[j])
            print('----------')
        else:
            print(df.d_list[i])
            print(wf.w_list[j])
            print('!!!!! Warning')
            if df.d_list[i][0] == wf.w_list[j][0]:
                print(df.d_list[i][0])
            else:
                print(df.d_list[i][0])
                print(wf.w_list[j][0])
            print('-----type')
            input()

            #input()

        i += 1
        j += 1