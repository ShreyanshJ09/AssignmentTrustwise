from flask import Flask, render_template, request, jsonify
from cal_toxic import detect_toxic
from cal_gibberish import detect_gibberish

app = Flask(__name__)

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




if __name__ == '__main__':
    app.run(debug=True)