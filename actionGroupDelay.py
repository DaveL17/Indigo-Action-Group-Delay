#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Indigo Action Group Delay

Usage:
import actionGroupDelay as agd
agd.runDelayedActionGroup(action_id=12345678, seconds=60)
"""
import indigo
import sys
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
            time.sleep(seconds)
            indigo.actionGroup.execute(action_id)

        else:
            raise IndexError

        return True, u"Action Group {0} executed.".format(action_id)

    except IndexError:
        return False, u"Please provide a valid action group ID"

    except ValueError:
        return False, u"Please provide a valid delay value in seconds (integer)."
