def get_predictions():
    """get predictions from db
    """
    pass


def is_available(cat):
    """returns whether items are available from cat
    """
    pass


def get_top_available(cat, stats):
    """loads available stuff from cat and returns the top one according to stats
    """
    pass


def get_cat_stats(cat):
    """gets stats about cathegory
    """
    pass


def prediction_for_user(user_id):
    preds = get_predictions(user_id)
    pred_count=0
    items=[]
    for pred in preds:
        if pred_count == N_RECOMMENDED:
            break
        if is_available(pred.cat):
            pred_count+=1
            stats = get_cat_stats(pred.cat)
            items.append(get_top_available(pred.cat, stats))

