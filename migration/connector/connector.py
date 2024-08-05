import xmlrpc.client
import ssl
def connect(url: str, db: str, username: str, password: str) -> tuple[str, str]:
    print("Importing conector package...")
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url), context=ssl._create_unverified_context())
    uid = common.authenticate(db, username, password, {})
    print(f"Uid, {uid}")
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url), context=ssl._create_unverified_context())
    return models, uid
