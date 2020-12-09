#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Indigo Action Group Delay
"""
import indigo
import threading
import time

__author__  = u"DaveL17"
__title__   = u"Indigo Action Group Delay"
__version__ = u"1.0"


def __init__(self):
    pass


def runDelayedActionGroup(action_id=None, seconds=60):
    """
    :param int action_id: Indigo action ID
    :param int seconds:  Time delay in seconds (default of 60)
    :return:
    """

    def run_delayed_action(a_id, s):
        time.sleep(s)
        indigo.actionGroup.execute(a_id)
        indigo.server.log(u"Action Group {0} executed.".format(a_id))

    try:
        if action_id not in indigo.actionGroups.keys():
            raise IndexError

        if not isinstance(seconds, int):
            raise ValueError

        t = threading.Thread(target=run_delayed_action, kwargs={'a_id': action_id, 's': seconds})
        t.start()

    except IndexError:
        indigo.server.log(u"Please provide a valid action group ID.")
        return False

    except ValueError:
        indigo.server.log(u"Please provide a valid delay value in seconds (integer).")
        return False
