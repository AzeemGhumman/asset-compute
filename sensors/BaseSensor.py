class BaseSensor:


    configure(pass in generic object, data and events): one time
    read(): every time we want to read sensor data
    parse(): convert raw data to something we can send to server -> output = dictionary
