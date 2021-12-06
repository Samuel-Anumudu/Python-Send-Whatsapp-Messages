import datetime
import keyboard
import pywhatkit
import pyautogui
import time


def send_message(list_of_number):
    try:
        current_datetime = datetime.datetime.now()
        hour = current_datetime.hour
        minute = current_datetime.minute
        for num in list_of_number:
            pywhatkit.sendwhatmsg(num, "Hello there!\n Thank you for showing interest in the spoken word / poetry "
                                       "performance category "
                                       "for the Gala Event. In order for us to assess your candidacy for the event, "
                                       "please send us a video of any of your poetry and spoken word."
                                       "This is an important step and once completed we will get back to "
                                       "you.\nWe will be looking forward to your video", hour, minute + 2, 10)
            minute += 2
            pyautogui.click(1050, 950)
            time.sleep(2)
            keyboard.press_and_release('enter')
            print("Your message has been sent successfully!")

    except:
        print("An Unexpected Error!")


numbers = ["+12345678910", "+10987654321"]
send_message(numbers)
