from restful_api import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
#from restful_api.models import User, user_schema
#from restful_api import db


app = create_app()

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    #manager.run()
    app.run(debug=True)
    #print(os.path.abspath(os.path.dirname(__file__)))
    #print(User.query.all())
   