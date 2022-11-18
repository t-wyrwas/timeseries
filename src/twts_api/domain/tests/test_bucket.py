from twts_api.domain.bucket import Bucket
from twts_api.domain.timeserie import Timeserie

def test_bucket_holds_a_name():
    bucket = Bucket(name="test_bucket")
    assert bucket.name == "test_bucket"

def test_bucket_holds_added_timeseries():
    bucket = Bucket(name="test_bucket")
    ts1 = Timeserie(name="timeserie1", unit="kWh", properties={})
    ts2 = Timeserie(name="timeserie2", unit="kWh", properties={})
    bucket.add(ts1)
    bucket.add(ts2)
    assert bucket.get_by(ts1.name) == ts1
    assert bucket.get_by(ts2.name) == ts2

def test_bucket_returns_none_for_unknown_timeserie():
    bucket = Bucket(name="test_bucket")
    assert bucket.get_by("unknown") == None
