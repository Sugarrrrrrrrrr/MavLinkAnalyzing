import re
import xlwt

file = open('MAVLink_20170908_1636.txt')
xls = xlwt.Workbook()
sheet = xls.add_sheet('sample')

b = 0
index = 0
for line in file:
    flag = False
    if line.startswith('s32FrameLen'):
        print('DOWN')
        direction = 'DOWN'
        flag = True
    elif line.startswith('PC back '):
        print('UP')
        direction = 'UP'
        flag = True

    if flag:
        index += 1
        lList = re.findall(r"\b\d+\b",line)
        if lList:
            l = int(lList[0])
            print(l)

        data = file.readline()
        message = data.split()
        print(message)

        messageID = int(message[5],16)

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
            description = ''

        









        row = index
        # index
        sheet.write(row,0,index)
        
        # direction
        sheet.write(row,1,direction)
        
        # messageID
        sheet.write(row,2,'#'+str(messageID))
        
        # description
        sheet.write(row,3,description)
        
        # message
        sheet.write(row,4,message)

        














    print(index)


xls.save('MAVLink_20170908_1636.xls')
