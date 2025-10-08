from flask import Flask, render_template, request, jsonify,session
import os
app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        teamcode = request.form['teamcode']
        session["teamcode"] = teamcode
        return render_template('team.html')
    return render_template('index.html')
@app.route("/getimage", methods=['GET'])
def get_image_question():
    teamcode=session.get("teamcode",None)
    if teamcode is None:
        return jsonify({"error": "Team code not found"}), 400
    image = f"images/{teamcode}.jpg"
    return jsonify({"image": '/static/' + image})

@app.route("/submit", methods=['POST'])
def image_submit():
    data = request.get_json()
    user_answer = data.get("answer")
    # You can process/save the answer here
    print(f"User submitted: {user_answer}")
    # Respond back to frontend
    return jsonify({"status": "success", "message": "Thanks for submitting!"})

if __name__ == '__main__':
    app.run(debug=True)
