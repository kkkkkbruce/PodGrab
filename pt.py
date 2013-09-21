#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  pt.py
#
#  Copyright 2013  <kkkkkbruce>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import os
import datetime


def play_today():
    """looks for <todays date>.m3u and plays it with mpg321
    a companion program to PodGrab.py"""
    today = datetime.datetime.now()
    print('Todays date is: ' + str(today.date()))
    playlistfile = "/home/pi/" + str(today.date()) + ".m3u"
    print('Looking for: ' + playlistfile)
    if os.path.exists(playlistfile):
        print('file exists')
        os.system('mpg321 -K -@ ' + playlistfile)
        os.system('mv ' + playlistfile + ' ' + playlistfile + '.done')
    else:
        print('Sorry, no podcasts to play at the moment')
    return 0

if __name__ == '__main__':
    play_today()

