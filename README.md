# 📸 Photo Studio Booking , Equipment Rental Website & Editing Point

A fully functional Django-based web application for a photo studio. It allows users to book photography sessions like weddings, pre-weddings, baby shoots, etc., and also rent cameras and drones. This project is built to streamline photography bookings and equipment rentals from a single platform.

## 🔥 Features

- ✅ User registration & login system
- 📅 Book photography sessions (Wedding, Pre-wedding, Events, etc.)
- 🎥 Rent cameras and drones
- 📸 Admin panel to manage bookings and rentals
- 💳 Payment gateway integration (optional/coming soon)
- 📧 Email notifications for bookings
- 🗓️ Calendar view for studio schedule (optional)

## 🛠 Tech Stack

- **Backend:** Django (Python)
 
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
 
- **Database:** SQLite (default, can switch to PostgreSQL/MySQL)
   
- **Other:** Django Admin, Django ORM

## 🚀 Getting Started

1. Clone the Repository

```bash
    git clone https://github.com/your-username/Studio-Booking.git
    cd photo-studio-booking
```

2. Set Up Virtual Environment
   
   python -m venv venv
   
   source venv/bin/activate 

3. Install Requirements
   
   pip install -r requirements.txt

4. Apply Migrations

   python manage.py makemigrations
   
   python manage.py migrate

5. Start Development Server

   python manage.py runserver

##📁 Project Structure

photo-studio/
├── studio_app/              # Main Django app

├── static/

  └── screenshot/          # Project screenshots

├── media/                   # Uploaded media files

├── templates/               # HTML templates

├── db.sqlite3

├── manage.py

└── requirements.txt

## 🖼️ Screenshots

##🎯 Future Improvements

Integrate Razorpay/Stripe for online payments

Add user reviews and ratings

Enable multi-language support

SMS notifications

📝 License

MIT License

🙋‍♂️ Author

Shubham Parmar




