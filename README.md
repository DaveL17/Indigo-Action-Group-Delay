# Indigo-Action-Group-Delay
# ![shield](https://img.shields.io/github/release/DaveL17/Indigo-Action-Group-Delay.svg) ![indigo-version](https://img.shields.io/badge/Indigo-7.0+-blueviolet.svg) ![indigo-version](https://img.shields.io/badge/Python-2.7-darkgreen.svg)

## Installation
Save file `actionGroupDelay.py` to a folder located within the Python 
search path. For example,  

`/Library/Python/2.7/site-packages/`

You may need to enter your administrator privileges depending on where
you choose to save the file.

## Usage
### Run directly
```python
import actionGroupDelay as agd  
agd.runDelayedActionGroup(action_id=12345678, seconds=60)  
```

### Run in asynchronous mode (non-blocking)
```python
import threading  
import actionGroupDelay as agd  


t = threading.Thread(target=agd.runDelayedActionGroup, args=[1450401770, 5])  # Replace with your action id, time in seconds    
t.start()```

## Parameters
`action_id` Indigo ID for the Action Group  
`seconds` Second to delay before running Action Group

