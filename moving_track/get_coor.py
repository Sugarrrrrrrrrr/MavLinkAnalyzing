import math

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率

def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


if __name__ == '__main__':
    
    with open('.cfg', 'r') as f:
        for line in f:
            if line.startswith('<StatusCenter>'):
                line = f.readline().strip()
                import sys
                sys.path.append(line)
                from parse import mavutil

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

    mf = mavutil.mavlink_connection(file_name + '.pcap', ip_list=[IP], port=eval(port))

    l = []    
    while True:
        try:
            m = mf.recv_match(type='GPS_RAW_INT')
            if out_of_china(m.lon/10000000, m.lat/10000000):
                continue
            if m.lat/10000000 < 22:
                continue
            l.append({'lat': m.lat, 'lng': m.lon})
        except StopIteration as e:
            break
    with open('polylines.txt', 'w') as f:

        f.write('l = [')
        for i in l:
            lat = i['lat']/10000000
            lng = i['lng']/10000000
            lng_lat = wgs84togcj02(lng, lat)
            lng = lng_lat[0]
            lat = lng_lat[1]
            f.write('\t{lat: %f, lng: %f},' % (lat, lng))
        f.write('];')
    
