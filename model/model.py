import numpy as np
import scipy
from lightfm import LightFM

from utils import get_cathegories


def get_users():
    """get all users from db"""
    pass


def get_item_index(item, cat):
    """provide index of cat an item"""
    pass


def update_field(param, ago):
    return param + np.exp(COEF * ago)


def get_orders_for_user(user):
    """get all order for user"""
    pass


def u_never_bought_cats(user, sparse_mat):
    """get list of never bought cats for user"""
    pass


def get_top_100(param):
    """top 100 predictions for user"""
    pass


def save_user_prediction(param):
    """save prediction to db"""
    pass


def create_item_matrix(users):
    """
    :return: sparse user cat matrix (every row one user, every column one cathegory, cells likelihood user likes them
    """
    cathegories = get_cathegories()

    sparse_mat = scipy.sparse.csr_matrix(shape=(len(users), len(cathegories)))
    for i, user in enumerate(users):
        order = get_orders_for_user(user)
        for item in order:
            sparse_mat[i, get_item_index(item, cathegories)] = update_field(
                sparse_mat[i, get_item_index(item, cathegories)], order.days_ago)


def fit_model_and_create_predictions():
    model = LightFM(loss='warp')
    users = get_users()
    usr_cat_matrix = create_item_matrix(users)
    model.fit(usr_cat_matrix, epochs=30, num_threads=2)
    for user in users:
        never_bought_cats = u_never_bought_cats(user, usr_cat_matrix)
        save_user_prediction(get_top_100(model.predict(user, never_bought_cats)))
