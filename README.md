## OEE Calculion APP
#### Overall Equipment Effectiveness (OEE) is a performance metric used in manufacturing to assess the efficiency of equipment or machines. It's calculated based on Availability, Performance, and Quality metrics.

## Technology Stack
#### This OEE Calculator is built using Python, Django, and Django REST framework. It leverages the power of these frameworks to provide real-time OEE calculations and insights.

## What it Calculates
#### The OEE Calculator computes the Overall Equipment Effectiveness (OEE) using the following formula:

- OEE = Availability * Performance * Quality
- Availability: Available Time - Unplanned Downtime / Available Time
- Performance: Ideal Cycle Time * Actual Output / Available Operating Time
- Quality: No of good products / Total no of products produced
  
## Data Source
#### The application retrieves data from a SQLite database. This database stores information about machines, production logs, and other relevant data for OEE calculation.

1. Clone and Setup
  - git clone https://github.com/yourusername/oee-calculator.git

2. Install Requirements:
  - pip install -r requirements.txt

3. Run the Server:
    - python manage.py runserver
    - Type "/api/" after the port number 

4. Using the API
    - admin pannel
        - /admin
        - username: admin
        - password: kishor
    Admin Panel: Admins can manage the application through the admin interface.

## API Endpoints
### Calculate OEE: GET /machines/<int:pk>/calculate_oee/
