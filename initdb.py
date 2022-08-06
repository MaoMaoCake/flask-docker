from app import db,app
# push the app context
app.app_context().push()
# create all the tables for the db
db.create_all()
db.session.commit()