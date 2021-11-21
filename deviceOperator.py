from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
# 音量0-100对应机器获取音量值
numToDev = {
    100:0,
    95:-0.7687,
    90:-1.578,
    85:-2.4337,
    80:-3.3399,
    75:-4.3037,
    70:-5.3327,
    65:-6.4365,
    60:-7.6268,
    55:-8.9182,
    50:-10.3297,
    45:-11.8857,
    40:-13.6194,
    35:-15.5766,
    30:-17.8235,
    25:-20.4612,
    20:-23.6548,
    15:-27.7028,
    10:-33.2365,
    5:-42.0267,
    0:-65.25,
}

class DeviceOpreator:
    def __init__(self):
        self.audioDevice = AudioUtilities.GetSpeakers()
        self.interface = self.audioDevice.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

    def is_mute(self):
        mute = self.volume.GetMute()
        return mute

    def get_volume(self):
        # 获取音量值，0.0代表最大，-65.25代表最小
        vl = self.volume.GetMasterVolumeLevel()
        return vl
    def set_volume(self,num):
        devNum = self.num_conv_dev(num)
        self.volume.SetMasterVolumeLevel(devNum,None)
    def num_conv_dev(self,num):
        #devNum = ((-1e-7)*(num**5)+(3e-5)*(num**4)-0.0035*(num**3)+0.1795*(num**2)-4.5843*num+65.25)
        #devNum = 5e-6*num**4-0.0012*num**3+0.0991*num**2-3.7063*num+65.25
        #devNum = -0.0002*num**3+0.0438*num**2-2.7654*num+65.25
        # 输入值不合法默认30
        if num<0 or num>100:
            num=30
        remainder = num%5
        # 不在预制中的数选择比起小的最接近的值
        if remainder!=0:
            num = int(num/5)*5
        return numToDev[num]
    def shut_down(self):
        os.system('shutdown -s -f -t 59')
if __name__ == '__main__':
    dev = DeviceOpreator()
    print(dev.get_volume())
    dev.set_volume(30)
    print(dev.get_volume())
