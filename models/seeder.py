from werkzeug.security import generate_password_hash
from datetime import date, datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from Models import *
import os

load_dotenv()
DB_URL = "mysql+pymysql://{}:{}@localhost/{}".format(os.getenv("DB_USERNAME"),os.getenv("DB_PASSWORD"),os.getenv("DB_DATABASE"))
engine = create_engine(DB_URL)
local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
db = local_session()
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
wala = None



seeds =[

    ##Users
    Admin(email='zhie@caz.com', username='admin', password=generate_password_hash('password', method='md5'), access='developer', active=1),




    #Home
    Content(id = 1 ,name='Web Title', types='website' ,content='BlackList'),
    Content(id = 2 ,name='Web Icon', types='website' ,content='none'),
    Content(id = 3 ,name='Home Greeting', types='home' ,content='Hello! we are'),
    Content(id = 4 ,name='Home Ownwer', types='home' ,content='Blacklist Productions'),
    Content(id = 5 ,name='Home Position', types='home' ,content='Photography Catering Team'),
    Content(id = 6 ,name='Home Image', types='home', content='bitoy.jpg'),
    Content(id = 7 ,name='About Description', types='about', content='awit'),
    Content(id = 8 ,name='About Image', types='about', content='logoofficial1.png'),
    
   
]
  
db.bulk_save_objects(seeds)

db.commit()
db.close()
print("Successfully added a new post")