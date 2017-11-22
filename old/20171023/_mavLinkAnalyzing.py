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

        elif messageID == 1:
            description = 'SYS_STATUS; 系统状态'

        elif messageID == 2:
            description = 'SYSTEM_TIME; 系统时间'

        elif messageID == 3:
            description = 'FIXME to be removed / merged with SYSTEM_TIME '

        elif messageID == 5:
            description = 'CHANGE_OPERATOR_CONTROL; 请求控制权'

        elif messageID == 20:
            description = 'PARAM_REQUEST_READ; '
                                    
        elif messageID == 21:
            description = 'PARAM_REQUEST_LIST;'

        elif messageID == 22:
            description = 'PARAM_VALUE;'

        elif messageID == 24:
            description = 'GPS_RAW_INT; RAW格式的GPS数据'

        elif messageID == 27:
            description = 'RAW_IMU; 原始的姿态传感器信息（加速度xyz, 角速度xyz, 地磁强度xyz） '

        elif messageID == 29:
            description = 'SCALED_PRESSURE; 处理之后的气压数据'

        elif messageID == 30:
            description = 'ATTITUDE; 姿态数据，滚转角、俯仰角、偏航角、滚转角速度、俯仰角速度、偏航角速度'                            
        
        elif messageID == 33:
            description = 'GLOBAL_POSITION_INT; 整数型表示的全球定位数据'
        
        elif messageID == 35:
            description = 'RC_CHANNELS_RAW; 遥控通道RAW格式数据'
                                    
        elif messageID == 36:
            description = 'SERVO_OUTPUT_RAW; 舵机输出原始数据'

        elif messageID == 37:
            description = 'MISSION_REQUEST_PARTIAL_LIST; 请求回送一部分任务清单。如果起始代号和结束代号相同，则只发送一个航路点'

        elif messageID == 42:
            description = 'MISSION_CURRENT; 当前任务'

        elif messageID == 43:
            description = 'MISSION_REQUEST_LIST ; 任务单下载请求'

        elif messageID == 44:
            description = 'MISSION_COUNT; 任务计数, 对#43的回应'

        elif messageID == 47:
            description = 'MISSION_ACK; 任务回应, 0成功, 非0出错'

        elif messageID == 55:
            description = 'SAFETY_ALLOWED_AREA; 安全区, frame p1x p1y p1z p2x p2y p2z'

        elif messageID == 60:
            description = 'SET_QUAD_MOTORS_SETPOINT; 四轴机型,马达转速设定'

        elif messageID == 62:
            description = 'NAV_CONTROLLER_OUTPUT; 导航控制器输出, 目标滚转角、俯仰角、指向角、距离、高度差、速度差'

        elif messageID == 63:
            description = 'SET_QUAD_SWARM_LED_ROLL_PITCH_YAW_THRUST;'

        elif messageID == 64:
            description = 'STATE_CORRECTION; 状态修正, 引入偏移, 以修正姿态和速度数据'

        elif messageID == 65:
            description = 'RC_CHANNELS; PPM values of the RC channels received'

        elif messageID == 66:
            description = 'REQUEST_DATA_STREAM; 请求数据流'

        elif messageID == 67:
            description = 'DATA_STREAM; 回应数据请求'

        elif messageID == 74:
            description = 'VFR_HUD; 用在HUD显示上的各种数据, 空速、地速、航向、油门、高度、爬升率'

        elif messageID == 76:
            description = 'COMMAND_LONG;'

        elif messageID == 77:
            description = 'COMMAND_ACK;'

        elif messageID == 93:
            description = 'HIL_ACTUATOR_CONTROLS;'

        elif messageID == 102:
            description = 'VISION_POSITION_ESTIMATE; 视觉位置估值 '

        elif messageID == 108:
            description = 'SIM_STATE; Status of simulation environment, if used'

        elif messageID == 116:
            description = 'SCALED_IMU2; secondary 9DOF sensor setup '

        elif messageID == 124:
            description = 'GPS2_RAW; Second GPS data'

        elif messageID == 125:
            description = 'POWER_STATUS; 电池状态'

        elif messageID == 128:
            description = 'GPS2_RTK; RTK GPS data'

        elif messageID == 129:
            description = 'SCALED_IMU3; The RAW IMU readings for 3rd 9DOF sensor setup'

        elif messageID == 135:
            description = 'TERRAIN_CHECK; 请求飞机返回指定位置的地形高度'

        elif messageID == 136:
            description = 'TERRAIN_REPORT; 应答地形高度'

        elif messageID == 148:
            description = 'AUTOPILOT_VERSION; 飞控的版本和功能 '

        elif messageID == 150:
            description = 'SENSOR_OFFSETS; Offsets and calibrations values for hardware sensors.'

        elif messageID == 152:
            description = 'MEMINFO; APM内存状态'

        elif messageID == 156:
            description = 'MOUNT_CONFIGURE; Message to configure a camera mount, directional antenna, etc'

        elif messageID == 160:
            description = 'FENCE_POINT; A fence point'

        elif messageID == 163:
            description = 'AHRS; DCM状态'

        elif messageID == 165:
            description = 'HWSTATUS; 关键硬件状态'

        elif messageID == 166:
            description = 'RADIO; Status generated by radio'
            
        elif messageID == 178:
            description = 'AHRS2; secondary AHRS 姿态数据'

        elif messageID == 183:
            description = 'AUTOPILOT_VERSION_REQUEST; Request the autopilot version from the system/component'

        elif messageID == 185:
            description = 'REMOTE_LOG_BLOCK_STATUS; Send Status of each log block that autopilot board might have sent'

        # MESSAGE IDs 180 - 229: Space for custom messages in individual projectname_messages.xml files

        elif messageID == 191:
            description = 'MAG_CAL_PROGRESS; Reports progress of compass calibration'

        elif messageID == 192:
            description = 'MAG_CAL_REPORT; Reports results of completed compass calibration. Sent until MAG_CAL_ACK received'

        elif messageID == 193:
            description = 'EKF_STATUS_REPORT; EKF状态消息包括标志和方差'

        elif messageID == 215:
            description = 'GOPRO_HEARTBEAT; Heartbeat from a HeroBus attached GoPro'

        elif messageID == 232:
            description = 'GPS_INPUT; 传感器原始数值'

        elif messageID == 241:
            description = 'VIBRATION; 震动等级、加速度计clipping'

        elif messageID == 252:
            description = 'NAMED_VALUE_INT; timestamp key-value'

        elif messageID == 253:
            description = 'STATUSTEXT (状态文本消息); '

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

    
    
