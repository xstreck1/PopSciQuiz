from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

players_count = 0

@app.route('/', methods=['GET', 'POST'])
def login():
    if session and 'username' not in session:
    # if True:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
    else:
        print('trying url')
        return app.send_static_file('player_view.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/controller')
def contoller():
    return app.send_static_file('controller.html')


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='192.168.2.236', port="35123")