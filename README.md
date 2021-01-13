# Python-Startersguide

This guide is meant to learn you the basics for Python on PLCnext. We'll learn how to run your Python code, build applications that can acces the data-variables from our PLCnext Engineer project. We can acces the variables in two ways, each with their own advantages and disadvantages. The REST interface can be considerd less cumbersome to set for a few variables. Accessing the variables on the OPC UA server is a bit more difficult to set up but supports a lot more functions.

## Prerequisites

- For this guide you'll need at least a minimal expierence with PLCnext Engineer, PLCnext and Python.
- Please have a AXC F 2152 with firmware 2021.0 LTS with an internet connection ready
- Please download the provided PLCnext Project to your PLCnext controller

## Setup script

We'll use a few different compontents on the controller, you can use installation scripts in this folder to set up pip3 (bootstrapped with python), balena-engine en download the different containers. To prepare for a course, just run the "setupall.sh" to limit wait time during the course.

## Examples 

To get you started you can follow the examples scripts. The instruction can be found in the directory of the example. Start with Hello-world and go from there!

## PLCnext Engineer

The PLCnext Engineer project we use in this guide as a demo-project


# The first steps

Start by opening a shell session to your controller and clone this repositry to your controller. Then navigate to the example folder and start trying out the examples!

```
git clone https://github.com/pxcbe/python-startersguide.git
```