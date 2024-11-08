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
  
