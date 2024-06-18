from flask import Flask, render_template,session,url_for,redirect
from flask_migrate import Migrate
from models.Models import db
from routes.web import auth,dashboards,contents
from jinja2 import Environment

##############
from models.Models import *
from models.Schema import *
content_schema = ContentSchema()
service_schema = ServiceSchema()
#############

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(dashboards, url_prefix='/dashboard')
app.register_blueprint(contents, url_prefix='/content')





###################################################





@app.route('/')
def index():
    websites = Content.query.filter(Content.types == 'website')
    websetting = content_schema.dump(websites,many=True)

    homes = Content.query.filter(Content.types == 'home')
    homesetting = content_schema.dump(homes,many=True)

    abouts = Content.query.filter(Content.types == 'about')
    aboutsetting = content_schema.dump(abouts,many=True)

    services = Service.query.all()
    servicesetting = service_schema.dump(services,many=True)

    return render_template('front_view/index.html',websetting=websetting, homesetting=homesetting, aboutsetting=aboutsetting, servicesetting=servicesetting)
    
@app.errorhandler(401)
def unauthorized(e):
    return redirect(url_for('auth.login'))



# Custom filter function
def separate_by_pipe(value, index):
    if '|' in value:
        return value.split('|')[index]
    else:
        modify_value = value + "|No Time Indicated"
        return modify_value.split('|')[index]
   

# Register the custom filter with Jinja
app.jinja_env.filters['separate_by_pipe'] = separate_by_pipe


if __name__ == '__main__':
    app.debug = True
    app.run()


















