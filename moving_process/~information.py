import moving_process._information_1_extraction
import moving_process._information_2_clean_up
import moving_process._information_3_formatting
import moving_process._information_5_

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
            moving_process._information_1_extraction.do(file_name, IP, ports)
            moving_process._information_2_clean_up.do(file_name, IP, ports)
            moving_process._information_3_formatting.do(file_name, IP, ports)
            moving_process._information_5_.do(file_name, IP, ports)