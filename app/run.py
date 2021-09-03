import re
import clipboard
import chromedriver_autoinstaller
from flask import Flask, request, render_template, redirect, jsonify, abort
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
        return render_template('Login.html', mode='form')
    elif request.method == 'POST':
        mode = request.form.get('mode')
        if mode == 'form':
            id = request.form.get('id')
            pw = request.form.get('pw')
            error_msg = login_form(id, pw)
            if error_msg == None:
                return redirect(NAVER_LOGIN_FORMAT[0])
            return render_template('Login.html', mode='form', form_error_msg=error_msg)
        elif mode == 'ones':
            pattern = re.compile('[0-9]{8}')
            key = request.form.get('key')
            length = len(key)
            if length <= 0 or not pattern.match(key) and length <= 0:
                error_msg = '일회용 로그인 번호를 입력하세요.'
                return render_template("Login.html", mode='ones', ones_error_msg=error_msg)
            elif length < 8:
                error_msg = '일회용 로그인 번호를 다시 입력해 주세요.<br>일회용 로그인 번호를 확인한 후 8자리 숫자를 다시 입력해 주세요.'
                return render_template("Login.html", mode='ones', ones_error_msg=error_msg)
            else:
                error_msg = login_ones(key)
                if error_msg == None:
                    return redirect(NAVER_LOGIN_FORMAT[1])
                return render_template("Login.html", mode='ones', ones_error_msg=error_msg)
        return abort(400)

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

@app.route('/qrcode', methods=['GET', 'POST'])
def qrcode():
    if request.method == 'GET':
        driver.get(NAVER_LOGIN_FORMAT[2])
        number = driver.execute_script('''
        return document.getElementsByClassName('point')[0].innerText;
        ''')
        qrImage = driver.execute_script('''
        return window.qrImage.getAttribute('src');
        ''')
        json = {"Status":"Success", "number":number, "qrImage":qrImage}
        return jsonify(json)
    elif request.method == 'POST':
        if driver.current_url == 'https://m.naver.com/':
            json = {"Status":"Success"}
        elif driver.current_url == 'https://nid.naver.com/nidlogin.login?mode=qrcode':
            json = {"Status":"Waiting"}
        elif 'block' in driver.execute_script('return window.reloadGuide.getAttribute("style");'):
            json = {"Status":"Failed"}
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

def login_ones(key):
    global driver
    clipboard.copy(key)
    driver.find_element_by_id('disposable').send_keys(Keys.CONTROL + 'v')
    driver.find_element_by_class_name('btn_login').click()

    if driver.current_url == 'https://nid.naver.com/nidlogin.login':
        msg = driver.execute_script('''
        return window.err_common.innerText;
        ''')
    else:
        msg = None
    return msg

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)