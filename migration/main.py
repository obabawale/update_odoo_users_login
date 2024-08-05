from decouple import config
from connector import connector


def update_login(models, db, uid, password) -> None:
    users = models.execute_kw(db, uid, password, 'res.users', 'search_read', [], {'fields': ['name', 'login']})
    for user in users:
        # Before update
        print("Before...", user['login'])
        if not 'asseco.ng' in user['login']:
            continue

        # update user login
        new_login = user['login'].replace('asseco.ng', 'axendit.com')

        # update user login
        # models.execute_kw(db, uid, password, 'res.users', 'write', [
                        #   user['id'], {'login': new_login}])
        # after update
        [new_user] = models.execute_kw(db, uid, password, 'res.users', 'search_read', [
            [['id', '=', user['id']]]], {'fields': ['name', 'login']})
        print(f"After..., {new_user['login']}")
    return True


def main():
    db = config('DB') 
    username = config('USERNAME')
    password = config("PASSWORD") 
    url = config("HOST")
    models, uid = connector.connect(
        url, db, username, password)
    return update_login(models, db, uid, password)


if __name__ == "__main__":
    main()
