#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Indigo Action Group Delay
"""
import threading
try:
    import indigo
except ImportError:
    pass

__author__  = "DaveL17"
__title__   = "Indigo Action Group Delay"
__version__ = "1.5"


def __init__():
    pass


def run_delayed_action_group(action_id=None, seconds=60):
    """
    :param int action_id: Indigo action ID
    :param int seconds:  Time delay in seconds (default of 60)
    :return:
    """

    def run_delayed_action(a_id):
        indigo.actionGroup.execute(a_id)
        indigo.server.log(f"Delayed action group {a_id} executed.")

    try:

        # action_id not recognized by Indigo
        if not action_id or action_id not in indigo.actionGroups.keys():
            raise IndexError

        # seconds not float or integer
        if not isinstance(seconds, (float, int)):
            raise ValueError

        threading.Timer(seconds, run_delayed_action, args=[action_id]).start()
        indigo.activePlugin.sleep(.25)  # Take a short heartbeat to ensure the command got sent

    except IndexError:
        msg = "Invalid action ID."
        raise ActionGroupDelayError(msg) from IndexError

    except ValueError:
        msg = "Delay time not an integer."
        raise ActionGroupDelayError(msg) from ValueError


class ActionGroupDelayError(Exception):
    """
    ActionGroupDelayError Custom Exception Class
    """
