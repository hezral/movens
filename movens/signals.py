#!/usr/bin/env python3

'''
   Copyright 2020 Adi Hezral (hezral@gmail.com) (https://github.com/hezral)

   This file is part of Movens.

    Movens is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Movens is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Movens.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
from gi.repository import GObject

class MyObject(GObject.GObject):
    __gsignals__ = {
        'adi': (GObject.SIGNAL_RUN_FIRST, None, (int,))
    }

    #@GObject.Signal(name='adi', flags=GObject.SignalFlags.RUN_FIRST, return_type=None, arg_types=None, accumulator=None, accu_data=None)
    def test(self, *args):
        print("Handler", args)

    # def do_adi(self):
    #     print("method handler for `my_signal' called with argument")


myobj = MyObject()

myobj.emit("adi", 2) # emit the signal "my_signal", with the
                             # argument 42


print(type(myobj))

# print(dir(myobj))

myobj = MyObject()

myobj.emit("adi", 2) # emit the signal "my_signal", with the
                             # argument 42


