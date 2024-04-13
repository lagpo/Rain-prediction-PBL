import serial
from datetime import datetime
import csv



#Open a serial port 
ser = serial.Serial('/dev/ttyUSB0',baudrate=115200)
ser.flushInput()


while True:

    #Read in data from Serial until \n (new line) received
     ser_bytes = ser.readline()
     
     #Open a csv file and set it up to receive comma delimited input
     logging =  open('logging2.csv',mode='a')
     writer = csv.writer(logging, delimiter=",", escapechar=' ', quoting=csv.QUOTE_NONNUMERIC)


    #Convert received bytes to text format
     decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
     if(decoded_bytes.startswith(" ")): 
     
     	  #Retreive current time
          c = datetime.now()
          current_time = c.strftime('%H:%M:%S')
          current_date=c.strftime("%Y-%m-%d")
          values=[current_date,current_time]
          
          for element in decoded_bytes.rstrip().split("|")[:-1]:
               a,b = element.split(":")
               values.append(b);    

          print(values)
          #Write received data to CSV file
          
          writer.writerow(values)
          logging.close()
          print("logging finished")

ser.close()
logging.close()
print("logging finished")
          

