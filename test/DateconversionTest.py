import orekit
orekit.initVM()

from orekit.pyhelpers import absolutedate_to_datetime, datetime_to_absolutedate

from org.orekit.time import TimeScalesFactory, AbsoluteDate, TimeOffset
from java.util.concurrent import TimeUnit


from datetime import datetime, timezone, timedelta


# This test tests the AbsoluteDate to datetime conversion and vice versa
# The routines are in pyhelpers.py

# Setup Orekit
from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir("resources")

utc = TimeScalesFactory.getUTC()


def test_absolutedate_to_datetime_and_back():
    # Create an AbsoluteDate
    orekit_date = AbsoluteDate("2024-12-19T21:42:55.145Z", utc)

    # Convert to datetime
    dt = absolutedate_to_datetime(orekit_date)

    # Check the conversion
    assert dt.microsecond == 145000
    assert dt.year == 2024
    assert dt.month == 12
    assert dt.day == 19
    assert dt.hour == 21
    assert dt.minute == 42
    assert dt.second == 55
    # Convert back to AbsoluteDate
    orekit_date_back = datetime_to_absolutedate(dt)
    # Check the conversion back
    assert orekit_date_back.getComponents(utc).getDate().getYear() == 2024
    assert orekit_date_back.getComponents(utc).getDate().getMonth() == 12
    assert orekit_date_back.getComponents(utc).getDate().getDay() == 19
    assert orekit_date_back.getComponents(utc).getTime().getHour() == 21
    assert orekit_date_back.getComponents(utc).getTime().getMinute() == 42
    assert orekit_date_back.getComponents(utc).getTime().getSplitSecond().getRoundedTime(TimeUnit.MICROSECONDS) == 55145000

def test_leap_second():
    # Test a leap second date
    orekit_date = AbsoluteDate("2016-12-31T23:59:60.000Z", utc)

    # Convert to datetime
    dt = absolutedate_to_datetime(orekit_date)

    # Convert back to AbsoluteDate
    orekit_date_back = datetime_to_absolutedate(dt)

    assert orekit_date.durationFrom(orekit_date_back) ==-1.0  # datetime do not support leap seconds, so the duration will be -1 second

def test_datetime_weakness():
    # Datetime objects in Python do not support leap seconds
    # This test is more an example of the limitation rather than a failure

    from datetime import datetime, timedelta, timezone

    start = datetime(2016, 12, 31, 23, 59, 30)
    delta = timedelta(seconds=35)
    end = start + delta

    start_ad = AbsoluteDate("2016-12-31T23:59:30", utc)
    end_ad = start_ad.shiftedBy(35.0)

    assert absolutedate_to_datetime(end_ad) < end  # end_ad will be one second before the end due to leap second

def test_tz_aware_utc_datetime_to_absolutedate():
    # Test with a timezone-aware datetime
    dt = datetime(2024, 12, 19, 21, 42, 55, 145000, tzinfo=timezone.utc)

    # Convert to AbsoluteDate
    orekit_date = datetime_to_absolutedate(dt)

    # Check the conversion
    assert orekit_date.getComponents(utc).getDate().getYear() == 2024
    assert orekit_date.getComponents(utc).getDate().getMonth() == 12
    assert orekit_date.getComponents(utc).getDate().getDay() == 19
    assert orekit_date.getComponents(utc).getTime().getHour() == 21
    assert orekit_date.getComponents(utc).getTime().getMinute() == 42
    assert orekit_date.getComponents(utc).getTime().getSplitSecond().getRoundedTime(TimeUnit.MICROSECONDS) == 55145000

def test_tz_local_datetime_to_absolutedate():
    # Test with a timezone-aware datetime in local timezone
    dt = datetime(2024, 12, 19,
                  22, 42, 55, 145000,
                  tzinfo=timezone(timedelta(hours=1))) # UTC+1

    # Convert to AbsoluteDate
    orekit_date = datetime_to_absolutedate(dt)

    # Check the conversion
    assert orekit_date.getComponents(utc).getDate().getYear() == 2024
    assert orekit_date.getComponents(utc).getDate().getMonth() == 12
    assert orekit_date.getComponents(utc).getDate().getDay() == 19
    assert orekit_date.getComponents(utc).getTime().getHour() == 21
    assert orekit_date.getComponents(utc).getTime().getMinute() == 42
    assert orekit_date.getComponents(utc).getTime().getSplitSecond().getRoundedTime(TimeUnit.MICROSECONDS) == 55145000

def test_absolutedate_to_datetime_with_tz():
    # Create an AbsoluteDate
    orekit_date = AbsoluteDate("2024-12-19T21:42:55.145Z", utc)

    # Convert to datetime with timezone
    dt = absolutedate_to_datetime(orekit_date, tz_aware=True)

    # Check the conversion
    assert dt.tzinfo is not None
    assert dt.tzinfo.utcoffset(dt) == timedelta(0)  # UTC timezone
    assert dt.microsecond == 145000
    assert dt.year == 2024
    assert dt.month == 12
    assert dt.day == 19
    assert dt.hour == 21
    assert dt.minute == 42
    assert dt.second == 55