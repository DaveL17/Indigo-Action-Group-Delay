# Indigo-Action-Group-Delay
# ![shield](https://img.shields.io/github/release/DaveL17/Indigo-Action-Group-Delay.svg) ![indigo-version](https://img.shields.io/badge/Indigo-2022.1+-blueviolet.svg) ![indigo-version](https://img.shields.io/badge/Python-3.10-darkgreen.svg)

As of version 2022.1, Indigo doesn't have a built-in method for setting 
a delay when executing an action group when calling the Python command 
`indigo.actionGroup.execute(12345678)`. The purpose of this short 
script is to provide a shim that can serve as a proxy for delayed 
execution. The shim runs independently--using it will not stop the 
rest of your script from continuing.

### Installation
Save file `action_group_delay.py` to a folder located within the Python 
search path. For example:  

`/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/action_group_delay.py`

You may need to enter your administrator privileges depending on where
you choose to save the file.

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
When run, the shim will create a separate process (thread) and 
execute the chosen action group after the specified delay. When the
action group is executed, the script will write 
`Delayed action group 12345678 executed.` to the Indigo events log.
