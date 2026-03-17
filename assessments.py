"""
Python Mastery Assessments: Levels 9 - 11
Curated for Washie.
"""
# --- LEVEL 7: DATA MANIPULATION & STRING FORMATTING ---

def university_admission_check(applicant_list, min_score):
    """
    Question 7 - university_admission_check(applicant_list, min_score)
    The University of Johannesburg is processing late applications. 
    'applicant_list' contains dictionaries: {'name': str, 'score': int}
    
    Requirements:
    - Identify applicants whose 'score' is greater than or equal to 'min_score'.
    - Return a list of strings formatted as: "APPROVED: [NAME] ([SCORE])"
    - The name must be in UPPERCASE.
    
    Example Input: [{"name": "Washie", "score": 85}, {"name": "Joe", "score": 40}], 50
    Example Output: ["APPROVED: WASHIE (85)"]
    """
    pass


# --- LEVEL 8: DATA STRUCTURES & AGGREGATION ---

def calculate_fuel_expenses(trip_logs):
    """
    Question 8 - calculate_fuel_expenses(trip_logs)
    A logistics company in Elandsfontein tracks fuel usage for their fleet.
    'trip_logs' is a list of dictionaries: 
    {'truck_id': str, 'liters': float, 'price_per_liter': float, 'business_trip': bool}
    
    Requirements:
    - Calculate the total cost (liters * price_per_liter) for all trips.
    - However, only include trips where 'business_trip' is True.
    - Return the total cost rounded to 2 decimal places.
    
    Example Input: [
        {'truck_id': 'T01', 'liters': 50.0, 'price_per_liter': 22.50, 'business_trip': True},
        {'truck_id': 'T02', 'liters': 20.0, 'price_per_liter': 21.00, 'business_trip': False}
    ]
    Example Output: 1125.0 (50 * 22.50)
    """
    pass
# --- LEVEL 9: STRING FORMATTING & DATA STRUCTURES ---

def format_property_listings(suburb, listings):
    """
    Question 9 - format_property_listings(suburb, listings)
    A real estate agency in Sandton needs to generate formatted summaries.
    'listings' is a list of dictionaries: {'price': int, 'bedrooms': int, 'available': bool}
    
    Requirements:
    - Only include properties where 'available' is True.
    - Format price with a 'R' prefix and comma separators (e.g., R 1,200,000).
    - Suburb must be UPPERCASE.
    - Return a list of strings: "[SUBURB] | [Price] | [Bedrooms] BR"
    
    Example Input: "Sandton", [{'price': 1500000, 'bedrooms': 3, 'available': True}]
    Example Output: ["SANDTON | R 1,500,000 | 3 BR"]
    """
    pass


# --- LEVEL 10: RECURSION & DATA MANIPULATION ---

def find_deepest_value(nested_data, target_key):
    """
    Question 10 - find_deepest_value(nested_data, target_key)
    In complex JSON configs, values are often buried deep. 
    'nested_data' is a dictionary that can contain integers, strings, 
    or OTHER dictionaries.
    
    Task: Use RECURSION to search through the dictionary and its 
    nested children to find the value associated with 'target_key'.
    
    Logic:
    - If the key is found, return the value.
    - If not found in the current level, search the nested dictionaries.
    - Return None if the key does not exist anywhere.
    
    Example Input: {'a': 1, 'b': {'c': 5, 'target': 'Found Me'}}, 'target'
    Example Output: 'Found Me'
    """
    pass


# --- LEVEL 11: DATA STRUCTURES & MANIPULATION ---

def audit_user_permissions(current_users, required_perms):
    """
    Question 11 - audit_user_permissions(current_users, required_perms)
    You are auditing a system's security. 
    'current_users' is a dict: { 'username': ['list', 'of', 'perms'] }
    'required_perms' is a list of strings that EVERY user must have.
    
    Task:
    - Identify "Non-Compliant" users who are missing one or more required permissions.
    - Return a dictionary where:
        - Keys are the usernames of non-compliant users.
        - Values are a sorted list of the SPECIFIC permissions they are missing.
    
    Example Input: 
    users = {'washie': ['read', 'write'], 'intern': ['read']}
    required = ['read', 'write', 'delete']
    
    Example Output: 
    {'washie': ['delete'], 'intern': ['delete', 'write']}
    """
    pass
