"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Python loops, functions, and arguments using the baking delicious lasagna example.
"""

# 1. تعريف الثابت الخاص بوقت الخبز الإجمالي (40 دقيقة)
EXPECTED_BAKE_TIME = 40


# 2. دالة حساب الوقت المتبقي في الفرن
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# 3. دالة حساب وقت التحضير بناءً على عدد الطبقات (كل طبقة تستغرق دقيقتين)
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    This function takes the number of layers you want to add to the lasagna
    and returns how many minutes you would spend making them.
    """
    return number_of_layers * 2


# 4. دالة حساب إجمالي الوقت المنقضي (وقت التحضير + الوقت المنقضي في الفرن)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed kitchen time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and returns the total minutes you've been cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
