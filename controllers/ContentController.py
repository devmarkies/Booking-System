from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
load_dotenv()
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()
db = SQLAlchemy()
content_schema = ContentSchema()
booked_schema = BookedSchema()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)


#Home
def home_index():
    if 'logged_in' in session:
        #contents = Content.query.all()

        websites = Content.query.filter(Content.types == 'website')
        websetting = content_schema.dump(websites,many=True)

        homes = homes = Content.query.filter(Content.types == 'home')
        homesetting = content_schema.dump(homes,many=True)



        return render_template('home/index.html', websetting=websetting, homesetting=homesetting)
    else:
        return abort(401)

def home_update():
    pass


#About

#Service



def book_now():
    data = request.get_json()
    check_mo = Booked.query.filter(Booked.service == data['service_id'],Booked.booked_date == data['book_date']  )
    res = booked_schema.dump(check_mo,many=True)

    if (len(res) == 0):
        cursor.execute("INSERT INTO `booked`(`name`, `service`, `contact_no`, `booked_date`, `is_confirm`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s)",([data['name'],data['service_id'],data['contact_no'],data['book_date'],'1',nows, nows]))
        cnx.commit()
        return '1'
    else:
        return '0'

def booked_index():
    
    bookedList = Booked.query.order_by(Booked.id.desc()).all()
    return render_template('booked/index.html', data=bookedList)
