"""
>>> dial_codes = [
... (880, 'Bangladesh'),
... (55, 'Brazil'),
... (86, 'China'),
... (91, 'India'),
... (62, 'Indonesia'),
... (81, 'Japan'),
... (234, 'Nigeria'),
... (92, 'Pakistan'),
... (7, 'Russia'),
... (1, 'United States'),
... ]
>>> country_dial = {country: code for code, country in dial_codes}
>>> country_dial # doctest: +NORMALIZE_WHITESPACE
{'Bangladesh': 880, 'Brazil': 55,
'China': 86, 'India': 91, 'Indonesia': 62,
'Japan': 81, 'Nigeria': 234, 'Pakistan': 92,
'Russia': 7, 'United States': 1}
>>> {code: country.upper()
...     for country, code in sorted(country_dial.items())
...     if code < 70}
{55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
