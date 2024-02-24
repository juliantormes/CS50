from seasons import calculate_age_in_minutes
from datetime import date

def test_calculate_age_in_minutes():
    # Corrected test case with proper date formatting
    dob = date(1990, 1, 1)
    current_date = date(2024, 1, 1)
    # We adjust for leap years: 34 years with 8 leap years = 12410 days
    expected_minutes = 12418 * 24 * 60
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes

    # Test case 1
    dob = date(1999, 1, 1)
    current_date = date(2000, 1, 1)
    expected_minutes = 525600  # 365 days * 24 hours/day * 60 minutes/hour
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes

    # Test case 2
    dob = date(2001, 1, 1)
    current_date = date(2003, 1, 1)
    expected_minutes = 1051200  # (2 years * 365 days/year + 1 leap day) * 24 * 60
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes

    # Test case 3
    dob = date(1995, 1, 1)
    current_date = date(2000, 1, 1)
    expected_minutes = 2629440  # (5 years * 365 days/year + 1 leap day) * 24 * 60
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes

    # Test case 4
    dob = date(2020, 6, 1)
    current_date = date(2032, 1, 1)
    expected_minutes = 6092640  # This needs a detailed calculation including leap years
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes

    # Test case 5
    dob = date(1998, 6, 20)
    current_date = date(2000, 1, 1)
    expected_minutes = 806400  # This needs a detailed calculation
    assert calculate_age_in_minutes(dob, current_date) == expected_minutes
