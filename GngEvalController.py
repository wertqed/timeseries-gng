from flask import Flask, jsonify
import evaluate_on_real

app = Flask(__name__)


@app.route('/gng/evaluate', methods=['GET', 'POST'])
def hello_world():
    result_eval = evaluate_on_real.evaluate()
    for elem in result_eval[:, 0]:
        elem = elem.tolist()
    return jsonify(result_eval)


if __name__ == '__main__':
    app.run()
