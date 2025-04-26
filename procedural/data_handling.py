"""
Data Handling Module - Procedural Programming Paradigm

This module contains procedural functions for data collection, processing,
and storage in the Mental Health Support System.
"""

import datetime
import json
import os

# Initialize data storage
def initialize_data():
    """Initialize empty data structures for the application"""
    data = {
        "mood_entries": [],
        "assessments_taken": [],
        "user_info": {
            "user_id": "user_1",
            "username": "student",
            "email": "student@example.com"
        }
    }
    return data

# Generate sample data for demonstration
def generate_sample_data():
    """Generate sample mood entries for demonstration purposes"""
    mood_entries = []
    
    # Generate sample data for the past week using procedural programming
    for i in range(7):
        entry_date = datetime.datetime.now() - datetime.timedelta(days=i)
        
        # Generate some realistic sample data
        if i == 0:  # Today
            mood_rating = 6
            journal_text = "Feeling okay today. A bit stressed about the upcoming project deadline."
            concerns = ["stress"]
            sleep_hours = 6
        elif i == 1:  # Yesterday
            mood_rating = 4
            journal_text = "Had a difficult day. Failed my quiz and feeling down. Didn't sleep well."
            concerns = ["stress", "depression"]
            sleep_hours = 5
        elif i == 2:  # 2 days ago
            mood_rating = 3
            journal_text = "Still feeling down. Having trouble concentrating on my work."
            concerns = ["depression", "concentration"]
            sleep_hours = 6
        elif i == 3:  # 3 days ago
            mood_rating = 3
            journal_text = "Another tough day. Feeling overwhelmed with coursework."
            concerns = ["stress", "anxiety"]
            sleep_hours = 5
        elif i == 4:  # 4 days ago
            mood_rating = 5
            journal_text = "Slightly better today. Had a good study session with friends."
            concerns = ["stress"]
            sleep_hours = 7
        elif i == 5:  # 5 days ago
            mood_rating = 7
            journal_text = "Good day! Finished an assignment and feeling accomplished."
            concerns = []
            sleep_hours = 8
        else:  # 6 days ago
            mood_rating = 6
            journal_text = "Normal day. Nothing special happened."
            concerns = []
            sleep_hours = 7
        
        # Create a mood entry dictionary
        mood_entry = {
            "entry_id": f"entry_{i}",
            "timestamp": entry_date.isoformat(),
            "mood_rating": mood_rating,
            "journal_entry": journal_text,
            "concerns": concerns,
            "sleep_hours": sleep_hours,
            "exercised": i % 3 == 0  # Exercise every 3 days in our sample
        }
        
        # Add to mood entries list
        mood_entries.append(mood_entry)
    
    return mood_entries

# Save data to file
def save_data(data, filename):
    """Save data to a JSON file"""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

# Load data from file
def load_data(filename):
    """Load data from a JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        else:
            return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Add a new mood entry
def add_mood_entry(data, mood_rating, journal_entry, concerns, sleep_hours, exercised):
    """Add a new mood entry to the data"""
    entry_id = f"entry_{len(data['mood_entries'])}"
    timestamp = datetime.datetime.now().isoformat()
    
    new_entry = {
        "entry_id": entry_id,
        "timestamp": timestamp,
        "mood_rating": mood_rating,
        "journal_entry": journal_entry,
        "concerns": concerns,
        "sleep_hours": sleep_hours,
        "exercised": exercised
    }
    
    data["mood_entries"].append(new_entry)
    return new_entry

# Get mood entries for a specific date range
def get_mood_entries_by_date_range(data, start_date, end_date):
    """Get mood entries within a specific date range"""
    start = datetime.datetime.fromisoformat(start_date)
    end = datetime.datetime.fromisoformat(end_date)
    
    filtered_entries = []
    for entry in data["mood_entries"]:
        entry_date = datetime.datetime.fromisoformat(entry["timestamp"])
        if start <= entry_date <= end:
            filtered_entries.append(entry)
    
    return filtered_entries

# Add assessment result
def add_assessment_result(data, assessment_type, score, level, description):
    """Add a new assessment result to the data"""
    assessment_id = f"assessment_{len(data['assessments_taken'])}"
    timestamp = datetime.datetime.now().isoformat()
    
    new_assessment = {
        "assessment_id": assessment_id,
        "timestamp": timestamp,
        "assessment_type": assessment_type,
        "score": score,
        "level": level,
        "description": description
    }
    
    data["assessments_taken"].append(new_assessment)
    return new_assessment
