from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import DateTime
db = SQLAlchemy()


#===================================================
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(25))
    password = db.Column(db.String(300))
    access = db.Column(db.String(50))
    active = db.Column(db.String(1))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'username' : self.username,
            'password' : self.password,
            'access' : self.access,
            'active' : self.active,
        }



#===================================================
class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    types = db.Column(db.String(500))
    content = db.Column(db.String(300))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'types' : self.types,
            'content' : self.content,
            
                   }


class Booked(db.Model):
    __tablename__ = 'booked'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    service = db.Column(db.String(500))
    contact_no = db.Column(db.String(300))
    booked_date = db.Column(db.String(300))
    is_confirm = db.Column(db.String(300))


    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'service' : self.service,
            'contact_no' : self.contact_no,
            'booked_date' : self.booked_date,
            'is_confirm' : self.is_confirm,
                   }

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    desc = db.Column(db.String(500))
    image_p = db.Column(db.String(300))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'desc' : self.desc,
            'image_p' : self.image_p,
                   }

class Pricing(db.Model):
    __tablename__ = 'pricing'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.String(500))
    desc = db.Column(db.String(500))
    price = db.Column(db.String(300))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'service_id' : self.service_id,
            'desc' : self.desc,
            'price' : self.price,
                   }
