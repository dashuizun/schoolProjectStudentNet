from flask import Flask,render_template

app=Flask(__name__,template_folder='../front',static_url_path='/',static_folder='../front/static');

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()