import sqlitedict


class UserSession:

    logindb = None

    def __init__(self):
        self.logindb = sqlitedict.SqliteDict('./resteasyLogin.sqlite', autocommit=True)
        pass

    def get_user_session(self):
        return self.logindb

    def login(self, username, is_admin = False):
        # self.setup_or_logout()
        self.logindb["username"] = username
        self.logindb["is_admin"] = is_admin
        self.logindb.commit()
        return True

    def setup_or_logout(self):
        self.logindb["username"] = None
        self.logindb["is_admin"] = False
        self.logindb.commit()
        return True

    def check_login(self):
        if self.logindb["username"]:
            return True
        else:
            print(self.logindb["username"])
            return False

    def check_admin(self):
        if self.logindb["username"] is not None and self.logindb["is_admin"] == True:
            return True
        else:
            return False

    def loggedIn_User(self):
        return self.logindb["username"]