from application import create_app
from application.models import db
import config


app = create_app(config.ProductionConfig())


# XXX: A special development route to be used to
# rebuild the database.
@app.route('/db-rebuild')
def db_rebuild():
    db.drop_all()
    db.create_all()
    return "Database rebuilt!"


if __name__ == '__main__':
    app = create_app(config.DevelopmentConfig())

    # XXX: A special development route to be used to
    # rebuild the database.
    @app.route('/db-rebuild')
    def dev_db_rebuild():
        db.drop_all()
        db.create_all()
        return "Database rebuilt!"

    app.run(debug=True)
