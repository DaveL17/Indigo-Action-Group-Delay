# Indigo-Action-Group-Delay
# ![shield](https://img.shields.io/github/release/DaveL17/Indigo-Action-Group-Delay.svg) ![indigo-version](https://img.shields.io/badge/Indigo-7.0+-blueviolet.svg) ![indigo-version](https://img.shields.io/badge/Python-2.7-darkgreen.svg)

As of version 7.4, Indigo doesn't have a built-in method for setting 
a delay when executing an action group when using the Python command 
`indigo.actionGroup.execute(12345678)`. The purpose of this short 
script is to provide a shim that can serve as a proxy for delayed 
execution.

## Installation
Save file `actionGroupDelay.py` to a folder located within the Python 
search path. For example,  

`/Library/Python/2.7/site-packages/`

You may need to enter your administrator privileges depending on where
you choose to save the file.

## Usage
### Run directly (blocking)
```python
import actionGroupDelay as agd  
agd.runDelayedActionGroup(action_id=12345678, seconds=60)  
```

### Run in asynchronous mode (non-blocking)
```python
import threading  
import actionGroupDelay as agd  


t = threading.Thread(target=agd.runDelayedActionGroup, kwargs={'action_id': 1450401770, 'seconds': 5})  # Replace with your action id, time in seconds
t.start()
```

## Parameters
`action_id` Indigo ID for the Action Group  
`seconds` Second to delay before executing Action Group

## Output
If successful, the script will return `True` and provide a message 
`Action Group XXXXXXXX executed.`.  

If unsuccessful, it will return 
`False` and a brief error message where appropriate.