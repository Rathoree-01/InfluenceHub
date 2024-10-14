# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# from flask_login import LoginManager, UserMixin

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# db = SQLAlchemy(app)

# # db.init_app(app)

# class Admin(db.Model, UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(20),nullable=False,unique=True)
#     password=db.Column(db.String(80),nullable=False)

# class influencer(db.Model,UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(20),nullable=False)
#     password=db.Column(db.String(80),nullable=False)

# class sponser(db.Model,UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(20),nullable=False)
#     password=db.Column(db.String(80),nullable=False)

# ##Run in command line for creating databases##

# # from make_data import app,db
# # with app.app_context():
# #     db.create_all()

import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('users.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
# cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
create_add_campaign_table = """
CREATE TABLE IF NOT EXISTS add_campaign (
    campaid INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(100) NOT NULL,
    start_date VARCHAR(100) NOT NULL,
    end_date VARCHAR(100) NOT NULL,
    visibility VARCHAR(100) NOT NULL,
    goals VARCHAR(100) NOT NULL
);
"""

create_ad_request_table = """
CREATE TABLE IF NOT EXISTS ad_request (
    id INTEGER PRIMARY KEY,
    camp_id INTEGER NOT NULL,
    influ_id INTEGER NOT NULL,
    messages VARCHAR(100) NOT NULL,
    requirements VARCHAR(100) NOT NULL,
    payment VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL,
    FOREIGN KEY (camp_id) REFERENCES add_campaign (campaid),
    FOREIGN KEY (influ_id) REFERENCES influencer (id)
);
"""

<button class="popup-button" type="submit"><a href="spons_6">Add</a></button>
# inser_1="""INSERT INTO admin values(1,'admin1','admin@1234')

# """
# cursor_obj.execute(inser_1)

# data=cursor_obj.execute('''SELECT * FROM admin''') 
# for row in data: 
#     print(row) 

print("insertion is Ready")
connection_obj.commit()
# Close the connection
connection_obj.close()



{% comment %} <form>
    <div class="tee">
      <label for="fruits">Choose a fruit:</label>
      <select id="fruits">
      {% for value, label in item.items() %}
            <option value="{{ value }}">{{ label }}</option>
        {% endfor %}
      </select>
    </div> 
</div><div class="add">create a new add request</div>
<!--create new add request-->
<button class="add-button" onclick="submitForm()">+</button>
</form>
</div> {% endcomment %}