# Indigo-Action-Group-Delay
# ![shield](https://img.shields.io/github/release/DaveL17/Indigo-Action-Group-Delay.svg) ![indigo-version](https://img.shields.io/badge/Indigo-7.0+-blueviolet.svg) ![indigo-version](https://img.shields.io/badge/Python-2.7-darkgreen.svg)

As of version 7.4, Indigo doesn't have a built-in method for setting 
a delay when executing an action group when calling the Python command 
`indigo.actionGroup.execute(12345678)`. The purpose of this short 
script is to provide a shim that can serve as a proxy for delayed 
execution.

### Installation
Save file `actionGroupDelay.py` to a folder located within the Python 
search path. For example,  

`/Library/Python/2.7/site-packages/`

You may need to enter your administrator privileges depending on where
you choose to save the file.

### Parameters
`action_id` Indigo ID for the Action Group  (required)  
`seconds` Seconds to delay before executing Action Group (optional, will default to 60)


### Usage
```python
from actionGroupDelay import runDelayedActionGroup

runDelayedActionGroup(1450401770, 5)
```

### Output
When run, the shim will create a separate process (thread) and 
execute the action group after the specified delay. When the
action group is executed, the script will write 
`Delayed Action Group XXXXXXXX executed` to the Indigo events log.
