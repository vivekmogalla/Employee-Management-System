
# Employee Management System

An Employee Management System in Django keeps track of all of the employee’s information and data. We’ve created all of the employee's and company crud (create, read, update, and delete) operations. This is a role-based module in which the admin can perform any operation on the data.

[![Python Badge](https://img.shields.io/badge/Python-YourColor?style=for-the-badge&logo=Python&logoColor=yellow)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=blue)](https://docs.djangoproject.com/en/4.2/) [![Bootstrap Badge](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/) [![SQLite3 Badge](https://img.shields.io/badge/SQLite3-%2300f.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://www.geeksforgeeks.org/html5-introduction/) [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.w3schools.com/js/)

## Features

•	Add Employee - The admin can add the employee in this software.

•	View Employee Details - The admin can view the list of all employee details.

•	Update Employee Details - The admin can edit the employee details and information.

•	Delete Employee - The admin can remove the employee from the database.

> This Application was created using Python, Django, HTML/CSS, and Bootstrap.


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django installed
- A modern web browser

### Installation

1. Clone the repository:

        git clone https://github.com/vivekmogalla/Employee-Management-System.git

2. Navigate to the Project directory
 

3. Install python virtual environment using pip command
 
       pip install virtualenv (same for linux and windows)

4. Create a Python virtual environment
 
       virtualenv env (same for linux and windows)

5. Activate the virtual environment
 
       cd env/scripts/.activate (windows)
       source env/bin/activate (Linux)

6. Install the required Python packages

        pip install -r requirements.txt

7. Run database migrations

        python manage.py migrate

8. Create a superuser accont (for admin access)

        python manage.py createsuperuser

9. Start the development server:

        python manage.py runserver

## Usage
### CRUD Operations
#### Add New Employee Information
1. Navigate to the add employee url (add-emp/) page to add the Employee details.

   <img width="960" alt="add_employees_EMS" src="https://github.com/vivekmogalla/Employee-Management-System/assets/131423732/ffd2be0d-8812-4ea2-9524-187552a071cd">


#### Edit Employee Info
1. Navigate to the Edit employee url (update-emp/<int:emp_id>/) page to update the Existing employee details.
   
   <img width="960" alt="update_emp_ems" src="https://github.com/vivekmogalla/Employee-Management-System/assets/131423732/22451ab4-4c49-4341-b36d-0ca5f40123ce">


#### Delete Employee Info
1. Navigate to the Delete employee url (delete-emp/<int:emp_id>/) page to Delete the employee record using employee_id.

#### Employee Home Page
1. Navigate to the Employee Home Page url ("home/") page.

   <img width="960" alt="home_view_ems" src="https://github.com/vivekmogalla/Employee-Management-System/assets/131423732/93055fa3-5ffc-4994-97ca-09872c982e1c">




