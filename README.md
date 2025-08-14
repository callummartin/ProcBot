# ProcBot
An automation tool written in Python based on Selenium. Simply provide a .proc file with instructions for the bot to complete. 

# Requirements 
You will need to have both [Python](https://www.python.org/downloads/) and [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/) installed on the machine before this tooling can be used. 

# Installation
Download the latest version of the `browser_engine.py` file either from source, or via package. 

# Example
Once the browser engine is available, simply import the module and then execute from a procedure file. 

```python
from browser_engine import * 
exec_proc_from_file("lorem.proc")
```

# Process Language (.proc)

The browser engine expects a process to be provided in the form of a `.proc` file. You simply invoke the engine, and define which processes should be executed. 

# General Syntax 

Each line of the `.proc` file is read sequentially and converted into Python, which will be executed via the browser engine. Each line can contain one command, the syntax and usage of which can be referenced below. 

```
// This is a comment line and will be ignored. 
```

> [!TIP]
> Empty lines will be ignored by the interpreter. 

# Commands

The Process Language supports the following commands: 
    
* `var` sets a variable. 
* `start` starts a new browser instance.
* `stop` quits the current browser instance with confirmation.
* `goto` navigates to a URL.
* `wait` pauses the process for a given number of seconds. 
* `quit` immediately quits the current browser instance.
* `confirm` gets confirmation from user.
* `gi` finds an element matching an ID.
* `gn` finds an element matching a name. 
* `gc` finds elements matching a class. 
* `gs` finds elements matching a CSS selector statement. 
* `gx` finds an element matching an XPATH string. 

# start

**Description**  
The `start` command invokes a new instance of a browser using Selenium. 

**Syntax**
```
start <browser_name>
```

# stop

**Description**  
The `stop` command quits the current instance of a browser using Selenium. 

**Syntax**
```
stop <browser_name>
```

**Example**
```
// Stops Chrome 
stop Chrome
```

# wait

**Description**  
The `wait` command pauses the process for a given number of seconds. 

**Syntax**
```
wait <seconds>
```

**Example**
```
// Waits for 1.5 seconds. 
wait 1.5
```

# quit

**Description**  
The `quit` command immediately terminates the current browser session. 

**Syntax**
```
quit
```

**Example**
```
// Quits browser process.
quit
```

# confirm

**Description**  
The `confirm` command allows you to define a custom confirm message in the terminal. 

**Syntax**
```
confirm <message>
```

**Example**
```
// Generic enter to continue message 
confirm "Press enter to continue..."
```

# gi
**Description**  
The `gi` command finds an element matching an ID. 

**Syntax**
```
gi <return_reference> <element_ID>
```

**Example**
```
// Finds an element on the current page with the ID "lorem"
gi lorem_element lorem
```

# gn
**Description**  
The `gn` command finds an element matching a name. 

**Syntax**
```
gn <return_reference> <element_name>
```

**Example**
```
// Finds an element on the current page with the name "lorem"
gn lorem_element lorem
```

# gc
**Description**  
The `gc` command finds elements with a given class. 

**Syntax**
```
gc <return_reference> <element_class>
```

**Example**
```
// Finds an element on the current page with the class "lorem"
gc lorem_element lorem
```

# gs
**Description**  
The `gs` command finds elements with a given CSS selector statement. 

**Syntax**
```
gs <return_reference> <element_selector>
```

**Example**
```
// Drills into the content class, finds the 56th paragraph and gets the first strong tag. 
gs ".content > p:nth-child(56) > strong:nth-child(1)"
```

# gx
**Description**  
The `gx` command finds elements with a given XPATH. 

**Syntax**
```
gx <return_reference> <element_xpath>
```

**Example**
```
// Fetches an element based on an example XPATH. 
gx lorem_element /html/body/main/div[6]/div/div[2]/div/div[2]/div[2]/div[1]/div/p[29]
```

# var

**Description**  
The `var` command initialises a new variable and assigns it a value. These variables can be used multiple times to remove the need for repetition. 

**Syntax**
```
var <variable_name> <variable_value>
```

**Example**
```
// Declares and initialises a variable called test_uri.
var test_uri "https://lorem.ipsum/dolor"

// Starts Chrome. 
start Chrome 

// Navigates Chrome to the variable value (lorem site).
goto [var]test_uri
```