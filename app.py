import os

from flask import Flask

from cathegory_statistics.stats import update_cathegory_statistics
from configuration.config import load_conf
from model.model import fit_model_and_create_predictions
from prediction.prediction import prediction_for_user

app = Flask(__name__)


@app.route('/update', methods=['POST'])
def update():
    fit_model_and_create_predictions()
    update_cathegory_statistics()


@app.route('/predict/<usr_id>', methods=['GET'])
def predict(usr_id):
    return prediction_for_user(usr_id)


if __name__ == '__main__':
    load_conf(app)
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
