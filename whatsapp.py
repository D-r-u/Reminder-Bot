import pywhatkit as kit
import pyautogui as pg
import time
def send_msg(ph,msg):
    try:
        kit.sendwhatmsg_instantly(phone_no=ph,message=msg,wait_time=18,tab_close=True,close_time=3)
        pg.press("enter")
    except:
        return 0
    else:
        # time.sleep(4)
        return 1

# print(send_msg("+917012336098","Hello")) # for testing this module