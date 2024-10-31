Steps to create the IoT MQTT-based Dashboard

1. set up Django for Backend ---> refer create a django project file
2. Install Required Libraries ---> refer create a django project file

3. Create Models for Sensors and Temperature Data ---> refer models.py

4. Create Views and URL Routing ---> refer views.py
5. Create User Login page ---> refer views.py
6. Create Main Dashboard View ---> refer views.py

7. Define URL Routes ---> urls.py

8. Create HTML templates ---> login.html 
			      dashboard.html


9. Configure MQTT Client --> MQTT Client Script ---> refer mqtt_client.py 

10. Frontend Graph ---> 
	The dashboard will use Chart.js to visualize the temperature data in a line chart
	The data will be fetched via an API endpoint (/api/temperature)

11. Run the Project

	a) Start the Django development server: python manage.py runserver
	b) Run the MQTT client in a separate terminal: python mqtt_client.py
	c) Access the dashboard at http://localhost:8000/dashboard/