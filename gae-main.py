import wsgiref.handlers

from application import app

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
