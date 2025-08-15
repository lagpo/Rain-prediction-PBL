# Rain-prediction-PBL

## Rain Prediction Weather Station
Designed and implemented a fully functional weather monitoring and rain prediction system using the ESP32 microcontroller as the central processing unit. The system continuously collected real-time environmental data including temperature, humidity, atmospheric pressure, and air quality using multiple sensors like BH1750, BME280, and water depth level sensor.
Implemented Arduino framework (C++) for firmware development, optimizing sensor reading intervals, data preprocessing, and memory usage to operate within the ESP32’s limited resources.


## ML model for predicttion 
Developed and trained a custom Machine Learning model to predict the likelihood of rainfall based on live sensor inputs, using historical weather datasets for model training.Integrated the trained ML model into the ESP32 firmware for on-device inference, ensuring predictions could be made locally without reliance on cloud services, reducing latency and improving reliability.

Designed a real-time data visualization interface accessible via Wi-Fi, enabling users to monitor environmental conditions and rain forecasts through a web dashboard or mobile device.Conducted model validation and tuning to improve prediction accuracy by experimenting with various ML algorithm, XGBoost and Random Forest
Tested the system in real weather conditions to ensure robustness, calibrating sensors and refining the prediction logic for better real-world performance.

## Key Achievements:
Achieved real world rain prediction accuracy of over 83.78% and ML accuracy over 93.65%.
Successfully deployed a low-cost, IoT-based weather station capable of operating autonomously in remote locations
