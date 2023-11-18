import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import paho.mqtt.publish as publish
import re
import configparser
#This programm reads the data from server.pvbutler.com and publish the data to MQTT server
#PVbutler user credensials and MQTT credensials need to modified in the config.ini for this program to work
config = configparser.ConfigParser()
config.read('config.ini')
pvbutler = config['pvbutler']
mqtt = config['mqtt']

#print("login url >> ",pvbutler["login_url"]) 
login_url = pvbutler["login_url"]
print("login url >> ",login_url) 
landing_url = pvbutler["landing_url"]
print("landing_url>>>",landing_url)
username = pvbutler["username"]
print("username>>>",username)
password = pvbutler["password"]
print("username>>>",password)

#{ "Name": "PV Charging+Loads Supporting", "Data Sources": "Data Sources", "Solar": "115W", "Charge": "2.5", "Consumption Power": "217W/332VA", "Charging": "99W", "SOC": "25%", "Solar Today": "0.6", "Solar Total": "504.3", "Discharged Today": "0.5", "Discharge Total": "163.1", "Charge Today": "1.5", "Total Charged": "825.8", "Grid Today": "1.0", "Grid Total": "1.1", "14": "4.5", "15": "583.5", "Load Today": "0.6", "Load Total": "25.5", "Solar Storage": "1", "Grid Storage": "1.5", "Load Consumption": "0.9", "Load Solar": "0.8", "Load Grid BP": "0.1", "CO2": "201.7", "Tree": "28", "Cole Saved": "201.7", "26": 0, "27": 0 }
#try:
while True:
		# Set up the session for making requests
		session = requests.Session()
		# Use Selenium to open a browser and interact with the page
		#driver = webdriver.Chrome()  # Use appropriate webdriver for your browser
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		driver = webdriver.Chrome(options=options)  # Use appropriate webdriver for your browser
		#driver = webdriver.Chrome()
		driver.get(login_url)
		print("opening login url")
		# Find the username and password fields and populate them
		username_field = driver.find_element(By.ID, 'val_loginAccount')
		username_field.send_keys(username)
		print("sending username")
		password_field = driver.find_element(By.ID, 'val_loginPwd')
		password_field.send_keys(password)
		print("seding password")
		# Find and click the Sign In button
		signin_button = driver.find_element(By.CLASS_NAME, 'loginB')
		signin_button.click()
		print("click on button")
		# Wait for the login to complete (you may need to customize this)
		#driver.implicitly_wait(10)
		print("waiting for 2-s")
		time.sleep(20)
		print("Done waiting")
		# Get the landing page content after successful login
		landing_page_content = driver.page_source
		print("waiting for 30s")
		time.sleep(30)  # Makes Python wait for 5 seconds
		print("done Waiting")
		# Use BeautifulSoup to parse the landing page content
		soup = BeautifulSoup(landing_page_content, 'html.parser')
		mydivs2 = soup.find_all("div",{"class_": "val"})
		mydivs3 = soup.find_all('span', {"class": "val"})  
		print("_____________________________")
		print("the div",mydivs3)
		print("div size",len(mydivs3))
		loop=0
		#inverter_data = [0][0] * 29
		inverter_data = [["Name", 0],["Data_Sources" , 0],["Solar", 0],["Charge",0],["Consumption_Power_W",0],["Charging",0],["SOC",0],["Solar_Today",0],["Solar_Total",0],["Discharged_Today",0],["Discharge_Total",0],["Charge_Today",0],["Total_Charged",0],["Grid_Today",0],["Grid_Total",0],["15",0],["16",0],["Load_Today",0],["Load_Total",0],["Charge",0],["Solar_Storage",0],["Grid_Storage",0],["Load_Consumption",0],["Load_Solar",0],["Load_Grid_BP",0],["CO2",0],["Tree",0],["Cole_Saved",0],["Consumption_Power_VA",0],["28",0],["29",0]]
		for i in mydivs3:
			html_content2 = mydivs3[loop].text
			print(loop," ",i," val " ,html_content2, end = '\n ')
			if loop == 0:
				if html_content2 == "--":
					print(" ************** no data trying again ***************")
					break
				else:
					inverter_data[0][1] = html_content2
			elif loop == 1:
					inverter_data[loop][1] = html_content2
			elif loop == 2:
					if html_content2[:-1] == '---.':
						print(" ************** no data trying again ***************")
						break
					#html_content2 = float(html_content2[:-1])
					inverter_data[2][1] = float(html_content2[:-1])
			elif loop == 3:
					#html_content2 = float(html_content2[:-1])
					inverter_data[3][1] = float(html_content2[:-1])
			elif loop == 4:
					Consumption_Power = html_content2.split("/")
					print("con 1", Consumption_Power[0])
					print("con 2", Consumption_Power[1])
					con1 = Consumption_Power[0]
					con2 = Consumption_Power[1]
					inverter_data[4][1] = float(con1[:-1])
					inverter_data[28][1] = float(con2[:-2])
			elif loop == 5:
					#html_content2 = float(html_content2[:-1])
					inverter_data[5][1] = float(html_content2[:-1])
			elif loop == 6:
				    #html_content2 = float(html_content2[:-1])
				    inverter_data[6][1] = float(html_content2[:-1])
			elif loop == 28:
					#do nothing	
					a=1
			else:
					#html_content3 = re.sub("[^0-9]","",html_content2) 
					inverter_data[loop][1] = float(html_content2)
					#print(loop," ",i," val " ,html_content2, end = '\n ')
					#print("html tag value",html_content2)
			loop += 1

		# Convert array to JSON object
		data_dict = dict(inverter_data)
		json_object = json.dumps(data_dict,indent=2)

		# Print the resulting JSON object
		print(json_object)
		# MQTT Broker Settings
		mqtt_broker = mqtt["broker"]
		print("mqtt_broker",mqtt_broker)
		mqtt_port = int(mqtt["port"])
		print ("mqtt_port >>>",mqtt_port)
		#mqtt_port = 1883
		mqtt_topic = mqtt["topic"]
		print("mqtt_topic",mqtt_topic)
		# Convert the array to a string
		message = json_object #",".join(json_object)
		usernamemqtt = mqtt["username"] #"homeassistant"
		passwordmqtt = mqtt["password"] # "h0m3@ss1$tant"
		print("mqtt message",message)
		
		# Publish the message to the MQTT broker
		publish.single(mqtt_topic, message, hostname=mqtt_broker, port=mqtt_port,auth={'username': usernamemqtt, 'password': passwordmqtt})

		# Reload the landing page
		#	reload_response = requests.get(landing_page_url, cookies=cookies)

		# Close the browser
		driver.quit()
		print("wating for 30 S")
		time.sleep(30)
#except Exception as error:
#  print("An exception occurred:", error) # An exception occurred: division by zero

