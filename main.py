import time
import board
import busio
import adafruit_ina260
import json

voltage = ""
json_dict = {}
i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c, address=0x41)

while 1:
        #print("Current", ina260.current)
        print("Voltage", ina260.voltage)
        voltage = str(ina260.voltage)
        #print("Power", ina260.power)
       # print("-----------")
        for variable in ["voltage"]:
            json_dict[variable] = eval(variable)
            with open("/home/albatross/PycharmProjects/powerManagement3/venv/batteryData.json", "w") as f:
                json.dump(json_dict, f)


        time.sleep(1)
