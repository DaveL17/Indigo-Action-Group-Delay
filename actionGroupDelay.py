#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Indigo Action Group Delay
"""
import indigo
import threading

__author__  = u"DaveL17"
__title__   = u"Indigo Action Group Delay"
__version__ = u"1.3"


def __init__(self):
    pass


def runDelayedActionGroup(action_id=None, seconds=60):
    """
    :param int action_id: Indigo action ID
    :param int seconds:  Time delay in seconds (default of 60)
    :return:
    """

    def run_delayed_action(a_id, s):
        indigo.activePlugin.sleep(s)
        indigo.actionGroup.execute(a_id)
        indigo.server.log(u"Delayed action group {0} executed.".format(a_id))

    try:

        # action_id is None
        if not action_id:
            raise IndexError

        # action_id not recognized by Indigo
        if action_id not in indigo.actionGroups.keys():
            raise IndexError

        # seconds not integer
        if not isinstance(seconds, int):
            raise ValueError

        t = threading.Thread(group=None,
                             target=run_delayed_action,
                             name=None,
                             args={},
                             kwargs={'a_id': action_id, 's': seconds}
                             )
        t.start()

    except IndexError:
        raise ActionGroupDelayError(u"Please provide a valid action group ID.")

    except ValueError:
        raise ActionGroupDelayError(u"Please provide a valid delay value in seconds (integer).")


class ActionGroupDelayError(Exception):
    pass
