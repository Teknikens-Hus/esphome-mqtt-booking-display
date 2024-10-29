import os
import json
import sys
import serial.tools.list_ports

esphomeVersion = "Version: 2024.10.2"
config_file = "config.json"

def install_new_devices():
    print("Lets install new devices!")
    if(not verify_esphome()):
        print("Please install the required version of esphome.")
        return
    config = getConfig()
    for device in config["devices"]:
        print(f"Installing {device['name']}, type: {device['type']}, which will get events from {device['eventsTopic']}...")
        list_com_ports()
        selectedPort = input("Write the COM port for the device: (ex: COM5): ")
        if not validateComPort(selectedPort):
            print("Invalid COM port. Please try again.")
            sys.exit(0)
        os.popen(f"esphome -s name {device['name']} -s eventsTopic {device['eventsTopic']} run ESPHOME/{device['type']} --device {selectedPort} --no-logs").read()
        print(f"{device['name']} installed")

def ota_update_existing_devices():
    print("Updating devices...")
    if(not verify_esphome()):
        print("Please install the required version of esphome.")
        return
    config = getConfig()
    for device in config["devices"]:
        print(f"Installing {device['name']}, type: {device['type']}, which will get events from {device['eventsTopic']}...")
        os.popen(f"esphome -s name {device['name']} -s eventsTopic {device['eventsTopic']} run ESPHOME/{device['type']} --device {device['name']}-booking-display.local --no-logs").read()
        print(f"{device['name']} updated")

def verify_esphome():
    installedVersion = os.popen("esphome --version").read().strip()
    installedVersionParts = installedVersion.split('.')[:2]
    requiredVersionParts = esphomeVersion.split('.')[:2]
    if installedVersionParts == requiredVersionParts:
        #print("The installed esphome version meets the required version.")
        return True
    else:
        print("The installed esphome version does not meet the required version.")
        print("Installed esphome version: " + installedVersion)
        print("Required esphome version: " + esphomeVersion)
        return False

def validateComPort(port):
    if port.startswith("COM") and port[3:].isdigit():
        return True
    else:
        return False

def getConfig():
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    else:
        return generate_config()

def generate_config():
    print("Config file not found. Starting configuration process...")
    config = {}
    config["devices"] = []
    numDevices = input("How many devices do you want to add? ")
    if not numDevices.isdigit():
        print("Invalid input. Please enter a number.")
        sys.exit(0)
    for i in range(int(numDevices)):
        device = makeDevice()
        config["devices"].append(device)
        print("Device added to config file!")
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"Generic config file created: {config_file}")
    return config

def makeDevice():
    name = input("Please enter the device name: ")
    name = name.lower().replace(" ", "-")
    eventsTopic = input("Please enter the events mqtt topic: ")

    typeSelected = False
    while not typeSelected:
        print("Please select the device type:")
        print("1. e-paper-display.yaml")
        print("2. small-oled-display.yaml")
        type = input("Enter the number of the type: ")
        if type == "1":
            type = "e-paper-display.yaml"
            typeSelected = True
        elif type == "2":
            type = "small-oled-display.yaml"
            typeSelected = True
        else:
            print("Invalid type. Please try again.")
    return {"name": name, "eventsTopic": eventsTopic, "type": type}

def modify_config():
    config = getConfig()
    print("Current config:")
    print(json.dumps(config, indent=4))
    print("Please select an option:")
    print("1. Add a device")
    print("2. Remove a device")
    print("3. Update a device")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        device = makeDevice()
        config["devices"].append(device)
    elif choice == "2":
        name = input("Enter the name of the device you want to remove: ")
        for device in config["devices"]:
            if device["name"] == name:
                config["devices"].remove(device)
    elif choice == "3":
        name = input("Enter the name of the device you want to update: ")
        for device in config["devices"]:
            if device["name"] == name:
                config["devices"].remove(device)
                newDevice = makeDevice()
                config["devices"].append(newDevice)
    else:
        print("Invalid choice. Please try again.")
        modify_config()
    
    if len(config["devices"]) > 0:
        with open(config_file, 'w') as file:
            json.dump(config, file, indent=4)
        print("Config file updated!")
    else:
        os.remove(config_file)
        print("Config file became empty so its been removed. Please create a new one.")

def list_com_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Port: {port.device}, Description: {port.description}")

def main():
    print("Welcome to the Booking Display AutoScript!")
    print("Please select an option:")
    print("1. Install new devices")
    print("2. OTA update existing devices")
    print("3. Create/Update config file")
    print("4. List COM ports")

    choice = input("Enter the number of your choice: ")
    print()

    if choice == "1":
        install_new_devices()
    elif choice == "2":
        ota_update_existing_devices()
    elif choice == "3":
        if(os.path.exists(config_file)):
            modify_config()
        else:
            generate_config()
    elif choice == "4":
        list_com_ports()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()