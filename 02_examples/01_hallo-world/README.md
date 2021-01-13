# Pyhton and the interpreter

Python does not get compiled, or at least not in the traditonal sense. Most of the time you won't be transfering binaries to the PLC but a script, a .py file to the controller.
In this direcorty you can find two python scripts. HelloWold.py and HelloWorld_Shebang.py. They share the same code but will differ in how you can execute or run the scripts.

## HelloWorld

You can execute the HelloWorld script with the following command.

```
python3 HelloWorld.py
```

Can you see the message promted in the shell?
You can do the same with HelloWorld_SheBang.py

## Shebang (shabang)
Try running:

```
./HelloWorld.py
```
and 
```
./HelloWorld_SheBang.py
```
You'll find that HelloWorld.py doesn't work and HelloWorld_SheBang.py does. Why is this?
On the first line of the HelloWorld_SheBang.py there is an extra statement, this statement is called a Shebang and this tells the operating system it is a python script. It performs the same function as the "python3" statement needed for the HelloWorld.py script

```
#!/usr/bin/python3
```
