# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


import time
from machine import Pin, I2C
from micropython_sht20 import sht20


i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht20.SHT20(i2c)

while True:
    print(f"Temperature: {sht.temperature:.2f}°C")
    print(f"Humidity: {sht.humidity:.2%}%")
    print("")
    time.sleep(1)
