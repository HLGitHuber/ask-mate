# AskMate

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
AskMate is a web application that emulates the functionality of a Q&A platform like Stack Overflow. This project, developed in Python with Flask, JavaScript, CSS, and HTML, focuses on adding various new features in Sprint 3 to enhance user experience and interactivity. The project also involves working with a PostgreSQL database and applying advanced SQL concepts.

## Features
1. **Gitflow Workflow:** The project follows the Gitflow workflow for team collaboration, making it easier to manage branches, merge code, and track progress.

2. **User Registration and Login:**
    - Users can register for a new account with a username (or email address) and a password.
    - Registered users can log in to the system.
    - Authentication is handled securely with password hashing and sessions.

3. **User Management:**
    - View a list of all registered users with details such as username, registration date, and user activity.
    - User profiles display the user's questions, answers, and comments.

4. **User Activity Tracking:**
    - Users are associated with the questions, answers, and comments they create.
    - Users can mark answers as accepted, with visual distinctions for accepted answers.

5. **Reputation System:** Users earn reputation points for positive contributions and lose points for downvoted content.

6. **Tagging System:** View a list of all existing tags and the number of questions associated with each tag.

7. **Advanced Search and Sorting:**
    - Filter and sort questions on the `bonus-questions` route without page reload.
    - Filter by text content and sort questions based on different columns.

8. **Font Size Adjustment:** (Optional)
    - Users can adjust the font size on the page to improve readability.

## Getting Started
To set up and run the AskMate project, follow these steps:

1. **Clone the Repository:** Clone the project repository to your local machine.
   ```shell
   git clone <repository-url>

2. **Database Setup:** Ensure you have a PostgreSQL database set up. You can use the sample_data script to populate the database with initial data.

3. **Environment Variables:** Set the following environment variables in your development environment, typically in a .env file or using an IDE-specific configuration:
    ```
    FLASK_APP=server.py
    FLASK_DEBUG=1
    PSQL_USER_NAME=<your-postgres-username>
    PSQL_PASSWORD=<your-postgres-password>
    PSQL_HOST=localhost
    PSQL_DB_NAME=cc_ask_mate
    ```

4. **Install Dependencies:** Install the necessary Python dependencies using pip.
    ```
    pip install -r requirements.txt
    ```

5. **Run the Application:** Start the Flask application.
    ```
    flask run
    ```

6. **Access the Application:** Open your web browser and navigate to `http://localhost:5000` to access the AskMate application.

## Usage

* Register for an account or log in to access the features.
* Explore questions, answers, and user profiles.
* Ask and answer questions, add comments, and mark answers as accepted.
* Interact with the reputation system and tags.
* Use the advanced search and sorting features on the bonus-questions route.
* Adjust the font size for improved readability (if enabled).

## Contributing

If you would like to contribute to the AskMate project, please follow the Gitflow workflow and create feature branches for the new features or bug fixes. Submit pull requests for review, and ensure that your code follows the project's coding standards.