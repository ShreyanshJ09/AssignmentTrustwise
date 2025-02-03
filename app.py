from flask import Flask, render_template, request, jsonify
from cal_toxic import detect_toxic
from cal_gibberish import detect_gibberish
from datetime import datetime

app = Flask(__name__)


sample_records = [
    {
        'id': 1,
        'text': "This is a sample comment.",
        'toxicity_score': 0.3,
        'gibberish_score': 0.1,
        'timestamp': datetime.utcnow()
    },
    {
        'id': 2,
        'text': "Another comment here.",
        'toxicity_score': 0.2,
        'gibberish_score': 0.05,
        'timestamp': datetime.utcnow()
    },
    # Add more records here as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():

    input_text = request.form.get('text-input')

    toxicity_result = detect_toxic(input_text)

    gibberish_result = detect_gibberish(input_text)


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

    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    paginated_records = sample_records[start:end]

    return render_template('history.html', records=paginated_records)


if __name__ == '__main__':
    app.run(debug=True)