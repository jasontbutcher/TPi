[![SI7021](SI7021_I2CS_A.png)](https://www.controleverything.com/content/Humidity?sku=SI7021_I2CS)
# SI7021
SI7021 Humidity and Temperature Sensor

The SI7021 is a Humidity and Temperature Sensor.
This Device is available from ControlEverything.com [SKU: SI7021_I2CS]

https://www.controleverything.com/content/Humidity?sku=SI7021_I2CS

This Sample code can be used with Raspberry pi.

##Java 
Download and install pi4j library on Raspberry pi. Steps to install pi4j are provided at:

http://pi4j.com/install.html

Download (or git pull) the code in pi.

Compile the java program.
```cpp
$> pi4j SI7021.java
```

Run the java program as.
```cpp
$> pi4j SI7021
```

##Python 
Download and install smbus library on Raspberry pi. Steps to install smbus are provided at:

https://pypi.python.org/pypi/smbus-cffi/0.5.1

Download (or git pull) the code in pi. Run the program

```cpp
$> python SI7021.py
```

The code output is the relative humidity and temperature reading in degree celsius and fahrenheit.
