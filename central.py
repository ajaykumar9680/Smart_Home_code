import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change port accordingly

def process_zigbee_data(data):
    # Process Zigbee data from end devices
    pass

while True:
    data = ser.readline().decode().strip()
    
    if "Zigbee:" in data:
        process_zigbee_data(data.split("-")[1].strip())
    elif "WiFi:" in data:
        # Process WiFi data
        pass
