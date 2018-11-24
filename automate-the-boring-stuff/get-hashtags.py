# enter bunch of words, get hashtags with those words


def get_hashtags():

    words = input('Введи слова через пробел, чтобы получить хештеги. \nЖми Enter, чтобы закончить ввод и получить результат.\t > ')
    words = words.split(' ')
    words = ['#'+ word for word in words]
    words = " ".join(tag for tag in words)
    print(words)

get_hashtags()