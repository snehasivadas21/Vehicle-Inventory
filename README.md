# Vehicle Inventory & Booking API

A RESTful API built with Django REST Framework for managing vehicle inventory and bookings.

The API supports vehicle CRUD operations, booking management, filtering, booking validation, automatic pricing, and prevention of overlapping bookings.

## Features

- Vehicle inventory management
- Vehicle CRUD APIs
- Booking creation and management
- Automatic booking price calculation
- Vehicle availability management
- Prevention of overlapping bookings
- Phone number validation
- Booking date validation
- Vehicle filtering
- Swagger API documentation
- Environment variable configuration

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- drf-spectacular
- SQLite

## Project Structure

```text
vehicle_system/
│
├── inventory/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

Installation
1. Clone the repository
git clone <your-github-repository-url>
cd vehicle_system
2. Create a virtual environment
python -m venv venv

Activate it.

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

Database Setup

Run migrations:

python manage.py makemigrations
python manage.py migrate
Run the Development Server
python manage.py runserver

The API will be available at:

http://127.0.0.1:8000/

API Documentation

Swagger documentation is available at:

http://127.0.0.1:8000/api/docs/

The OpenAPI schema is available at:

http://127.0.0.1:8000/api/schema/

API Endpoints

Vehicle APIs
Method	  Endpoint	          Description
GET	      /api/vehicles/	    List vehicles
POST	    /api/vehicles/	    Create vehicle
GET	      /api/vehicles/<id>/	Get vehicle details
PUT	      /api/vehicles/<id>/	Update vehicle
DELETE	  /api/vehicles/<id>/	Delete vehicle

Booking APIs
Method	  Endpoint	          Description
GET	      /api/bookings/	    List bookings
POST	    /api/bookings/	    Create booking
GET	      /api/bookings/<id>/	Get booking details

Vehicle Filtering

Vehicles can be filtered using query parameters.

Filter by brand
/api/vehicles/?brand=Toyota
Filter by fuel type
/api/vehicles/?fuel_type=Electric
Filter by availability
/api/vehicles/?is_available=true
Combine filters
/api/vehicles/?brand=Toyota&fuel_type=Hybrid

Vehicle Example
POST /api/vehicles/

Request:
{
    "name": "Corolla",
    "brand": "Toyota",
    "year": 2024,
    "price_per_day": "2000.00",
    "fuel_type": "Petrol",
    "is_available": true
}
Response:
{
    "id": 1,
    "name": "Corolla",
    "brand": "Toyota",
    "year": 2024,
    "price_per_day": "2000.00",
    "fuel_type": "Petrol",
    "is_available": true
}

Booking Example
POST /api/bookings/

Request:
{
    "vehicle": 1,
    "customer_name": "Sneha",
    "customer_phone": "9876543210",
    "start_date": "2026-08-25",
    "end_date": "2026-08-28"
}

Example response:
{
    "id": 1,
    "vehicle": 1,
    "customer_name": "Sneha",
    "customer_phone": "9876543210",
    "start_date": "2026-08-25",
    "end_date": "2026-08-28",
    "total_amount": "6000.00"
}

Create an admin user:

python manage.py createsuperuser

Then visit:

http://127.0.0.1:8000/admin/

Screen Recording:

Add your Google Drive / YouTube link here after recording.

Deployment:

Add the deployed API URL here after deployment.

Swagger:

Add deployed Swagger URL here after deployment.

Author

S Sneha


