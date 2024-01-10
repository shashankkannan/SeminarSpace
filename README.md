# SeminarSpace
SeminarSpace is a thoughtfully designed software solution aimed at streamlining seminar attendance and management. Built on a Python foundation with Flask for web development, it seamlessly integrates with a MongoDB database for effective data handling.

**Key Aspects:**
- **Facial Recognition Technology:** SeminarSpace employs advanced facial recognition, incorporating machine learning and Convolutional Neural Network (CNN) models for precise attendance tracking.

- **User-Friendly Interface:** The frontend is developed using HTML, CSS, and JavaScript, ensuring a straightforward and accessible experience for administrators managing seminar logistics.

- **Efficient Backend:** SeminarSpace's backend, developed in Python and supported by Flask, ensures smooth communication and efficient data flow, contributing to reliable system performance.

- **Data Management with MongoDB:** The application makes use of MongoDB for storing and retrieving data, providing a reliable and scalable solution for evolving data requirements.


The **main.py** file initializes a Flask application, creates a MongoDB connection with the specified URI, and registers the task_controller blueprint, which likely contains route definitions and related functionalities. When the script is executed directly, it starts the Flask development server in debug mode, enabling detailed error messages and automatic server reloads upon code changes for smoother development. The application is configured to connect to a MongoDB database named 'ADT_project' running on the localhost at port 27017.

In the **templates folder, HTML files** play a crucial role in defining the structure and design of the web pages. These files contain embedded styles and scripts to handle dynamic operations on the page. They establish a connection with the application's routes through controllers, allowing seamless integration between the frontend and backend functionalities.

The **task_controller.py in controllers folder** module in the Seminar Space project is a Flask Blueprint responsible for handling various tasks related to seminar attendance, workshop registration, and user interactions. It encompasses routes for rendering HTML templates, fetching data from MongoDB, registering students and workshops, processing unknown faces for attendance, and managing email communication. The controller efficiently integrates with the main Flask application, using routes and functions to ensure a seamless flow of data and actions between the frontend and backend components. From capturing and registering photos to handling workshop registrations and email communications, the 'task_controller' plays a pivotal role in orchestrating the core functionalities of the Seminar Space software.

SeminarSpace combines simplicity with effective technology, offering a formal and user-friendly tool for seminar organizers and administrators.
