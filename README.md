# Indigo-Action-Group-Delay
# ![shield](https://img.shields.io/github/release/DaveL17/Indigo-Action-Group-Delay.svg) ![indigo-version](https://img.shields.io/badge/Indigo-2022.1+-blueviolet.svg) ![indigo-version](https://img.shields.io/badge/Python-3.10-darkgreen.svg)

Up to version 2022.1, Indigo doesn't have a built-in method for setting a delay when executing an action group when 
calling the Python command `indigo.actionGroup.execute(12345678)`. The purpose of this short script is to provide a 
shim that can serve as a proxy for delayed execution. The shim runs independently--using it will not stop the rest of 
your script from continuing.

### Installation
Save file `action_group_delay.py` to a folder located within the Python search path. For example:  

`/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/action_group_delay.py`

You may need to enter your administrator privileges depending on whereyou choose to save the file.

### Parameters
`action_id` Indigo ID for the Action Group to be executed (required; integer)  
`seconds` Seconds to delay before executing the Action Group (optional, will default to 60; integer)

### Examples

```python
from action_group_delay import run_delayed_action_group

run_delayed_action_group(action_id=12345678, seconds=5)
```
or

```python
from action_group_delay import run_delayed_action_group

run_delayed_action_group(12345678, 5)
```
or

```python
import action_group_delay

action_group_delay.run_delayed_action_group(12345678, 5)
```

or

```python
import action_group_delay

action_group_delay.run_delayed_action_group(12345678)  # will execute in 60 seconds
```

### Output
When run, the shim will create a separate process (thread) and execute the chosen action group after the specified 
delay. When the action group is executed, the script will write `Delayed action group 12345678 executed.` to the 
Indigo events log.

> [!NOTE]
> If used in an embedded script, the action group delay time can exceed Indigo's 10-second limitation -- the delayed 
action will still fire.  ***HOWEVER***, if the embedded script times out for another reason, the Indigo Host will 
kill the embedded script (and the delayed action along with it). Therefore, if you need to use the `Action Group Delay` shim with a script that could take longer than 10-seconds to execute, it's  recommended to use a linked script 
instead (which isn't subject to the 10-second limitation).
