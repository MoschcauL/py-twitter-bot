# -*- coding: utf-8 -*-
"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone
# import mac address
from uuid import getnode as macaddress

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "hi" in message.lower():
        berlin_time = datetime.now(timezone('Europe/Berlin'))
        date = berlin_time.strftime("It is %H:%M:%S on a %A.")
        return "Hi @" + user + "! " + date + "\nfrom " + macaddress()
    return None

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (280 chars max)
    values = sysvalues()
    text = "Hi, I am " + ("%0.2X" % macaddress()) + "!\nMy body temperature is " + str(values[0]) + "°C, fueled with " + "{:.0f}".format(values[1] * 100) + "%" + (" and I still can't get enough" if values[2] else "") + "! Also I'm shining at around " + "{:.1f}".format(values[3] * 100) + "%." 
    return text

def sysvalues():
    temperature = int(open('/sys/bus/platform/devices/coretemp.0/hwmon/hwmon1/temp1_input', 'r').read()) / 1000
    capacity = float(open('/sys/class/power_supply/BAT0/capacity', 'r').read()) / 100
    power = bool(int(open('/sys/class/power_supply/AC0/online', 'r').read()))
    brightness = float(open('/sys/class/backlight/intel_backlight/brightness', 'r').read()) / int(open('/sys/class/backlight/intel_backlight/max_brightness', 'r').read())

    return (temperature, capacity, power, brightness)
