# Brain-Age-Prediction

Brain-Age-Prediction is a web application that estimates the brain age of users based on various cognitive tests. This project is built using Django and includes an admin approval system for new user registrations.

## Features

- **User Registration**: Users can register to access the brain age prediction tests.
- **Admin Approval**: Admin needs to approve new user registrations.
- **Brain Age Calculation**: Users can take cognitive tests to estimate their brain age after approval.

## Admin Login

- **Username**: admin
- **Password**: admin

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/anshive/Brain-Age-Prediction.git
   cd Brain-Age-Prediction
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Register as a new user:**

   - Visit the registration page and fill in the required details.

2. **Admin Approval:**

   - Log in as the admin using the provided credentials (username: `admin`, password: `admin`).
   - Approve the newly registered users in the admin panel.

3. **Calculate Brain Age:**

   - Once approved, log in as the user.
   - Take the cognitive tests to calculate your brain age.

## Dependencies

The project relies on the following dependencies, listed in requirements.txt:

    Django==3.2
    djangorestframework==3.12.4
    numpy==1.21.0
    pandas==1.3.0
    scikit-learn==0.24.2
    matplotlib==3.4.2

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at [anshivevasist@gmail.com](mailto:anshivevasist@gmail.com).
