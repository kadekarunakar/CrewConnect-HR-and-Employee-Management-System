# CrewConnect – HR and Employee Management System

CrewConnect is a web-based HR and Employee Management System developed using Django. It simplifies employee onboarding, employee management, leave management, payroll processing, payslip generation, and HR reporting through role-based access for HR and employees.

## Project Overview

The system provides two primary user roles:

- **HR:** Manages employees, departments, designations, leave requests, payroll, payslips, and reports.
- **Employee:** Views personal information, applies for leave, tracks leave status, views the leave calendar, and accesses payslips.

## Features

### 1. Employee Onboarding and Management
- Add, view, update, and delete employee records.
- Maintain Employee ID, name, email, phone, department, designation, joining date, employment type, salary, address, and employment status.
- Automatically create a Django User account when HR creates an employee.
- Send employees a secure password setup link through email.

### 2. Department and Designation Management
- Maintain separate department and designation master tables.
- Manage departments such as HR, Development, Testing, and Finance.
- Support designations such as Python Developer, Senior Python Developer, Software Tester, HR Executive, and Accountant.
- Use Django model relationships to associate employees with departments and designations.

### 3. Authentication and Role-Based Dashboards
- Use Django's built-in authentication system.
- Maintain a OneToOne relationship between the Django User model and Employee model.
- Create employee accounts with unusable passwords until the employee sets a password through the onboarding link.
- Redirect authenticated users to the appropriate dashboard based on their role.

### 4. Leave Management
- Allow employees to apply for leave.
- Support Earned Leave (EL), Sick Leave (SL), and Casual Leave (CL).
- Maintain Pending, Approved, and Rejected leave statuses.
- Allow HR to approve or reject leave applications.
- Enable employees to view their leave history and leave calendar.

### 5. Payroll and Payslip Generation
- Generate monthly employee payslips.
- Include basic salary, allowances, deductions, and net salary.
- Calculate net salary using the following formula:

  **Net Salary = Basic Salary + Allowances − Deductions**

- Prevent duplicate payslips for the same employee and month/year using a database-level unique constraint.
- Allow employees to access their payslips.

### 6. HR Payroll Reports
- Filter payroll information by month and year.
- Generate aggregated payroll reports.
- Use Django ORM aggregation functions, including `Sum`, to calculate payroll totals.

### 7. Responsive Frontend
- Build user interfaces using HTML, CSS, Bootstrap, and JavaScript.
- Use Django templates and template inheritance to reuse layouts, sidebars, and common UI components.
- Provide separate dashboards and navigation for HR and employees.

### 8. Email Integration
- Integrate SMTP for employee onboarding emails.
- Send password setup links when employee accounts are created.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Django | Backend web framework |
| SQLite | Relational database |
| Django ORM | Database operations and queries |
| HTML5 | Page structure |
| CSS3 | Styling |
| Bootstrap | Responsive UI components |
| JavaScript | Frontend interactivity |
| Django Authentication | User login and session management |
| SMTP | Employee onboarding emails |

## Application Workflow

```text
Employee Onboarding
        |
        v
Create Employee and User Account
        |
        v
Send Password Setup Email
        |
        v
Employee Sets Password
        |
        v
Authentication and Login
        |
        v
Role-Based Dashboard
        |
        +------------------------+
        |                        |
        v                        v
    HR Dashboard           Employee Dashboard
        |                        |
        v                        v
Employee Management       Profile Management
Department Management    Leave Application
Designation Management  Leave History/Calendar
Leave Approval           Payslip Access
Payroll Generation
        |
        v
Payslips and Payroll Reports
```

**Overall workflow:** Employee onboarding → Authentication → HR/Employee dashboard → Employee management and leave applications → Leave approval → Payroll and payslip generation → HR reporting.

## Project Structure

```text
CrewConnect/
│
├── CrewConnect/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employee/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── hr/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The structure above is illustrative. Adjust it to match the actual files and folders in your project.*

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CrewConnect.git
cd CrewConnect
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Create a virtual environment

**Windows:**

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Step 3: Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If it does not exist, install Django and the other dependencies your project actually uses, then generate the file:

```bash
pip freeze > requirements.txt
```

### Step 4: Configure environment variables

Keep secret keys, email passwords, and other credentials outside version control. Configure the values required by your Django settings using environment variables or a local `.env` file.

Do not upload `.env` or other files containing credentials to GitHub.

### Step 5: Apply database migrations

```bash
python manage.py migrate
```

### Step 6: Create an HR administrator

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

### Step 7: Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## Database Design

The application uses Django ORM models to manage relational data.

Key relationships include:

- **User – Employee:** One-to-one relationship between Django's User model and Employee.
- **Department – Employee:** A department can be associated with multiple employees.
- **Designation – Employee:** A designation can be associated with multiple employees.
- **Employee – Leave Application:** An employee can submit multiple leave applications.
- **Employee – Payslip:** An employee can have payslips for multiple payroll periods.

A database-level unique constraint prevents duplicate payslips for an employee in the same month and year.

## Security Considerations

- Use Django's built-in authentication and password validation.
- Keep secret keys, email credentials, and database passwords out of source control.
- Use appropriate authentication and authorization checks for HR and employee views.
- Restrict employees to their own personal information, leave records, and payslips.
- Configure `DEBUG = False` and appropriate `ALLOWED_HOSTS` for production deployment.
- Use HTTPS and secure cookie settings when deploying publicly.

## Future Enhancements

- Role-based permission improvements.
- Automated monthly payroll processing.
- Employee attendance management.
- Leave balance tracking.
- Exportable payroll reports.
- Dashboard analytics and visualizations.
- Production deployment and automated testing.

## Learning Outcomes

This project demonstrates practical experience with:

- Django MVT architecture.
- Django models, views, URLs, and templates.
- CRUD operations using Django ORM.
- Authentication and role-based access.
- One-to-one and foreign-key relationships.
- Leave approval workflows.
- Payroll calculations and database constraints.
- ORM aggregation for reporting.
- SMTP email integration.
- Reusable templates and responsive frontend design.

## Author

**Kade Karunakar**

GitHub: https://github.com/kadekarunakar

---

*CrewConnect – Simplifying HR operations through a centralized employee management system.*
