from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cal_toxic import detect_toxic  # Import toxicity score function
from cal_gibberish import detect_gibberish  # Import gibberish detection function
import  os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///output.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    toxicity_score = db.Column(db.Float, nullable=False)
    gibberish_score = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_text():
    input_text = request.form.get('text-input')

    toxicity_result = detect_toxic(input_text)

    gibberish_result = detect_gibberish(input_text)

    output_entry = Output(
        text=input_text,
        toxicity_score=toxicity_result["score"],
        gibberish_score=gibberish_result["score"]
    )
    db.session.add(output_entry)
    db.session.commit()

    result = {
        "toxicity": {
            "score": toxicity_result["score"]
        },
        "gibberish": {
            "score": gibberish_result["score"]
        }
    }

    return jsonify(result)


@app.route('/history')
def history():
    page = request.args.get('page', 1, type=int)

    records = Output.query.order_by(Output.timestamp.desc()).paginate(page=page, per_page=10)

    return render_template('history.html', records=records)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port,debug=True)
    # app.run(debug=True)
