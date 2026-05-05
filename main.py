import RPi.GPIO as GPIO 
import time


def interval_led():
    """
    间隔点亮led
    """
     # 引脚BOADpin数字
    channel = 36
    
    # 获得编码方式
    mode = GPIO.getmode()
    print(f"Pin mode:{mode}")
    
    # 设置引脚编码模式
    GPIO.setmode(GPIO.BOARD)
    mode = GPIO.getmode()
    print(f"Pin mode: {mode}")
    
    # 设置指定引脚为输出模式
    GPIO.setup(channel, 0, initial=0)  
    # 或
    # GPIO.setup(36, GPIO.OUT)
    
    # 间隔点亮LED灯
    while True:
        
        # 点亮
        GPIO.output(channel, 1) # 点
        # 停留
        time.sleep(1)           # 线： 单位s  
        
        # 熄灭
        GPIO.output(channel, 0)
        # 持续
        time.sleep(1)


def led_continue(led_continus_time: int | float = 0.5 ,leds_channel: list | int = [40, 38 , 36]):
    """
    依次led点亮循环
    """
    
    # 设置引脚输入输出模式: 0代表输出模式 或GPIO.OUTPUT
    led_modes = [ (channel,GPIO.setup(channel, 0)) for channel in leds_channel]
    
    # 统一输出置0
    led_set_0 = [( channel, GPIO.output(channel, 0)) for  channel in leds_channel]
        
    # 点亮算法
    while True:
        for channel in leds_channel:
            # 选中channel状态设置输出为1
            GPIO.output(channel, 1)
            
            # 持续点亮时间
            time.sleep(led_continus_time)
            
            # 重置输出为0
            GPIO.output(channel, 0)
        

def pin_in():
    """
    pin引脚输入测试
    """
    #定义引脚
    channel = 40
    
    #设置对应引脚为输入模式: 悬浮引脚默认输入电平为随机的电平，需要在未连接时通过上下拉电阻设置为默认电平，上拉为高电平3.3v  下拉为低电平0v
    GPIO.setup(channel, 1, pull_up_down=GPIO.PUD_DOWN)
    
    while True:
        time.sleep(1)
        # 获取输入电平
        v = GPIO.input(channel)
        print(f"channel = {channel} v={v}")
        
    
if  __name__ == "__main__":
    
    # 设置引脚编码模式
    GPIO.setmode(GPIO.BOARD)
    
    # 间隔点亮led
    # interval_led()
    
    # 循环led灯连续点亮
    # led_continue(led_continus_time=0.05,leds_channel=[40, 38 , 36])
    
    # 引脚输入测试
    pin_in()
    
   
        
        
    
    