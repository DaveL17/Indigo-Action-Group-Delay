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
__version__ = "1.4"


def __init__():
    pass


def run_delayed_action_group(action_id=None, seconds=60):
    """
    :param int action_id: Indigo action ID
    :param int seconds:  Time delay in seconds (default of 60)
    :return:
    """

    def run_delayed_action(a_id, secs):
        indigo.activePlugin.sleep(secs)
        indigo.actionGroup.execute(a_id)
        indigo.server.log(f"Delayed action group {a_id} executed.")

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

        delayed_action_thread = threading.Thread(
            group=None,
            target=run_delayed_action,
            name=None,
            args={},
            kwargs={'a_id': action_id, 'secs': seconds}
        )
        delayed_action_thread.daemon = True
        indigo.activePlugin.sleep(.25)  # Take a short heartbeat to ensure the command got sent
        delayed_action_thread.start()

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
