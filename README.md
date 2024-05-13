## Pipenv setup
```
$> python -m pip install pipenv
$> python -m pipenv install --python 3.12
$> python -m pipenv run exercise_<num_of_task>/main.py
```
## DB connection
For correct work with database please specify `connection_string` in the `mongo_client.py` for each execrise.
```
connection_string = "mongodb+srv://<username>:<password>@some.cluster.mongodb.net/"
```
