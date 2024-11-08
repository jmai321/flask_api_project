# Flask RESTful API Project

- Group Members: Jonathan Mai, Daniel Currey
- Screenshot including all postman endpoints can be found in the repo: screenshot.png
- Video Demonstrating working of authentication and file handling endpoints: [Click on this link](https://youtu.be/rBsJuuiSg5k)

## Features
- **Error Handling**: Returns  error messages for various HTTP status codes.
- **JWT Authentication**: Login endpoint provides JWT tokens for accessing protected routes.
- **File Handling**: Allows file uploads with type and size validation.
- **Public and Admin Routes**: Public routes require no authentication, while admin routes are protected.
- **CRUD Operations**: Allows creating, reading, updating, and deleting items.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/jmai321/flask_api_project.git
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

