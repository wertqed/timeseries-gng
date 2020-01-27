from flask import Flask, jsonify, render_template, request
import evaluate_on_real
import evaluate_on_math_attributes
from flask import send_file
import os
import zipfile
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='', static_folder="static", template_folder="templates")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return app.send_static_file('/index.html')


@app.route('/gng/evaluate/real', methods=['POST'])
@cross_origin()
def get_clusters_elems():
    record = request.get_json(force=True)
    result_eval = evaluate_on_real.evaluate(record['e_b'], record['e_n'], record['a_max'], record['l'], record['a'],
                                            record['d'], record['passes'])
    return jsonify(result_eval)

@app.route('/gng/evaluate/math', methods=['POST'])
@cross_origin()
def get_clusters_elems_math():
    record = request.get_json(force=True)
    result_eval = evaluate_on_math_attributes.evaluate(record['e_b'], record['e_n'], record['a_max'], record['l'], record['a'],
                                            record['d'], record['passes'])
    return jsonify(result_eval)

@app.route('/gng/image', methods=['GET'])
@cross_origin()
def get_clusters_img():
    path = "visualization/clusters.png"
    return send_file(path, as_attachment=True)


@app.route('/gng/images/zip', methods=['GET'])
@cross_origin()
def get_clusters_archive():
    zipf = zipfile.ZipFile('gng_images.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('visualization/', zipf)
    zipf.close()
    return send_file('gng_images.zip', as_attachment=True)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


if __name__ == '__main__':
    app.run()
