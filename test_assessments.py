import pytest
from data_structures import (
    format_property_listings,
    find_deepest_value,
    audit_user_permissions,
    university_admission_check,
    calculate_fuel_expenses
)

# --- Level 7 Test ---
def test_university_admission_check():
    applicants = [
        {"name": "Washie", "score": 90},
        {"name": "Thembi", "score": 45},
        {"name": "Sipho", "score": 75}
    ]
    result = university_admission_check(applicants, 60)
    assert "APPROVED: WASHIE (90)" in result
    assert "APPROVED: SIPHO (75)" in result
    assert len(result) == 2

# --- Level 8 Test ---
def test_calculate_fuel_expenses():
    logs = [
        {'truck_id': 'A1', 'liters': 100, 'price_per_liter': 20.0, 'business_trip': True},  # 2000
        {'truck_id': 'B2', 'liters': 50, 'price_per_liter': 20.0, 'business_trip': False},  # Skip
        {'truck_id': 'C3', 'liters': 10.5, 'price_per_liter': 20.0, 'business_trip': True}  # 210
    ]
    # Total: 2210.0
    assert calculate_fuel_expenses(logs) == 2210.0

def test_calculate_fuel_expenses_empty():
    assert calculate_fuel_expenses([]) == 0.0

# --- Level 9 Test ---
def test_format_property_listings():
    listings = [
        {'price': 2500000, 'bedrooms': 4, 'available': True},
        {'price': 1200000, 'bedrooms': 2, 'available': False},
        {'price': 950000, 'bedrooms': 1, 'available': True}
    ]
    result = format_property_listings("Midrand", listings)
    assert result[0] == "MIDRAND | R 2,500,000 | 4 BR"
    assert result[1] == "MIDRAND | R 950,000 | 1 BR"
    assert len(result) == 2

# --- Level 10 Test ---
def test_find_deepest_value():
    data = {
        'level1': 'info',
        'metadata': {
            'author': 'Washie',
            'details': {'secret_code': 9999}
        }
    }
    assert find_deepest_value(data, 'author') == 'Washie'
    assert find_deepest_value(data, 'secret_code') == 9999
    assert find_deepest_value(data, 'non_existent') is None

# --- Level 11 Test ---
def test_audit_user_permissions():
    users = {
        'admin': ['read', 'write', 'delete', 'sudo'],
        'dev_user': ['read', 'write'],
        'guest': []
    }
    required = ['read', 'write', 'delete']
    
    result = audit_user_permissions(users, required)
    
    # admin is compliant, shouldn't be in result
    assert 'admin' not in result
    # dev_user missing 'delete'
    assert result['dev_user'] == ['delete']
    # guest missing all three, sorted
    assert result['guest'] == ['delete', 'read', 'write']
