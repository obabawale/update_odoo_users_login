from decouple import config
from connector import connector

# Generic model for the update


def update_models(models, db, uid, password) -> None:
    models_to_update = [
        ('res.users', 'email'),
        ('res.partner', 'email'),
        ('hr.employee', 'work_email'),
    ]

    for Model, field in models_to_update:
        records = models.execute_kw(db, uid, password, Model, 'search_read', [
                                    [[field, '!=', False]]], {'fields': ['name', field]})
        for record in records:
            # Before update
            print("Before...", record[field])
            
            if not 'asseco.ng' in record[field]:
                continue

            # update record login
            updated_field_value = record[field].replace(
                'asseco.ng', 'axendit.com')

            # update record login
            models.execute_kw(db, uid, password, Model, 'write', [
                record['id'], {field: updated_field_value}])
            # after update
            [emp] = models.execute_kw(db, uid, password, Model, 'search_read', [
                [['id', '=', record['id']]]], {'fields': ['name', field]})
            
            print(f"After..., {emp[field]}")
    return True


def main():
    db = config('DB')
    username = config('USERNAME')
    password = config("PASSWORD")
    url = config("HOST")
    models, uid = connector.connect(
        url, db, username, password)
    print("Staring the migration of data...")
    update_models(models, db, uid, password)
    print("Updates completed successfully...")


if __name__ == "__main__":
    main()
