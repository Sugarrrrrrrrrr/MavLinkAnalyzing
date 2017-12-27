import json
import xlwt

with open('QGC', 'r') as f:
    packetList = json.load(f)
xls = xlwt.Workbook()
sheet = xls.add_sheet('sample')

index = 0
row = 0

for packet in packetList:
    index += 1
    # 序号
    print('No.', index)
    #sheet.write(row, 0, index)



    # 方向
    if '_source' in packet:
        _source = packet['_source']
        if 'layers' in _source:
            layers = _source['layers']
            if 'ip' in layers:
                ip = layers['ip']
                if 'ip.dst_host' in ip:
                    if ip['ip.dst_host'] == '255.255.255.255':
                        print('DOWN')
                        sheet.write(row, 1, 'DOWN')
                    else:
                        print('UP')
                        sheet.write(row, 1, 'UP')
            # 数据
            if 'udp' in layers:
                # 序号
                sheet.write(row, 0, index)
                if 'data' in layers:
                    Data = layers['data']
                    if 'data.data' in Data:
                        data = Data['data.data'].replace(':','')
                        #print(data)

                        # 分割 message
                        j = 0
                        messageList = []
                        
                        while j<len(data):
                            i = data.find('fe',j,len(data))
                            if i == -1:
                                i = len(data)
                            elif i == j:
                                i = j + 2*int(data[j+2:j+4],16)+16
                            messageList.append(data[j:i])
                            j = i
                       
                        print(len(messageList),'messages')
                        for message in messageList:
                            # 消息ID

                            print (message)
                            sheet.write(row, 4, message)
                            
                            if message[0:2] == 'fe' and len(message)>=12: 
                                messageID = int(message[10:12],16)
                                print('#',messageID)
                                sheet.write(row, 2, '#'+str(messageID))

                                # 消息描述
                                if messageID == 0:
                                    description = 'HEARTBEAT;'
                                    
                                elif messageID == 21:
                                    description = 'PARAM_REQUEST_LIST;'
                                    
                                elif messageID == 76:
                                    description = 'COMMAND_LONG;'
                                    
                                elif messageID == 66:
                                    description = 'REQUEST_DATA_STREAM;'
                                    
                                elif messageID == 253:
                                    description = 'STATUSTEXT (状态文本消息); '
                                    
                                elif messageID == 22:
                                    description = 'PARAM_VALUE;'
                                    
                                elif messageID == 20:
                                    description = 'PARAM_REQUEST_READ; '
                                    
                                elif messageID == 148:
                                    description = 'AUTOPILOT_VERSION; 飞控的版本和功能 '
                                    
                                elif messageID == 77:
                                    description = 'COMMAND_ACK; (应答命令 0x0802, 执行结果 0x00) '
                                    
                                elif messageID == 27:
                                    description = 'RAW_IMU; 原始的姿态传感器信息（加速度xyz, 角速度xyz, 地磁强度xyz） '
                                    
                                elif messageID == 116:
                                    description = 'SCALED_IMU2; secondary 9DOF sensor setup '
                                    
                                elif messageID == 29:
                                    description = 'SCALED_PRESSURE; 处理之后的气压数据'
                                    
                                elif messageID == 1:
                                    description = 'SYS_STATUS; 系统状态'
                                    
                                elif messageID == 125:
                                    description = 'POWER_STATUS; 电池状态'
                                    
                                elif messageID == 152:
                                    description = 'MEMINFO; APM内存状态'
                                    
                                elif messageID == 42:
                                    description = 'MISSION_CURRENT; 当前任务'
                                    
                                elif messageID == 24:
                                    description = 'GPS_RAW_INT; RAW格式的GPS数据'
                                    
                                elif messageID == 62:
                                    description = 'NAV_CONTROLLER_OUTPUT; 导航控制器输出, 目标滚转角、俯仰角、指向角、距离、高度差、速度差'
                                    
                                elif messageID == 36:
                                    description = 'SERVO_OUTPUT_RAW; 舵机输出原始数据'
                                    
                                elif messageID == 35:
                                    description = 'RC_CHANNELS_RAW; 遥控通道RAW格式数据'
                                    
                                elif messageID == 30:
                                    description = 'ATTITUDE; 姿态数据，滚转角、俯仰角、偏航角、滚转角速度、俯仰角速度、偏航角速度'
                                    
                                elif messageID == 178:
                                    description = 'AHRS2; secondary AHRS 姿态数据'
                                    
                                elif messageID == 74:
                                    description = 'VFR_HUD; 用在HUD显示上的各种数据, 空速、地速、航向、油门、高度、爬升率'

                                elif messageID == 33:
                                    description = 'GLOBAL_POSITION_INT; 整数型表示的全球定位数据'

                                elif messageID == 163:
                                    description = 'AHRS; DCM状态'

                                elif messageID == 165:
                                    description = 'HWSTATUS; 关键硬件状态'

                                elif messageID == 2:
                                    description = 'SYSTEM_TIME; 系统时间'

                                elif messageID == 193:
                                    description = 'EKF_STATUS_REPORT; EKF状态消息包括标志和方差'

                                elif messageID == 241:
                                    description = 'VIBRATION; 震动等级、加速度计clipping'

                                elif messageID == 150:
                                    description = 'MEMINFO; APM内存状态'


                                else:
                                    print('nodefined')
                                    description = ''
                                print(description)
                                sheet.write(row, 3, description)

                            row += 1;

                            




    if index < 965:
        continue
    if index >= 965:
        break
    aaa=input()

#aaa=input()
xls.save('QGC.xls')


