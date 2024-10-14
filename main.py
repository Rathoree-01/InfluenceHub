from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import InputRequired, Length, EqualTo,ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

db = SQLAlchemy(app)

message=''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Influencer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Sponser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
class add_campaign(db.Model):
    campaid=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), unique=True, nullable=False)
    description=db.Column(db.String(100), unique=True, nullable=False)
    start_date=db.Column(db.String(100), unique=True, nullable=False)
    end_date=db.Column(db.String(100), unique=True, nullable=False)
    visibility=db.Column(db.String(100), unique=True, nullable=False)
    goals=db.Column(db.String(100), unique=True, nullable=False)
    payment=db.Column(db.Integer,nullable=False)
    
class ad_request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camp_id=db.Column(db.Integer,db.ForeignKey('add_campaign.campaid'))
    influ_id=db.Column(db.Integer,db.ForeignKey('influencer.id'))
    messages=db.Column(db.String(100), unique=True, nullable=False)
    requirements=db.Column(db.String(100), unique=True, nullable=False)
    payment=db.Column(db.String(100), unique=True, nullable=False)
    status=db.Column(db.String(100), unique=True, nullable=False)
    name=db.Column(db.String(100), unique=True, nullable=False)
    
# Create the database tables
# with app.app_context():
#     db.create_all()

#     # Example to manually insert users (replace with actual logic)
#     # Ensure to hash passwords before storing in production
#     user1 = User(username='admin1', password=generate_password_hash('admin123'))
   

#     db.session.add(user1)
   
#     db.session.commit()

@app.route('/influ_regis',methods=['GET', 'POST'])
def influ_register():
    message=''
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        industry = request.form['confirm_password']
        existing_usr=Influencer.query.filter_by(username=email).first()
        if existing_usr:
            message="This email is already taken."
        else:
            if industry==password:
                with app.app_context():
                    user1 = Influencer(username=email, password=generate_password_hash(password))  
                    db.session.add(user1)
                    db.session.commit()
                
                return render_template('influencerdashboard.html')
    return render_template('influencer.html',message=message)           

@app.route('/spons_regis',methods=['GET', 'POST'])
def spons_register():
    message=''
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        industry = request.form['confirm_password']
        existing_usr=Sponser.query.filter_by(username=email).first()
        if existing_usr:
            message="This email is already taken."
        else:
            if industry==password:
                with app.app_context():
                    user1 = Sponser(username=email, password=generate_password_hash(password))  
                    db.session.add(user1)
                    db.session.commit()
                
                return redirect(url_for('spons_dash'))
    return render_template('sponsors.html',message=message) 

@app.route('/spons_dash', methods=['GET', 'POST'])
def spons_dash():
    campaigns=add_campaign.query.all()
    return render_template('sponsorboard.html',camp=campaigns)

@app.route('/influ_dash', methods=['GET', 'POST'])
def influ_dash():
    return render_template('influencerdashboard.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with app.app_context():
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                # Correct username and password
                # Redirect to a protected route or home page
                return redirect(url_for('admin_dash'))
            else:
                # Incorrect username or password
                error = 'Invalid username or password'
                return render_template('index.html', error=error)
    else:
        return render_template('index.html')


@app.route('/admin_dash', methods=['GET', 'POST'])
def admin_dash():
     with app.app_context():
        influ=Influencer.query.all()
     if request.method=="POST":
        # influ_username = request.form['username']
        admin_username=request.form.get('username')
        print(admin_username)
        with app.app_context():
            sub = add_campaign.query.filter_by(name=admin_username).first()
            print("fghjkl:",sub.name)
            influ_user=Influencer.query.filter_by(username=admin_username).first()
            if sub and influ_user:
                add1=ad_request(camp_id=sub.campaid,influ_id=influ_user.id,name=influ_username,messages=name,requirements=description,payment=sub.payment,status='pending')
                db.session.add(add1)
                db.session.commit()
                return render_template('admin.html')
    
    

@app.route('/admin_2')
def admin_2():
    return render_template('admin2.html')

@app.route('/user',methods=['GET','POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with app.app_context():
            influ=Influencer.query.filter_by(username=username).first()
            spons=Sponser.query.filter_by(username=username).first()
        
            if influ and check_password_hash(influ.password, password):
               return redirect(url_for('influ_dash'))
            elif spons and check_password_hash(spons.password, password):
                return redirect(url_for('spons_dash'))
            else:
                return render_template('/user.html')
            
    return render_template('user.html')
    

@app.route('/campaigns')
def campaigns():
    return render_template('campaigns.html')

@app.route('/spons_4',methods=['GET','POST'])
def spons_4():
    message=''
    if request.method=='POST':
        print("post called")
        description = request.form['description']
        name = request.form['name']
        start_date = request.form['start']
        end_date = request.form['end']
        visibility = request.form['visibility']
        industry = request.form['goals']
        payment= request.form['payment']
        with app.app_context():
            user1 = add_campaign(name=name, description=description,goals=industry,visibility=visibility,start_date=start_date,end_date=end_date)  
            db.session.add(user1)
            db.session.commit()
            message="Added the campaign."
        return redirect(url_for('spons_dash'))
    return render_template('sponsorD4.html',message=message)

#@app.route('/spons_<item_name>')
@app.route('/spons_<item_name>')
def spons_6(item_name):
    item = {'name': item_name} 
    with app.app_context():
         print("in app")
         sub = add_campaign.query.filter_by(name=item_name).first()
         print("sub is :", sub)
         if sub:
            item = {
                'name': sub.name,
                'description': sub.description,
                'start_date': sub.start_date,
                'end_date': sub.end_date,
                'visibility': sub.visibility,
                'goals': sub.goals
            }
         else:
            item = None
    return render_template('sponsorD6.html', item=item)


@app.route('/spons_3')
def spons_3():
    return render_template('sponsorD3.html')

@app.route('/spons_7')
def spons_7():
    return render_template('sponsorD7.html')

@app.route('/spons_2',methods=['POST','GET'])
def spons_2():
    name = request.args.get('name')
    description= request.args.get('description')
    start=request.args.get('start')
    end=request.args.get('end')
    visibility=request.args.get('visibility')
    goals=request.args.get('goals')
    details = {
                'name': name,
                'description': description,
                'start_date': start,
                'end_date': end,
                'visibility': visibility,
                'goals': goals
            }
    print(details)
    # selected_value = request.args.get('selected')
    with app.app_context():
        influ=Influencer.query.all()
    if request.method=="POST":
        # influ_username = request.form['username']
        influ_username=request.form.get('username')
        print(influ_username)
        with app.app_context():
            sub = add_campaign.query.filter_by(name=name).first()
            print("fghjkl:",sub.name)
            influ_user=Influencer.query.filter_by(username=influ_username).first()
            if sub and influ_user:
                add1=ad_request(camp_id=sub.campaid,influ_id=influ_user.id,name=influ_username,messages=name,requirements=description,payment=sub.payment,status='pending')
                db.session.add(add1)
                db.session.commit()
                return redirect(url_for('spons_dash'))
    return render_template('sponsorD7.html',details=details,influ=influ)
    
@app.route('/spons_5')
def spons_5():
    return render_template('sponsorD5.html')

@app.route('/influ_3')
def influ_3():
    return render_template('influencerD3.html')

@app.route('/influ_2')
def influ_2():
    return render_template('influencerD2.html')

@app.route('/createsign')
def createsign():
    return render_template('createsign.html')


if __name__ == '__main__':
    app.run(debug=True)



#######Passwords and usernames already created######

# Admin:
#     username=admin1, password=admin123

# Influencer
# username=abc@gmail.com, password=abc123

# Sponser
# username=sponser@gmail.com  ,password=abc123