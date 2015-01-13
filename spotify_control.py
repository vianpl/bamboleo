#!/usr/bin/env python

import dbus
import sys

class SpotifyControl:

    def __init__(self):
        self.session = dbus.SessionBus.get_session()
        self.spotify = self.session.get_object(
                "org.mpris.MediaPlayer2.spotify",
                "/org/mpris/MediaPlayer2")
    def playpause(self):
        self.spotify.PlayPause()

