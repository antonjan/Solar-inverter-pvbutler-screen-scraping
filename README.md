# Solar-inverter-pvbutler-screen-scraping
This repository will have the PvButler solar wifi dongle code that will screenscrape the server.pvbutler.com website and get all your solar data and then send it to an mqtt server
## Usage
Edit the config.ini with your details for username and password for pvbuttler website and mqtt server details and username and password in the config as in exsample below and save file in same directory as the python file<br>
You will have to pip install some librayeries<br>
pip3 install beautifulsoup
pip3 install selenium
pip3 install json
pip3 install ?

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

## Run the code 
python3 ./scrape_pvbutler_3.py

## MQTT json object

        {
          "Name": "PV&Grid Charging+Grid Bypass",
          "Data_Sources": "Data Sources",
          "Solar": 134.0,
          "Charge": 0.0,
          "Consumption_Power_W": 137.0,
          "Charging": 0.0,
          "SOC": 50.0,
          "Solar_Today": 0.4,
          "Solar_Total": 507.2,
          "Discharged_Today": 0.3,
          "Discharge_Total": 164.3,
          "Charge_Today": 1.0,
          "Total_Charged": 831.0,
          "Grid_Today": 1.4,
          "Grid_Total": 1.2,
          "15": 4.5,
          "16": 583.5,
          "Load_Today": 1.1,
          "Load_Total": 32.2,
          "Solar_Storage": 0.0,
          "Grid_Storage": 0.0,
          "Load_Consumption": 0.0,
          "Load_Solar": 0.0,
          "Load_Grid_BP": 0.0,
          "CO2": 202.9,
          "Tree": 28.0,
          "Cole_Saved": 202.9,
          "Consumption_Power_VA": 206.0,
          "28": 0,
          "29": 0
        }

    
