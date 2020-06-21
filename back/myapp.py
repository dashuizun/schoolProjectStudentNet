from flask import Flask,render_template
#from app.main import mainIndex

from app import create_app


app = create_app('default')

#app.jinja_env.variable_start_string = '{['
#app.jinja_env.variable_end_string = ']}'

if __name__ == '__main__':
    app.run()