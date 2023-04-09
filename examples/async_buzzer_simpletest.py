# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: Unlicense
import asyncio
import board
import pwmio

from async_buzzer import Buzzer

tune = [
    ("E5", 500),
    ("G5", 500),
    ("A5", 1000),
    ("E5", 500),
    ("G5", 500),
    ("B5", 250),
    ("A5", 750),
    ("E5", 500),
    ("G5", 500),
    ("A5", 1000),
    ("G5", 500),
    ("E5", 1500),
]

pwm = pwmio.PWMOut(board.D10, variable_frequency=True)
buzzer = Buzzer(pwm)


async def main():
    buzzer.play(tune, wait=False)
    for i in range(5):
        print(i)
        await asyncio.sleep(1)
    await buzzer.wait()


asyncio.run(main())
