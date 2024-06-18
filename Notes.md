## Exciting Updates to the Grade Tracking App!

Your feedback and usage have significantly enhanced my interactive grade-tracking app. These updates are designed to make the app more user-friendly, secure, and visually appealing. Here are the new features:

**Flask Framework and Flask-Login Integration:** The app now uses Flask, SqlAlchemy, and Flask-Login for better authentication and security. This integration ensures a more secure login process, protecting your data from unauthorized access.

**Code Refactoring:** The original app.py file, a hefty 600 lines of code, has been transformed into several modular pages. This restructuring enhances code readability and maintainability and boosts the app's performance, making future updates and maintenance a breeze. 

**Improved Styling using Dash-Bootstrap cards:** This update makes the interface more intuitive and visually appealing and enhances navigation, making it easier for you to input and find your grades.

**Docker Image Creation:** I've created a Docker image named "dashcoco1-flask". This addition simplifies deployment and ensures consistency across different environments, making running the app on various platforms easier.

**Ongoing Spanish Translation:** I'm translating the app to Spanish to make it accessible to a broader audience. Stay tuned for the multilingual support that will be available soon.

**Deployment Using AWS Services:** The app is being deployed using AWS services, ensuring high availability, scalability, and reliability. 

These updates bring a more secure, faster, and aesthetically pleasing experience to your fingertips. And this is just the beginning! Stay tuned for more updates.


```bash
ubuntu@hcoco1:~/dashcoco1-flask$ tree -L 3 -I 'venv|__pycache__'
.
├── app
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── config.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   └── signup.html
│   └── utils.py
├── commands.md
├── config.py
├── dash_app
│   ├── app.py
│   ├── assets
│   │   └── styles.css
│   ├── components
│   │   ├── callbacks.py
│   │   ├── dropdowns.py
│   │   ├── graphs.py
│   │   ├── __init__.py
│   │   ├── layout.py
│   │   └── tables.py
│   ├── index.py
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── ecs-params.yml
├── instance
│   ├── config.py
│   └── site.db
├── requirements.txt
└── run.py

8 directories, 30 files
```


```bash
ubuntu@hcoco1:~/dash-google$ tree -L 3 -I 'venv|__pycache__'
.
├── assets
│   └── favicon.ico
├── data
│   ├── backup_without_translation.py
│   ├── backup_with_translation.py
│   ├── data.py
│   ├── grades_over_time .csv
│   ├── jane_doe.jpg
│   └── john_doe.jpg
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── src
    ├── app.py
    ├── assets
    │   └── favicon.ico
    └── __init__.py

4 directories, 14 files
```



```yml
version: '3'
services:
  web:
    image: hcoco1/dashcoco1-flask:latest
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: development
      ```

docker pull hcoco1/dashcoco1-flask:latest

docker-compose up

docker-compose down


