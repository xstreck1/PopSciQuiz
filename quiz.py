from flask import Flask, session, redirect, url_for, escape, request
import os, json

players = []
runid = os.urandom(32)
app = Flask(__name__)
question_no = -1
answers = []
correct_answers = [1,3,4,2,2]

@app.route('/', methods=['GET', 'POST'])
def login():
    global players, runid
    if 'runid' not in session or session['runid'] != runid:
        session.pop('username', None)
        session['runid'] = runid
    if 'username' not in session:
    # if True:
        if request.method == 'POST':
            session['username'] = request.form['username']
            players.append(session['username'])
            return redirect(url_for('player_view'))
        else:
            return '''
            <form action="" method="post" >
                <p><input type=text name=username style="font-size: 50pt;">
                <p><input type=submit value=Login style="font-size: 50pt;">
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
    global answers
    global question_no
    answers = []
    question_no = -1
    return app.send_static_file('question.html')

@app.route('/result.html')
def results():
    global answers
    global players
    global question_no
    result = '<div style="font-size: 50pt">'
    for player in players:
        score = 0
        for question_i in range(0, question_no + 1):
            if player in answers[question_i] and answers[question_i][player] == correct_answers[question_i]:
                score += 1
        result += '<div>' + player + ' ' + str(score) + '</div>'
    result += '</div>'
    return result


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
    global players
    return ", ".join(players)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='192.168.2.236', port="35123")
