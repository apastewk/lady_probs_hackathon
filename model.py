"""Models and database functions for Galvanize's Lady Problems Hackathon."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    first_name = db.Column(db.String(30),
                           nullable=False)

    last_name = db.Column(db.String(30),
                          nullable=False)

    username = db.Column(db.String(64),
                         unique=True,
                         nullable=False)

    password = db.Column(db.String(200),
                         nullable=False)

    profile_img = db.Column(db.String(200),
                            nullable=True)

    email = db.Column(db.String(64),
                      unique=True,
                      nullable=False)

    time_zone = db.Column(db.String(25),
                          nullable=True)

    # Define relationship tasks table
    tasks = db.relationship("Task",
                            backref=db.backref("users"))

    # Define relationship goal table
    goal = db.relationship("Goal",
                           backref=db.backref("users"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s username=%s email=%s>" % (self.user_id,
                                                           self.username,
                                                           self.email)


    def check_by_userid(cls, user_id):
        """Search user table by user_id"""

        return cls.query.filter(cls.user_id == user_id).one()



############################################################################
def init_app():

    from server import app

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app, db_uri='postgres:///phones'):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    from server import app

    # Need to add to db.create_all()

    connect_to_db(app, "postgresql:///phones")
    print "Connected to DB."
