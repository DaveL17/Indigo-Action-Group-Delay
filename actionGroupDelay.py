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
__version__ = u"1.1"


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
        indigo.server.log(u"Delayed action group {0} executed.".format(a_id))

    try:

        if not action_id:
            raise IndexError

        if action_id not in indigo.actionGroups.keys():
            raise IndexError

        if not isinstance(seconds, int):
            raise ValueError

        t = threading.Thread(target=run_delayed_action, kwargs={'a_id': action_id, 's': seconds})
        t.start()

    except IndexError:
        raise actionGroupDelayError(u"Please provide a valid action group ID.")

    except ValueError:
        raise actionGroupDelayError(u"Please provide a valid delay value in seconds (integer).")


class actionGroupDelayError(Exception):
    pass

