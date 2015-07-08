pyAIML
======

**NOTE: This repo has been cloned from sourceforge. Credits follow.**

PyAIML -- The Python AIML Interpreter

author: Cort Stratton (cort@users.sourceforge.net)
web: http://pyaiml.sourceforge.net/

PyAIML is an interpreter for AIML (the Artificial Intelligence Markup
Language), implemented entirely in standard Python.  It strives for
simple, austere, 100% compliance with the AIML 1.0.1 standard, no less
and no more.

This is currently pre-alpha software.  Use at your
own risk!

For information on what's new in this version, see the
CHANGES.txt file.

For information on the state of development, including 
the current level of AIML 1.0.1 compliance, see the
SUPPORTED_TAGS.txt file.

Quick & dirty example (assuming you've downloaded the
"standard" AIML set):

```python
import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("std-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")

# Loop forever, reading user input from the command
# line and printing responses.
while True: print k.respond(raw_input("> "))
```


To INSTALL
----------

    1. clone this repo inside site-package directory.
	2. modify all path file std-startup.xml 
	3. modify path at start-aiml.py


	
HELPER
------
     help2line.py is a helper for formatting AIML for 2 lines 
	 conversation lines
	 save all line in peribahasa.txt
	 then run the helper.
	 
    
REMEMBER
--------

   -- inside :pattern: tag -> MUST CAPITAL
   
   
FLASHCHAT BOT
-------------
   please use irzflashbot.swf upload to make a flashbot
   html code included

