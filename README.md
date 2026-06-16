# Box Selection System

A Django-based system that recommends the most suitable shipping box for an order based on product dimensions, weight, and box capacity/cost. Built as part of a 24‑hour intern assignment.

## Features

- Product, Box, and Order management via Django admin
- Automated box recommendation logic (cheapest box that fits dimensions & weight)
- REST API endpoint for box recommendation
- Simple Bootstrap 5 UI to place an order and view the recommendation
- Unit tests covering multiple fit scenarios

## Tech Stack

- Python 3
- Django 
- SQLite (default)
- Bootstrap 5 (CDN)
- python‑decouple for environment variables

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd box_selection_system
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django python-decouple
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with:
   ```text
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Admin Panel

- Go to `http://127.0.0.1:8000/admin/`
- Add **Products** and **Boxes** (sample data provided in the testing section)

### Web UI

- Visit `http://127.0.0.1:8000/select-box/`
- Choose a product and quantity, click **"Get Recommendation"**
- See the recommended box or error message

### API Endpoint

```
GET /api/recommend-box/?product_id=1&quantity=2
```

Returns JSON with recommended box details or error.

## Running Tests

```bash
python manage.py test boxes
```

## Project Structure

```text
box_selection_system/
├── box_selection/          # Django project settings
│   ├── settings.py
│   └── urls.py
├── boxes/                  # Main app
│   ├── models.py           # Product, Box, Order models
│   ├── admin.py            # Admin registration
│   ├── box_selector.py     # Core recommendation logic
│   ├── views.py            # API + UI views
│   ├── forms.py            # Order form
│   ├── tests.py            # Unit tests
│   ├── templates/boxes/    # HTML template
│   └── urls.py             # App routes
├── .env                    # Environment variables (not committed)
├── manage.py
└── README.md
```

## Sample Data (for testing)

### Products

| Product     | Dimensions (L×W×H cm) | Weight (kg) |
|-------------|------------------------|-------------|
| Small Book  | 20 × 15 × 5            | 0.5         |
| Medium Toy  | 30 × 20 × 10           | 1.2         |
| Large Lamp  | 50 × 40 × 30           | 5.0         |

### Boxes

| Box           | Inner Dims (L×W×H cm) | Max Weight (kg) | Cost (₹) |
|---------------|------------------------|-----------------|----------|
| Tiny Box      | 25 × 20 × 8            | 1.0             | 40       |
| Standard Box  | 35 × 25 × 12           | 3.0             | 60       |
| Large Box     | 55 × 45 × 35           | 6.0             | 100      |
| Heavy Box     | 55 × 45 × 35           | 10.0            | 120      |
