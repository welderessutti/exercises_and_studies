def make_shirt(tam, msg):
    print(f"The shirt size is {tam} and the printed message is '{msg}'.")


make_shirt("L", "Message in the bottle!")


def make_shirt(tam="L", msg="I love Python"):
    print(f"The shirt size is {tam} and the printed message is '{msg}'.")


make_shirt()
make_shirt("M")
make_shirt("S", "I'm becoming a software developer!")
