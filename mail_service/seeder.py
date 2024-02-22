from random import randint, choice
from string import ascii_lowercase


from mail_service.models import Recipient


def seed_recipients(amount):
    for _ in range(amount):
        email = get_fake_email()
        name, surname = get_fake_full_name()
        comment = get_fake_comment()
        Recipient.objects.create(email=email, full_name=f"{name} {surname}", comment=comment)


def get_fake_email():
    letters_amounts = (randint(4, 10), randint(4, 6), randint(2, 3))
    fake_email = ''
    for index, amount in enumerate(letters_amounts):
        for _ in range(amount):
            fake_email += choice(ascii_lowercase)
        if index == 0:
            fake_email += '@'
        elif index == 1:
            fake_email += '.'
    return fake_email


def get_fake_full_name():
    letters_amounts = (randint(4, 10), randint(4, 10))
    fake_full_name = []
    for amount in letters_amounts:
        fake_full_name.append(create_fake_word(amount).capitalize())
    return fake_full_name


def get_fake_comment():
    words_amount = (randint(4, 10))
    fake_comment = []
    for _ in range(words_amount):
        letters_amount = (randint(4, 10))
        fake_comment.append(create_fake_word(letters_amount))
    return ' '.join(fake_comment).capitalize()


def create_fake_word(letters_amount):
    fake_word = [choice(ascii_lowercase) for _ in range(letters_amount)]
    return ''.join(fake_word)
