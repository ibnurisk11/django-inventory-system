# django-inventory-system

A simple Inventory Management System built with Django. This project helps you manage products, stock levels, and transactions efficiently.

## Features

- Product management (add, edit, delete)
- Stock tracking
- Transaction history
- User authentication

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-inventory-system.git
    cd django-inventory-system
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage

- Access the system at `http://127.0.0.1:8000/`
- Log in with your credentials
- Start managing your inventory

## License

This project is licensed under the MIT License.