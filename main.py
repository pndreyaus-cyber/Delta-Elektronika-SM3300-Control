from DeltaElektronika import SM15K
import time

# IP Address of the power supply, can be obtain the device itself.
IPV4 = '169.254.0.2' 

# To activate debugging option. Creates system-log file and logs there
SM15K.activateDebugLogger = True 

# To use colorful printing at console.
ColorPrint = SM15K.ColorPrinter()
ColorPrint.printFeedback(message="Your message to print to console as feedback!")
ColorPrint.printComment(message="Your message to print to console as comment!")
ColorPrint.printError(message="Your message to print to console as error!")
ColorPrint.printNormal(message="Your message to print to console as normal!")
ColorPrint.printColorful(message="Your message to print to console as colorful!", colour="purple")
# Available colors for printColorful method are "purple", "blue", "cyan", "green", "red", "yellow", "normal"

# To use all comments for SM15K
MyDelta = SM15K.SM15K(IPV4=IPV4)

# Source related comments
#MyDelta.source."SourceRelatedComments"()

MyDelta.system.setProgSourceV(src="eth")
MyDelta.system.setProgSourceI(src="eth")

MyDelta.source.SetCurrent(current=20)
MyDelta.source.ReadCurrentSet()
MyDelta.source.SetVoltage(voltage=20)
MyDelta.source.ReadVoltageSet()


# Measure related comments
#MyDelta.measure."MeasureRelatedComments"()
#MyDelta.measure.MeasurePower()
#MyDelta.measure.SetAhMeasurementState(setting="ON")

# Output related comments
#MyDelta.output."OutputRelatedComments"()
MyDelta.output.ReadOutputSet()
MyDelta.output.SetOutput(setting="ON")

# System related comments
#MyDelta.system."SystemRelatedComments"()
#MyDelta.system.ReadWatchdogSet()
#MyDelta.system.SetPowerLimit(powerlimit=2000, setting="ON")

# Shutdown related comments
#MyDelta.shutdown."ShutdownRelatedComments"()
time.sleep(60) # Wait for 60 seconds to allow the system to stabilize
cnt = 0
while cnt < 60:
    print(f"Measured voltage: {MyDelta.measure.MeasureVoltage()}")
    print(f"Measured current: {MyDelta.measure.MeasureCurrent()}")
    time.sleep(1)
    cnt += 1


MyDelta.shutdown.limitShutdownValues()
MyDelta.shutdown.setShutdownOutput()