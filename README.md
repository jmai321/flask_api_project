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
   ```
2. Create Virtual Environment 
 ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
 ```

3. Run the commands to install required packages and run flask app. 
   ```bash
   pip install -r requirements.txt
   flask run

6. Test it using Postman

