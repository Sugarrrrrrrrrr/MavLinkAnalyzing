class mavLinkAnalyzing:
    dataStrList = []

    def __init__ (self, dataStrList):
        self.dataStrList = dataStrList

    def getMessageID(self):
        if self.dataStrList[0] == '0xfe':
           if len(self.dataStrList) >5:
              return int(self.dataStrList[5], 16)

    def getDataStr(self):
        dataStr = ''
        for s in self.dataStrList:
            if eval(s) >= 16:
                dataStr += s[2:4]
            else:
                dataStr += '0' + s[2]
        return dataStr

    def getDescription(self):
        
        messageID = self.getMessageID()

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

        return description
                

    













import binascii


if __name__ == '__main__':

    dataStr = '0xfe 0x19 0x13 0x1 0x1 0x16 0x0 0x0 0xf0 0x42 0xfc 0x1 0x0 0x0 0x53 0x59 0x53 0x49 0x44 0x5f 0x53 0x57 0x5f 0x4d 0x52 0x45 0x56 0x0 0x0 0x0 0x4 0x4a 0xb5'
    
    dataStrList = dataStr.split()
    ml = mavLinkAnalyzing(dataStrList)
    
    print(ml.dataStrList)
    print(ml.getMessageID())
    print(ml.getDataStr())
    print(ml.getDescription())

    
    
