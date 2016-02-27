from flask import Flask, session, redirect, url_for, escape, request
import os

players_count = 0
runid = os.urandom(32)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    global players_count, runid
    if 'runid' not in session or session['runid'] != runid:
        session.pop('username', None)
        session['runid'] = runid
    if 'username' not in session:
    # if True:
        if request.method == 'POST':
            players_count += 1
            session['username'] = request.form['username']
            return redirect(url_for('player_view'))
        else:
            return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
    else:
        return redirect(url_for('player_view'))

@app.route('/player_view')
def player_view():
    if 'runid' not in session or session['runid'] != runid or 'username' not in session:
        return redirect(url_for('login'))
    else:
        return app.send_static_file('player_view.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/controller')
def contoller():
    return app.send_static_file('controller.html')

#@app.route('/reset')
#def reset():
#    players_count = 0
#    app.secret_key = os.urandom(32)
#    return ''

@app.route('/player_count')
def get_player_count():
    global players_count
    return str(players_count)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='192.168.2.236', port="35123")
