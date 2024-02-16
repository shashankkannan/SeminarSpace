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

**Application flow:**

**User Registration:**
  - Users access the registration page (register_page.html) to provide their details. They upload a photo, which is saved in the ‘data/known’ directory. The   registration data, including face encodings, is stored in the MongoDB collection (‘face_encodings’).

**Workshop Management:**
  - Administrators use the web application to upload workshop details, including the workshop name and presenter’s name.
  - Workshop data is stored in the MongoDB collection (‘workshop_dets’). Email notifications are sent to registered users informing them about upcoming       workshops/seminars.

**Attendance Capture:**
  - On the day of the workshop, the ‘capture_photo.html’ page is used to capture images. Face recognition is performed on the captured images using the     ‘face_recognition’ library. Captured photos are temporarily stored in the ‘data/unknown’ directory. Captured images are compared with the face encodings of registered users. If a match is found, the attendee’s name is recorded, and the attendance count is updated in the MongoDB collection. The workshop name is added to the user’s ‘workshop_list’ if not already present.

**Results Display:**
  - Results of the attendance capture are displayed on the dashboard. A list of attendees and matched records is shown.
  
**Clearing Data:**
  - Administrators have the option to clear registered users, attendance lists, or workshop data. The ‘clear_registered_users’ and ‘clear_attendance_list’     routes handle the data clearance.

**Toast Notifications:**
  - Toast notifications are used for success and error messages, providing real-time feedback on user actions.
  - Additional Features: Users can register for multiple workshops, and attendance data is updated accordingly. The system ensures that duplicate entries are avoided when updating workshop lists.
