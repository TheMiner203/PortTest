import os, sys, io
import M5
from M5 import *
from hardware import *
import time



G25 = None
G32 = None
G33 = None
G26_text = None
G25_text = None
G0Warning = None
G26 = None
G32_text = None
G33_text = None
Testmode = None
pin26 = None
pin25 = None
pin32 = None
pin33 = None


def btnA_wasClicked_event(state):
  global G25, G32, G33, G26_text, G25_text, G0Warning, G26, G32_text, G33_text, Testmode, pin26, pin25, pin32, pin33
  pass

def setup():
  global G25, G32, G33, G26_text, G25_text, G0Warning, G26, G32_text, G33_text, Testmode, pin26, pin25, pin32, pin33

  M5.begin()
  Widgets.fillScreen(0x2e2e2e)
  G25 = Widgets.Circle(30, 70, 15, 0xffffff, 0xffffff)
  G32 = Widgets.Circle(30, 110, 15, 0xffffff, 0xffffff)
  G33 = Widgets.Circle(30, 150, 15, 0xffffff, 0xffffff)
  G26_text = Widgets.Label("G26", 55, 20, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu18)
  G25_text = Widgets.Label("G25", 55, 60, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu18)
  G0Warning = Widgets.Label("G0 is unable to test", 10, 225, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu9)
  G26 = Widgets.Circle(30, 30, 15, 0xffffff, 0xffffff)
  G32_text = Widgets.Label("G32", 55, 100, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu18)
  G33_text = Widgets.Label("G33", 55, 140, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu18)
  Testmode = Widgets.Label("Auto: 3.3v", 19, 184, 1.0, 0xffffff, 0x2e2e2e, Widgets.FONTS.DejaVu18)

  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_CLICKED, cb=btnA_wasClicked_event)

  pin26 = Pin(26, mode=Pin.IN, pull=Pin.PULL_UP)
  pin25 = Pin(25, mode=Pin.IN, pull=Pin.PULL_UP)
  pin32 = Pin(32, mode=Pin.IN, pull=Pin.PULL_UP)
  pin33 = Pin(33, mode=Pin.IN, pull=Pin.PULL_UP)
  time.sleep(1.5)
  Testmode.setText(str('Auto: 3.3v'))
  if (pin26.value()) == 1:
    G26.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G26.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin25.value()) == 1:
    G25.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G25.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin32.value()) == 1:
    G32.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G32.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin33.value()) == 1:
    G33.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G33.setColor(color=0xcccccc, fill_c=0xFF0000)
  time.sleep(3)
  Testmode.setText(str('Auto: GND'))
  pin26 = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin25 = Pin(25, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin32 = Pin(32, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin33 = Pin(33, mode=Pin.IN, pull=Pin.PULL_DOWN)
  G26.setColor(color=0xFFFFFF, fill_c=0xFFFFFF)
  G25.setColor(color=0xFFFFFF, fill_c=0xFFFFFF)
  G32.setColor(color=0xFFFFFF, fill_c=0xFFFFFF)
  G33.setColor(color=0xFFFFFF, fill_c=0xFFFFFF)
  time.sleep(1.5)
  if (pin26.value()) == 0:
    G26.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G26.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin25.value()) == 0:
    G25.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G25.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin32.value()) == 0:
    G32.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G32.setColor(color=0xcccccc, fill_c=0xFF0000)
  if (pin33.value()) == 0:
    G33.setColor(color=0xcccccc, fill_c=0x33ff33)
  else: 
    G33.setColor(color=0xcccccc, fill_c=0xFF0000)
  time.sleep(3)
  pin26 = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin25 = Pin(25, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin32 = Pin(32, mode=Pin.IN, pull=Pin.PULL_DOWN)
  pin33 = Pin(33, mode=Pin.IN, pull=Pin.PULL_DOWN)
  Testmode.setText(str('  Manual'))
  while True:
    if pin26.value() == 1:
        G26.setColor(color=0xcccccc, fill_c=0x33ff33)
    else:
        G26.setColor(color=0xcccccc, fill_c=0xFF0000)
    if pin25.value() == 1:
        G25.setColor(color=0xcccccc, fill_c=0x33ff33)
    else:
        G25.setColor(color=0xcccccc, fill_c=0xFF0000) 
    if pin32.value() == 1:
        G32.setColor(color=0xcccccc, fill_c=0x33ff33)
    else:
        G32.setColor(color=0xcccccc, fill_c=0xFF0000)
    if pin33.value() == 1:
        G33.setColor(color=0xcccccc, fill_c=0x33ff33)
    else:
        G33.setColor(color=0xcccccc, fill_c=0xFF0000)
    time.sleep(0.05)




def loop():
  global G25, G32, G33, G26_text, G25_text, G0Warning, G26, G32_text, G33_text, Testmode, pin26, pin25, pin32, pin33
  M5.update()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
