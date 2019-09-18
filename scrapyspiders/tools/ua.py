from faker import Faker


def get_user_agent():
    return Faker().user_agent()
