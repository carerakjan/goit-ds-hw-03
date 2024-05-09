from mongo_client import client
import crud

db = client.hbs_exercise_1
cats = db.cats


if cats.count_documents({}) == 0:
    crud.insert_docs(
        cats,
        [
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
            },
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
            {
                "name": "Murzik",
                "age": 1,
                "features": ["ходить в лоток", "дає себе гладити", "чорний"],
            },
        ],
    )

print("\n--READ ALL --\n")
for c in crud.read_all(cats):
    print(c)

print("\n--READ BY NAME --\n")
print(crud.read_by_name(cats, "barsik"))

# update age
crud.update_age_by_name(cats, "barsik", 9)
print("\n--READ BY NAME AFTER UPDATE AGE --\n")
print(crud.read_by_name(cats, "barsik"))

# add feature
crud.update_features_by_name(cats, "barsik", "спить весь день")
print("\n--READ BY NAME AFTER UPDATE FEATURES --\n")
print(crud.read_by_name(cats, "barsik"))
# remove last added feature
crud.delete_feature_by_name(cats, "barsik", "спить весь день")

# remove by name
crud.delete_by_name(cats, "barsik")
print("\n--READ ALL AFTER REMOVING ONE --\n")
for c in crud.read_all(cats):
    print(c)
    
# remove all
crud.delete_all(cats)