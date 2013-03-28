from application import create_app
import os


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    create_app().run(debug=True, port=port)
