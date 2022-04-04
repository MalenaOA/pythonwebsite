from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__) #__main__

# @app.route('/')
# def hello_world():
#     return 'Hello, Malena!'

# @app.route('/')
# def hello_world():
#     return render_template('oldindex.html')
#
# # # Terminal
# # '''
# # PS C:\Users\Malena-NUC\Desktop\Python Course\19_WebDevelopment\WebServer> $env:FLASK_APP = "server.py"
# # PS C:\Users\Malena-NUC\Desktop\Python Course\19_WebDevelopment\WebServer> flask run
# #  * Serving Flask app 'server.py' (lazy loading)
# #  * Environment: production
# #    WARNING: This is a development server. Do not use it in a production deployment.
# #    Use a production WSGI server instead.
# #  * Debug mode: off
# #  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
# # 127.0.0.1 - - [01/Apr/2022 13:51:22] "GET / HTTP/1.1" 200 -
# # 127.0.0.1 - - [01/Apr/2022 13:51:22] "GET /favicon.ico HTTP/1.1" 404 -
# # '''
#
# # # Debug Mode -> to show changes immediately
# # '''
# # ERROR - flask run --debugger
# # PS C:\Users\Malena-NUC\Desktop\Python Course\19_WebDevelopment\WebServer> $env:FLASK_APP = "development"
# # PS C:\Users\Malena-NUC\Desktop\Python Course\19_WebDevelopment\WebServer> flask run
# #  * Serving Flask app 'development' (lazy loading)
# #  * Environment: production
# #    WARNING: This is a development server. Do not use it in a production deployment.
# #    Use a production WSGI server instead.
# #  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
# #  * Restarting with stat
# #  * Debugger is active!
# #  * Debugger PIN: 121-955-027
# # '''
#
# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dog'
#
# @app.route('/about')
# def about():
#     return render_template('oldabout.html')
#
# # in html files {{}} converts to python expressions
#
# @app.route('/<username>/<int:post_id>')
# def name(username=None, post_id=None):
#     return render_template('oldindex.html', name=username, post_id=post_id)

# ------- #
# Using Universe HTLM/CSS/JS template

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('work.html')

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "try again"
