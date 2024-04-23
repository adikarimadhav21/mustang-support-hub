# Mustangs Support Hub

**Enhancing Student Life at Midwestern State University**

**Team:**
- Madhav Adhikari 
- Naga Vamshi Krishna Jammalamadaka
- Nitish Kumar Erelli

The Mustangs Support Hub is a dynamic platform designed to address the practical needs and challenges faced by university students on a daily basis. From finding compatible roommates to sharing rides and managing lost belongings, Mustangs Support Hub provides essential services and features tailored to the unique needs of our campus community.

## Key Features:

- University Marketplace for buying and selling items
- Room Finder for finding compatible roommates
- Ride Sharing for cost-effective transportation
- Lost and Found for managing lost belongings

## Technical Stack Overview:
- Hardware-  Server, storage 
- System- web application 
- Programming Languages 
- Front end- JavaScript, HTML, CSS, Bootstrap 
- Back end- Python			
- Database- SQLite					
- Frameworks- Django
- Code editor- Visual Studio Code
- Source control - Github

## Instructions

1. Create a virtual environment

   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Make migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server

   ```bash
   python manage.py runserver
   ```

7. Open the browser and go to http://127.0.0.1:8000/



### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1 | [requirements.txt](requirements.txt)   | file that holds list of dependencies for this project    |


## References
- https://docs.python.org/
