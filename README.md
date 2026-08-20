# Vehicle Inventory & Booking REST API

A complete Vehicle Inventory and Booking system built with **Django REST Framework**.  
This API allows managing vehicles, creating bookings with proper validations, automatic pricing calculation, and preventing double-booking.

---

## 🚀 Live API

**Base URL:** [https://vehicle-inventory-5j02.onrender.com](https://vehicle-inventory-5j02.onrender.com)

- Vehicles: [/api/vehicles/](https://vehicle-inventory-5j02.onrender.com/api/vehicles/)
- Bookings: [/api/bookings/](https://vehicle-inventory-5j02.onrender.com/api/bookings/)
- API Documentation (Swagger): [/api/docs/](https://vehicle-inventory-5j02.onrender.com/api/docs/)
  
### 🎥 Screen Recording

[Watch the Screen Recording on YouTube](https://youtu.be/FArl2osUcO0)

---

## ✨ Features

- Full CRUD operations for Vehicles and Bookings
- Filtering vehicles by `brand`, `fuel_type`, and `is_available`
- Automatic calculation of `total_amount` (days × price_per_day)
- Business logic validations:
  - No overlapping bookings for the same vehicle
  - Start date cannot be in the past
  - End date must be after start date
  - Phone number must be exactly 10 digits
  - Vehicle becomes unavailable after booking
- Clean and well-structured REST API
- Swagger / OpenAPI documentation

---

## 🛠 Tech Stack

- Python 
- Django 
- Django REST Framework
- PostgreSQL (Production)
- SQLite (Development)
- Render (Hosting)
- WhiteNoise (Static files)
- drf-spectacular (API Documentation)

---

## 📦 Setup Instructions (Local)

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Create virtual environment

python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Environment variables
Create a .env file in the root directory:

SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

5. Run migrations
Bashpython manage.py migrate

6. Create superuser 
Bashpython manage.py createsuperuser

7. Run the development server
Bashpython manage.py runserver
API will be available at: http://127.0.0.1:8000

🔗 API Endpoints
Vehicles

Method   Endpoint             Description
GET      /api/vehicles/       List all vehicles
POST     /api/vehicles/       Create a new vehicle
GET      /api/vehicles/{id}/  Retrieve vehicle details
PUT      /api/vehicles/{id}/  Update vehicle
DELETE   /api/vehicles/{id}/  Delete vehicle

Filtering examples:

/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Electric
/api/vehicles/?is_available=true

Bookings

Method    Endpoint            Description
GET       /api/bookings/      List all bookings
POST      /api/bookings/      Create a new booking
GET       /api/bookings/{id}/ Retrieve booking details

Sample Booking Request (JSON)

{
  "vehicle": 1,
  "customer_name": "John Doe",
  "customer_phone": "9876543210",
  "start_date": "2026-08-25",
  "end_date": "2026-08-28"
}

Successful Response:

{
  "id": 3,
  "vehicle": 1,
  "customer_name": "John Doe",
  "customer_phone": "9876543210",
  "start_date": "2026-08-25",
  "end_date": "2026-08-28",
  "total_amount": "9000.00"
}

📁 Project Structure

vehicle_inventory/
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
├── build.sh
├── .env.example
└── README.md

Developed by: S Sneha
GitHub: https://github.com/snehasivadas21?
