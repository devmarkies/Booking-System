from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from datetime import datetime, date
from sqlalchemy import func

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def dashboad_index():
    if 'logged_in' in session:
        today_str = datetime.now().strftime('%Y-%m-%d')
        today = date.today()
        pending_count = Booked.query.filter_by(is_confirm="0").count()
        today_count = Booked.query.filter_by(is_confirm='1').filter(func.substr(Booked.booked_date, 1, 10) == today_str).count()
        new_book_today_count = Booked.query.filter(func.date(Booked.created_at) == today).count()
        countarr = [new_book_today_count, today_count,pending_count]
        
        bookedList = Booked.query.filter_by(is_confirm='1').filter(func.substr(Booked.booked_date, 1, 10) == today_str).all()
        newbook = Booked.query.filter(func.date(Booked.created_at) == today).all()
        
        
        return render_template('dashboard/index.html', data_count=countarr, data=bookedList,data2=newbook)
    else:
        return abort(401)
     
# def dept_count():
#     data = Department.query.count()
#     return custom_response(data, 200)

# def subj_count():
#     data = Subject.query.count()
#     return custom_response(data, 200)

# def course_count():
#     data = Course.query.count()
#     return custom_response(data, 200)
    
# def users_count():
#     data = User.query.count()
#     return custom_response(data, 200)
    
# def student_count():
#     data = User.query.filter_by(access='student').count()
#     return custom_response(data, 200)

# def instructor_count():
#     data = User.query.filter_by(access='instructor').count()
#     return custom_response(data, 200)
    
