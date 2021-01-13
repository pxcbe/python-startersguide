# Getting acces to the PLCnext variables

You can use the REST service component to get acces to the PLCnext variables. AlexanderSkachkov wrote a great python library that will make the communication very easy.
Before we can use the library we need to install it on our controller. Follow the insctructions for the installation of the PIP3 in the setup directory before going further.


# Installing the library

Use PIP to install the library:
```
pip3 install pyPLCn
```

# Modify the script

Change the ip adress on line 8 of the rest_api.py file to match the ip adress of your controller.
Execute the next command

```
python3 rest_api.py
```

If all goes well, you should see the variables printing in your shell with the specified polling interval!
