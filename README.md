# Flask RESTful API Project

## Features
- **Error Handling**: Returns  error messages for various HTTP status codes.
- **JWT Authentication**: Login endpoint provides JWT tokens for accessing protected routes.
- **File Handling**: Allows file uploads with type and size validation.
- **Public and Admin Routes**: Public routes require no authentication, while admin routes are protected.
- **CRUD Operations**: Allows creating, reading, updating, and deleting items.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd flask_api_project
2. python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate    # On Windows

3. pip install -r requirements.txt

4. flask run

5. Test it using postman

