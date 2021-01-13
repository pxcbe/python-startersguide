# A containerized Python application

A containerized application has a lot of advantages, you can easily distribute an application with all the dependencies included in the container image.
It also makes starting the application after a reboot very easy. In this example we'll use the OPC UA script to develop a Python container.
Because the package comes with the image, we can run the script on the PLCnext controller.

## Dockerfile

```
FROM pxcbe/python-opcua

COPY ./app:/ap
```

