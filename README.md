# Solar-inverter-pvbutler-screen-scraping
This repository will have the PvButler solar wifi dongle code that will screenscrape the server.pvbutler.com website and get all your solar data and then send it to an mqtt server
## Usage
Edit the config.ini with your details

    [DEFAULT]
    ServerInterval = 45 #Sec
    
    [pvbutler]
    login_url = http://server.pvbutler.com/login
    landing_url = http://server.pvbutler.com/index
    username = username
    password = password
    
    [mqtt]
    broker = mqtt.server.com
    port = 1883
    topic = home/5kwInverter
    username = mqtt_username
    password = mqtt_password
    
    [json]
    json_object = '[["Name", 0],["Data_Sources" , 0],["Solar", 0],["Charge",0],["Consumption_Power_W",0],["Charging",0],["SOC",0],["Solar_Today",0],["Solar_Total",0],["Discharged_Today",0],["Discharge_Total",0],["Charge_Today",0],["Total_Charged",0],["Grid_Today",0],["Grid_Total",0],["15",0],["16",0],["Load_Today",0],["Load_Total",0],["Charge",0],["Solar_Storage",0],["Grid_Storage",0],["Load_Consumption",0],["Load_Solar",0],["Load_Grid_BP",0],["CO2",0],["Tree",0],["Cole_Saved",0],["Consumption_Power_VA",0],["28",0],["29",0]]'
    
