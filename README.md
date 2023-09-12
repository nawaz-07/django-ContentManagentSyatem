# django-ContentManagentSyatem

# CMS Project

CMS Project is a Django-based Content Management System that allows administrators and authors to manage and publish content efficiently.

## Features

- **User Management:**
  - Admins can create, update, and delete user accounts.
  - Users can register, log in, and update their profiles.

- **Content Management:**
  - Admins can create, update, and delete content items.
  - Authors can create, update, and delete their own content items.

- **Authentication:**
  - JWT-based authentication for user registration and login.
  - Authorization checks ensure only authorized users can perform certain actions.

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/yourusername/cms-project.git](https://github.com/nawaz-07/django-ContentManagentSyatem.git)
   cd cms-project

2. Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install the Project Dependencies:
pip install -r requirements.txt


4. Apply Migrations:
python manage.py migrate


5. Start the Development Server:
python manage.py runserver


6. Access CMS Project:
Visit http://localhost:8000/ in your web browser.

7. Usage
Admin Panel: Access the admin panel at http://localhost:8000/admin/ to manage users and content items.

8. API Endpoints: Explore the API endpoints to interact with the application programmatically.

9. Seed Data
You can use the django-seed package to seed your database with sample data. Refer to the seed.py file for more details on seeding.
