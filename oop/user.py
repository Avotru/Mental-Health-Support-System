"""
User Class - Object-Oriented Programming Paradigm

This module implements the User class for the Mental Health Support System.
"""

class User:
    """User class - Object-Oriented Programming example"""
    
    def __init__(self, user_id, username, email):
        """Initialize a new User object"""
        self.user_id = user_id
        self.username = username
        self.email = email
        self.preferences = {
            "theme": "light",
            "notifications_enabled": True,
            "check_in_time": "18:00"
        }
        self.mood_history = []
        self.assessment_history = []
    
    def update_preferences(self, new_preferences):
        """Update user preferences"""
        self.preferences.update(new_preferences)
        return self.preferences
    
    def get_user_info(self):
        """Get user information"""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "preferences": self.preferences
        }
    
    def add_mood_entry(self, mood_entry):
        """Add a mood entry to user's history"""
        self.mood_history.append(mood_entry)
    
    def add_assessment_result(self, assessment_result):
        """Add an assessment result to user's history"""
        self.assessment_history.append(assessment_result)
    
    def get_recent_mood_entries(self, count=7):
        """Get the most recent mood entries"""
        sorted_entries = sorted(
            self.mood_history,
            key=lambda entry: entry["timestamp"],
            reverse=True
        )
        return sorted_entries[:count]
    
    def get_average_mood(self, days=7):
        """Calculate average mood over specified number of days"""
        recent_entries = self.get_recent_mood_entries(days)
        if not recent_entries:
            return 0
        
        total = sum(entry["mood_rating"] for entry in recent_entries)
        return total / len(recent_entries)
