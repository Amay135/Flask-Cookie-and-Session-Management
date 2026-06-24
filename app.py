from flask import Flask, request, make_response, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/set_cookie')
def set_cookie():
    # Membuat response dan mengatur cookie
    resp = make_response('Cookie "AMAY" telah diatur.')
    resp.set_cookie('AMAY', 'AIMAY FOUNDER', max_age=60 * 60) 
    return resp

@app.route('/get_cookie')
def get_cookie():
    amay_value = request.cookies.get('AMAY') 
    if amay_value:
        return f'Cookie "AMAY" adalah: {amay_value}'
    return 'Cookie "AMAY" tidak ditemukan.'

@app.route('/update_cookie')
def update_cookie():
    resp = make_response('Cookie "AMAY" telah diperbarui.')
    resp.set_cookie('AMAY', 'Updated Value', max_age=60 * 60)
    return resp

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('Cookie "AMAY" telah dihapus.')
    resp.set_cookie('AMAY', '', expires=0)
    return resp

@app.route('/set_session')
def set_session():
    session.permanent = True 
    session['user'] = 'AMAR'
    return 'Session "user" telah diatur dengan nilai "AMAR".'

@app.route('/get_session')
def get_session():
    user = session.get('user')
    if user:
        return f'Session "user" adalah: {user}'
    return 'Session "user" tidak ditemukan.'

@app.route('/update_session')
def update_session():
    if 'user' in session:
        session['user'] = 'AMAR' 
        return 'Session "user" telah diperbarui menjadi "AMAR".'
    return 'Session "user" tidak ditemukan untuk diperbarui.'

# Route untuk clear session
@app.route('/clear_session')
def clear_session():
    session.clear()
    return 'Semua session telah dihapus.'

if __name__ == '__main__':
    app.run(debug=True)
