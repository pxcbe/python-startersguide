# Python and the OPC UA server

Every PLCnext controller has an embedded  OPC UA server. This server can be used to interchange variables between your Pythonscript and PLCnext Engineer program.
This is a bit harder to do then the previous example witch used the REST interface but this effort will pay you back when setting up a bigger python application.

# Installation
Unfortuniltly, it's not easy to install the nessesary packages on the PLCnext controller with PIP.
I recomend developing the application on an other Linux machine for example an Ubuntu 20.04 virtual machine, this ofcourse has the added benefit of being able to use the IDE of your chose.
I'm using Visual Studio Code but you can try any other IDE or even just your notepad.

Follow the steps to install Python3 and pip3 for your machine. When ready you can check the install with the next commands:

```
Python3 --version
pip3 --version
```

# Running the script

Change the IP adress, username and password to fit the settings of your controller. You can find these settings on line 27,28,29.
Execute the next command:

```
python3 plcnext.py
```

If this works, you should see the variables printing in the screen!
