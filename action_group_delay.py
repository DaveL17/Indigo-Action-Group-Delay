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


def __init__(self):
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

        t = threading.Thread(
            group=None,
            target=run_delayed_action,
            name=None,
            args={},
            kwargs={'a_id': action_id, 's': seconds}
        )
        t.daemon = True
        indigo.activePlugin.sleep(.25)  # Take a short heartbeat to ensure the command got sent
        t.start()

    except IndexError:
        raise ActionGroupDelayError("Please provide a valid action group ID.")

    except ValueError:
        raise ActionGroupDelayError("Please provide a valid delay value in seconds (integer).")


class ActionGroupDelayError(Exception):
    pass
