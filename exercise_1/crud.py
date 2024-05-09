def insert_doc(db, data):
    return db.insert_one(data)


def insert_docs(db, docs):
    return db.insert_many(docs)


def read_all(db):
    return list(db.find({}, {"_id": 0}))


def read_by_name(db, name):
    return db.find_one({"name": name}, {"_id": 0})


def update_age_by_name(db, name: str, age: int):
    return db.update_one({"name": name}, {"$set": {"age": age}})


def update_features_by_name(db, name, feature):
    return db.update_one({"name": name}, {"$addToSet": {"features": feature}})


def delete_by_name(db, name):
    return db.delete_one({"name": name})


def delete_feature_by_name(db, name, feature):
    return db.update_one({"name": name}, {"$pull": {"features": feature}})


def delete_all(db):
    return db.delete_many({})
