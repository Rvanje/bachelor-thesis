# module to proceed user logins
import users

lst_auth = []


def sign_in_button_event_1():
    sign_in_authenticator("1")


def sign_in_button_event_2():
    sign_in_authenticator("2")


def sign_in_button_event_3():
    sign_in_authenticator("3")


def sign_in_button_event_4():
    sign_in_authenticator("4")


def sign_in_button_event_5():
    sign_in_authenticator("5")


def sign_in_button_event_6():
    sign_in_authenticator("6")


def sign_in_button_event_7():
    sign_in_authenticator("7")


def sign_in_button_event_8():
    sign_in_authenticator("8")


def sign_in_button_event_9():
    sign_in_authenticator("9")


def sign_in_button_event_0():
    sign_in_authenticator("0")


def sign_out_button_event():
    pass


def sign_in_authenticator(psw):
    lst_auth.append(psw)
    if len(lst_auth) == 6:
        code = "".join(lst_auth)
        try:
            if code in users.dict_user:
                print("Logged in as: " + users.dict_user[code])
                lst_auth.clear()
                return True
            else:
                print("Nope")
                lst_auth.clear()
                return False
        except KeyError:
            print("Nope")
            lst_auth.clear()