# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: MIT
"""
`async_buzzer`
================================================================================

Play simple tunes on a piezo buzzer asynchronously


* Author(s): Phil Underwood

Implementation Notes
--------------------

**Hardware:**

* This works with passive piezo transducers.

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""
try:
    from typing import Optional, Union, Tuple, Sequence, Deque, NamedTuple, List
    import pwmio
except ImportError:
    pass

import asyncio
from collections import namedtuple


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/furbrain/CircuitPython_async_buzzer.git"


Note = namedtuple("Note", ("freq", "duration"))


class Buzzer:
    """
    Async implementation of a buzzer that can play simple tunes
    """
    NOTES = {
        'C2': 65,
        'C#2': 69,
        'D2': 73,
        'D#2': 78,
        'E2': 82,
        'F2': 87,
        'F#2': 92,
        'G2': 98,
        'G#2': 104,
        'A2': 110,
        'A#2': 117,
        'B2': 123,
        'C3': 131,
        'C#3': 139,
        'D3': 147,
        'D#3': 156,
        'E3': 165,
        'F3': 175,
        'F#3': 185,
        'G3': 196,
        'G#3': 208,
        'A3': 220,
        'A#3': 233,
        'B3': 247,
        'C4': 262,
        'C#4': 277,
        'D4': 294,
        'D#4': 311,
        'E4': 330,
        'F4': 349,
        'F#4': 370,
        'G4': 392,
        'G#4': 415,
        'A4': 440,
        'A#4': 466,
        'B4': 494,
        'C5': 523,
        'C#5': 554,
        'D5': 587,
        'D#5': 622,
        'E5': 659,
        'F5': 698,
        'F#5': 740,
        'G5': 784,
        'G#5': 831,
        'A5': 880,
        'A#5': 932,
        'B5': 988,
        'C6': 1047,
        'C#6': 1109,
        'D6': 1175,
        'D#6': 1245,
        'E6': 1319,
        'F6': 1397,
        'F#6': 1480,
        'G6': 1568,
        'G#6': 1661,
        'A6': 1760,
        'A#6': 1865,
        'B6': 1976,
        'C7': 2093,
        'C#7': 2217,
        'D7': 2349,
        'D#7': 2489,
        'E7': 2637,
        'F7': 2794,
        'F#7': 2960,
        'G7': 3136,
        'G#7': 3322,
        'A7': 3520,
        'A#7': 3729,
        'B7': 3951,
        'C8': 4186,
    }

    def __init__(self, pwm: pwmio.PWMOut):
        """

        :param ~pwmio.PWMOut pwm: pwm to use for output
        """
        self.pwm = pwm
        self.playing_task: Optional[asyncio.Task] = None
        self.notes: Optional[List[Note]] = None

    async def _worker(self):
        self.pwm.duty_cycle = 0x7fff
        for frequency, duration in self.notes:
            self.pwm.frequency = frequency
            await asyncio.sleep(duration/1000)
        self.pwm.duty_cycle = 0

    def play(self, notes: Sequence[Tuple[Union[str,float], float]],
                   wait: bool=False):
        """
        Start playing a series of notes

        :param list notes: A sequence of tuples of frequency and duration (in ms). Frequency can
          also be specified as a note string e.g "C#6". Note for reasons of space only notes
          between C2 and C8 can be referenced by name, but any numeric frequency can be used.
          What frequencies actually work will depend on your transducer.
        :param bool wait: If True, wait until sequence has finished or been
        :return:
        """
        self.stop() # stop any current playing tune.
        self.notes = []
        for note, duration in notes:
            if isinstance(note, str):
                freq = self.NOTES[note]
            else:
                freq = note
            self.notes.append(Note(freq, duration))
        self.playing_task = asyncio.create_task(self._worker())

    async def wait(self):
        """
        Wait for the current tune to finish. This may finish early if a new tune is played
        """
        if self.playing_task is not None:
            try:
                await self.playing_task
            except asyncio.CancelledError:
                pass

    def stop(self):
        """
        Stop playing
        """
        if self.playing_task is not None:
            if not self.playing_task.done():
                self.playing_task.cancel()
        self.playing_task = None
        self.pwm.duty_cycle = 0
