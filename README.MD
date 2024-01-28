# Corporate Asset Tracking App
## Django Practical Challenge
### Overview
Welcome to the Corporate Asset Tracking App, a Django-based application designed to help organizations efficiently manage and monitor the distribution and usage of corporate assets such as phones, tablets, laptops, and other equipment.

### Goals
The primary objectives of this application are:

#### Multi-Company Support:
* The app is designed to be used by multiple companies simultaneously.
Each company can independently manage its assets and employees.

#### Employee Management:
* Companies can add and maintain a list of their employees within the system.
Flexibility to include all or a subset of employees based on company requirements.

#### Device Delegation:
* Companies and their staff can assign one or more devices to employees for specified durations.
  
#### Check-out and Return Tracking:
* The application tracks the dates and times when a device is checked out to an employee and when it is returned.
  
#### Condition Log:
* Each device has a detailed log that records the condition of the device when it was handed out and when it was returned.

### How to use
#### Installation
##### Clone the repository to your local machine:
* https://github.com/sagorluc/REPLIQ-django-test.git

##### Navigate to the project directory:
* cd Device_Management

##### Install the required dependencies:
* pip install -r requirements.txt

##### Apply database migrations:
* python manage.py makemigrations
* python manage.py migrate

### Usage
##### Run the development server:
* python manage.py runserver

