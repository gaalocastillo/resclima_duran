import configparser
from datetime import datetime

def parseCSV(file, sensor_type):
	"""Parse a csv from any meteorological station, and save measures in the database"""
	config = configparser.ConfigParser()
	config.read("meteo_stations.ini")
	if sensor_type not in config:
		print ("Meteorological station not configured. Exit...")
		sys.exit()
	file = open(file,"r")
	headers= int (config[sensor_type][headers])
	#read verbose headers
	for i in range(headers):
		file.readline()
	#start reading the file
	for line in file:
		measures = line.strip().split(",")
		#Parse timestamp as it can be a datetime or date and time independent fields
		datetime_format = config[sensor_type]["datetime_format"]
		date_pos = config[sensor_type]["date_pos"]

		if(config[sensor_type]["time_pos"]=="None"):
			ts = datetime.strptime(measures[date_pos], datetime_format)

		else:
			time_format = config[sensor_type]["time_format"]
			datetime_format = datetime_format+" "+time_format
			time_pos = config[sensor_type]["time_pos"]

			date = measures[date_pos]
			time = measures[time_pos]
			ts = datetime.strptime(date+time, datetime_format)




	    

