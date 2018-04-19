import os
from flask import Flask, request, render_template, url_for, jsonify
from werkzeug import secure_filename

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html',message='render_template函数还可以传入一个message说明')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123456':
        return render_template('signin-ok.html', username='password')
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/json')
def returnJson():
  return jsonify(username='lofayo', email='87@qq.com', id='42')

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def uploads():
  if request.method == 'GET':
    return render_template('upload.html',message='you can upload some files......')
  if request.method == 'POST':
    f = request.files['file']
    if f and allowed_file(f.filename):
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return render_template('upload.html',message='files uploaded!')
    return render_template('upload.html',message='unsurported format')


# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#   if request.method == 'GET':
#     return render_template('form.html', message='渲染模板中可以传入参数')
#   elif request.method == 'POST':
#     username = request.form['username']
#     password = request.form['password']
#     if username == 'admin' and password == '123456':
#       f = request.files['file']
#       f.save("./uploads/" + secure_filename(f.filename))
#       return render_template('signin-ok.html', username=username)
#     else:
#       return render_template('form.html', message='用户名或密码有误', username=username)  
#       #这里明显有个问题，如若传入多个数据，那又该怎么写？


if __name__ == '__main__':
    app.debug = True
    app.run('localhost', 9000)