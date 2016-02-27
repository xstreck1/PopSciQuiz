from flask import Flask, session, redirect, url_for, escape, request
import os, json

players_count = 0
runid = os.urandom(32)
app = Flask(__name__)
question_no = -1
answers = []

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

@app.route('/question.html')
def question():
    return app.send_static_file('question.html')

@app.route('/result.html')
def results():
    global answers
    print('results')
    return app.send_static_file('result.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/controller.html')
def controller():
    return app.send_static_file('controller.html')

@app.route('/answer/<int:post_id>', methods=['POST'])
def answer(post_id):
    global question_no
    global answers
    if question_no != -1:
        print(session['username'] + ":" + str(post_id))
        answers[question_no][session['username']] = post_id
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/new_question', methods=['POST'])
def new_question():
    global question_no
    global answers
    question_no += 1
    answers.append({})
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

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
