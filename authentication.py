# module to proceed user logins

dict_user = {"999999": "Administrator",
             "888888": "Service Technician",
             "111111": "Leroy Harreh",
             "222222": "Tobias Graetzer",
             "333333": "Bojan Resan",
             "1": ""}


def sign_in_button_event_1():
    sign_in_authent("1")


def sign_in_button_event_2():
    sign_in_authent("2")


def sign_in_button_event_3():
    sign_in_authent("3")


def sign_in_button_event_4():
    sign_in_authent("4")


def sign_in_button_event_5():
    sign_in_authent("5")


def sign_in_button_event_6():
    sign_in_authent("6")


def sign_in_button_event_7():
    sign_in_authent("7")


def sign_in_button_event_8():
    sign_in_authent("8")


def sign_in_button_event_9():
    sign_in_authent("9")


def sign_in_button_event_0():
    sign_in_authent("0")


# psw += psw
# if len(psw) == 6:
#     psw, _ = sign_in_authent(psw)
#     print(psw)


def sign_out_button_event():
    pass


def sign_in_authent(psw):
    psw = psw + psw
    if len(psw) == 6:
        try:
            if psw in dict_user:
                print("psw is: " + psw)
                psw = ""
        except KeyError:
            print("User name or password not wrong or user not existing")