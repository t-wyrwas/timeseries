from twts_api.domain.bucket import Bucket
from twts_api.domain.timeserie import Timeserie
import pytest

def test_bucket_name_can_set():
    bucket = Bucket(name="test_bucket")
    assert bucket.name == "test_bucket"

def test_bucket_name_is_immutable():
    bucket = Bucket(name="test_bucket")
    with pytest.raises(AttributeError):
        bucket.name = "other_name"

def test_bucket_add_adds_timeserie():
    bucket = Bucket(name="test_bucket")
    ts_name = "timeserie1"
    ts = Timeserie(name=ts_name)
    bucket.add(ts)
    assert bucket.get(ts_name) == ts
