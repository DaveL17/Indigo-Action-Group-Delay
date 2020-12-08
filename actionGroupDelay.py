#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Indigo Action Group Delay

Usage:
import actionGroupDelay as agd
agd.runDelayedActionGroup(action_id=12345678, seconds=60)
"""
import indigo
import time

__author__  = u"DaveL17"
__title__   = u"Indigo Action Group Delay"
__version__ = u"1.0"


def __init__(self):
    pass


def runDelayedActionGroup(action_id=None, seconds=60):

    try:
        seconds = int(seconds)

        if action_id:
            indigo.server.log(u"Running Action Group {id} with delay of {sec} seconds.".format(id=action_id, sec=seconds))
            time.sleep(seconds)
            indigo.actionGroup.execute(action_id)
            indigo.server.log(u"Action Group {0} executed.".format(action_id))

        else:
            raise IndexError

        return True

    except IndexError:
        indigo.server.log(u"Invalid Action Group ID provided.", isError=True)
        return False

    except ValueError:
        indigo.server.log(u"Invalid time delay provided.", isError=True)
        return False
