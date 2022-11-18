from uuid import uuid4
from json import loads, dumps
import httpx


hostname = "localhost"
port = "8080"
bucket_endpoint = "api/v1/metadata/buckets"


def test_add_new_bucket_list_new_bucket():
    bucket_name = str(uuid4())
    client = httpx.Client()

    response_to_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}", params={'name': bucket_name}, headers={'accept': 'application/json'})
    assert response_to_post.status_code == 201, f"POST request to create new bucket should return 201 status code"

    response_to_get = client.get(url=f"http://{hostname}:{port}/{bucket_endpoint}")
    assert response_to_get.status_code == 200, f"GET request on {bucket_endpoint} should return 200 status code"
    content_str = response_to_get.content.decode('utf8').replace("'", "\"")
    content = loads(content_str)
    returned_bucket = next(filter(lambda b: b['name'] == bucket_name, content))
    assert returned_bucket, "the added bucket should be on the list of existing buckets"


def test_add_bucket_second_time_returns_400():
    bucket_name = str(uuid4())
    client = httpx.Client()

    response_to_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}", params={'name': bucket_name}, headers={'accept': 'application/json'})
    assert response_to_post.status_code == 201, f"POST request to create new bucket should return 201 status code"

    response_to_second_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}", params={'name': bucket_name}, headers={'accept': 'application/json'})
    assert response_to_second_post.status_code == 400, f"second POST request on {bucket_endpoint} should return 201 status code"


def test_add_timeserie_to_nonexistent_bucket_returns_400():
    bucket_name = str(uuid4())
    client = httpx.Client()

    timeserie = "{\"name\": \"newtimeserie\", \"unit\": \"kWh\"}"
    response_to_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}/{bucket_name}", headers={'accept': 'application/json'}, content=timeserie)
    assert response_to_post.status_code == 400, f"POST request on nonexisting bucket should return 400 status code"


def test_add_timeserie_without_properties_list_timeserie_with_base_properties():
    bucket_name = str(uuid4())
    timeserie_name = str(uuid4())
    client = httpx.Client()

    response_to_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}", params={'name': bucket_name}, headers={'accept': 'application/json'})
    assert response_to_post.status_code == 201, f"POST request to create new bucket should return 201 status code"

    timeserie = {"name": f"{timeserie_name}", "unit": "kWh"}
    response_to_timeserie_post = client.post(url=f"http://{hostname}:{port}/{bucket_endpoint}/{bucket_name}", headers={'accept': 'application/json'}, content=dumps(timeserie))
    assert response_to_timeserie_post.status_code == 201, f"first POST request on {bucket_endpoint}/{bucket_name} to add new timeserie should return 201 status code"

    response_to_get = client.get(url=f"http://{hostname}:{port}/{bucket_endpoint}")
    content_str = response_to_get.content.decode('utf8').replace("'", "\"")
    content = loads(content_str)
    returned_bucket = next(filter(lambda b: b['name'] == bucket_name, content))
    timeseries = returned_bucket.get('timeseries', None)

    assert timeseries, f"there should be some timeseries in bucket {bucket_name}"
    returned_timeserie = next(filter(lambda t: t['name'] == timeserie_name, timeseries))
    assert returned_timeserie, f"there should be timeserie {timeserie_name} in the bucket"
    returned_properties = returned_timeserie.get('properties', None)
    assert returned_properties, "the returned timeserie should have properties"
    assert returned_properties.get('average', None) == 0.0, "the returned properties should have average initialized to 0.0"
    assert returned_properties.get('count', None) == 0, "the returned properties should have count initialized to 0"
