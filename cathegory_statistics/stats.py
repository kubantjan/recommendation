from utils import get_cathegories


def calculate_stats_for_items():
    """
    calculates how commonly is an item bought
    :return: dict with key item and value number of purchases
    """

    pass


def save_stats(stats):
    pass


def update_cathegory_statistics():
    cats = get_cathegories()
    for cat in cats:
        stats = calculate_stats_for_items()
        save_stats(stats)
