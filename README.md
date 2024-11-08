**Greetings!** This is a short test application developed to manage Spy Cat Agency. This project was created for DevelopsToday IT company.     
    
**Tech Overview**     
- Framework    
    - DRF     
- Database     
    - PostgreSQL     
- Validations      
    - Validate cat’s breed with https://api.thecatapi.com/v1/breeds    
- Environment    
    - Dockerized setup for easy deployment and consistent development environment     
- Dependencies    
   - All necessary libraries are listed in requirements.txt for easy setup and installation.     
*The application adheres to PEP8 standards and utilizes flake8 and isort for code quality and organization.          
         
**WARNING!**       
The `.env` file is **NOT** pushed to GitHub. This file must include the following items:       
- `SECRET_KEY`='django-SECRET_KEY-example'     
- `DEBUG`=True/False     
- `DB_HOST`=db            
- `DB_NAME`=devdb     
- `DB_USER`=devuser         
- `DB_PASS`=changeme       
- `POSTGRES_DB`=devdbexamlpe          
- `POSTGRES_USER`=devuserexamlpe        
- `POSTGRES_PASSWORD`=changeme                   
- `PASSWORD_LENGTH`=8    
**WARNING!**      
     
**How to start?!**     
1)Clone this repository:      
**git clone <repo_url>**     
2)Navigate to the Spy_Cat_Agency folder and run the following command in your terminal:         
**docker-compose up --build**       
3)After the application builds, verify everything is working correctly by running:      
**docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"**      
4)You're all set! Use the available API endpoints to create your Spy Cat Agency.:)      
           
**API endpoints**     
https://interstellar-crescent-112490.postman.co/workspace/lab9~2fedf218-1f46-4058-8f2a-8e307579cb2b/collection/24294621-af5da9e5-a445-40f4-abe5-a6b198e3620b?action=share&creator=24294621         
All endpoints in a Postman collection are sorted by task order.      
*To manage cats, you must register an account. Each cat and mission is assigned to an individual owner. A user cannot manage another user's cats or missions. Guests have limited access and can only log in or register; full functionality is available only to authenticated users.      
    
