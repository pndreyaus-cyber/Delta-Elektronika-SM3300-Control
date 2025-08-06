from DeltaElektronika import SM15K
import time
import datetime

# IP Address of the power supply, can be obtain the device itself.
IPV4 = '169.254.0.2' 

# To activate debugging option. Creates system-log file and logs there
SM15K.activateDebugLogger = True 

# To use the DeltaElektronika library.
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


MyDelta.system.setProgSourceV(src="eth")
MyDelta.system.setProgSourceI(src="eth")


MyDelta.source.SetCurrent(current=10)
MyDelta.source.SetVoltage(voltage=5)
MyDelta.output.SetOutput(setting="ON")

# Wait for the output to stabilize
time.sleep(2)

# Read the current and voltage values
ColorPrint.printNormal(message=f'Set output: {MyDelta.output.ReadOutputSet()}')
ColorPrint.printNormal(message=f'Set output current: {MyDelta.source.ReadCurrentSet()}A')
ColorPrint.printNormal(message=f'Set output voltage: {MyDelta.source.ReadVoltageSet()}V')

log_filename = "output_log.txt"
with open(log_filename, "w") as log_file:
    log_file.write("timestamp,voltage,current\n")
    for i in range(6):  # 6 times, every 10 seconds for 1 minute
        timestamp = datetime.datetime.now().isoformat()
        voltage = MyDelta.measure.MeasureVoltage()
        current = MyDelta.measure.MeasureCurrent()
        log_file.write(f"{timestamp},{voltage},{current}\n")
        time.sleep(10)


MyDelta.shutdown.limitShutdownValues()
MyDelta.shutdown.setShutdownOutput()