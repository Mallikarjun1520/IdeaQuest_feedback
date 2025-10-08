from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team_name = request.form['team_name']
        topic_name = request.form['topic_name']
        # send to team page
        return render_template('team.html', team_name=team_name, topic_name=topic_name)
    return render_template('index.html')


@app.route('/feedback', methods=['POST'])
def feedback():
    # (Optional) handle form inputs later — render the thank-you template so
    # the user sees the styled confirmation page (templates/thankyou.html).
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
