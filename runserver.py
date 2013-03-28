from application import create_app
import config


app = create_app(config.ProductionConfig())


if __name__ == '__main__':
    app = create_app(config.DevelopmentConfig())
    app.run(debug=True)
