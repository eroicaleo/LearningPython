
# This note is about the date time

* I have been asked once
* Some problem like `539_Minimum_Time_Difference.py`

## Find the difference between two time, only hours and seconds

* This is the problem of `539_Minimum_Time_Difference.py`
* Python `datetime` module implemented `__sub__` method
* It started on line 2088
* It returns a `timedelta` object
* Then `timedelta` align everything to seconds, and we can use this approach

## Find the difference between two time, only days, i.e. year/month/day

* Python `datetime`'s `__sub__` method uses `toordinal` which in turn uses `_ymd2ord`
* When it computes years, it uses `y*365 + y//4 - y//100 + y//400` which is very smart.
  This works even when year is 0 or negative.
* To calculate the month before the current month, it uses a list to quickly get the days

```python
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

_DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
dbm = 0
for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim

def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _days_before_year(year):
    "year -> number of days before January 1st of year."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400

def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 12, month
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]

def _days_before_month(year, month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 12, 'month must be in 1..12'
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))

def _ymd2ord(year, month, day):
    "year, month, day -> ordinal, considering 01-Jan-0001 as day 1."
    assert 1 <= month <= 12, 'month must be in 1..12'
    dim = _days_in_month(year, month)
    assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
    return (_days_before_year(year) +
            _days_before_month(year, month) +
            day)

days1 = self.toordinal()
days2 = other.toordinal()
```

## Convert a day to year/month/day

* This is more complex, so skip it for now.

