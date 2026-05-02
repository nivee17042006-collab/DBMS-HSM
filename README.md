# Hospital Management System Using ER Diagram and Stored Procedure

This project is a web-based Hospital Management System developed using Flask and DBMS concepts. It is designed to manage hospital records such as patients, doctors, nurses, staff, pharmacy stock, IoT monitoring, and infant security details in a centralized system.

## Project Aim

The aim of this project is to reduce manual hospital record handling and provide a secure and structured digital system. The project is based on ER diagram design and stored procedures for important database operations.

## Main Modules

- Staff Login Module
- Patient Registration Module
- Admin Dashboard Module
- Doctor Portal Module
- Nurse Portal Module
- Staff Portal Module
- Pharmacy Portal Module
- IoT and Infant Security Module

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- MySQL / SQLite
- HTML
- CSS
- SQL Stored Procedures

## Database Design

The database is designed using ER diagram concepts. It contains tables for:

- Users
- Access Layers
- Doctors
- Patients
- Ward Assignments
- Prescriptions
- Pharmacy Stock
- IoT Band Monitor
- Infant Security

## Stored Procedures

The project includes stored procedures for important operations such as:

- `AddPatient()`
- `GetPatientDetails()`
- `ValidateStaffLogin()`
- `GetDoctorPatients()`
- `GetNursePatientDetails()`
- `UpdatePharmacyStock()`
- `GetIotAlerts()`
- `GetAdminSummary()`

These procedures improve database organization, reduce repeated query logic, and support the project topic technically.

## How the Application Works

- Staff can log in using role, login ID, password, and BioThumb ID
- Patients can be registered through the registration form
- Admin can monitor hospital summary details
- Doctors and nurses can view patient and prescription information
- Pharmacy staff can manage medicine stock
- IoT and infant security modules show monitoring and alert details

## Deployment

This project can be deployed on Render.

### Required files

- `app.py`
- `requirements.txt`
- `render.yaml`
- `hms_batch4_dataset.sql`
- `templates` folder
- `static` folder

### Render configuration

Build Command:
```text
pip install -r requirements.txt
