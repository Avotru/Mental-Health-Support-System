"""
Analysis Module - Functional Programming Paradigm

This module implements functional programming approaches for data analysis
in the Mental Health Support System.
"""

from functools import reduce
import datetime

# Pure function to calculate average mood
def calculate_average_mood(entries):
    """Calculate average mood rating - Functional Programming example"""
    if not entries:
        return 0
    
    # Use functional programming approach with map and sum
    ratings = list(map(lambda entry: entry["mood_rating"], entries))
    return sum(ratings) / len(ratings)

# Pure function to identify mood patterns
def identify_mood_patterns(entries):
    """Identify patterns in mood data - Functional Programming example"""
    if not entries:
        return []
    
    # Sort entries by timestamp
    sorted_entries = sorted(
        entries,
        key=lambda entry: entry["timestamp"],
        reverse=True
    )
    
    # Extract mood ratings
    ratings = list(map(lambda entry: entry["mood_rating"], sorted_entries))
    
    # Identify patterns
    patterns = []
    
    # Pattern: Consistent low mood
    if len(ratings) >= 3 and all(rating <= 4 for rating in ratings[:3]):
        patterns.append({
            "type": "consistent_low_mood",
            "description": "Consistently low mood for 3+ days",
            "severity": "high"
        })
    
    # Pattern: Improving mood
    if len(ratings) >= 5:
        is_improving = all(ratings[i] >= ratings[i+1] for i in range(4))
        if is_improving:
            patterns.append({
                "type": "improving_mood",
                "description": "Your mood has been steadily improving",
                "severity": "low"
            })
    
    # Pattern: Declining mood
    if len(ratings) >= 5:
        is_declining = all(ratings[i] <= ratings[i+1] for i in range(4))
        if is_declining:
            patterns.append({
                "type": "declining_mood",
                "description": "Your mood has been declining recently",
                "severity": "medium"
            })
    
    # Pattern: Mood swings
    if len(ratings) >= 4:
        differences = [abs(ratings[i] - ratings[i+1]) for i in range(len(ratings)-1)]
        if any(diff >= 4 for diff in differences):
            patterns.append({
                "type": "mood_swings",
                "description": "You've experienced significant mood swings",
                "severity": "medium"
            })
    
    return patterns

# Pure function to analyze sleep patterns
def analyze_sleep_patterns(entries):
    """Analyze sleep patterns - Functional Programming example"""
    if not entries:
        return {"average": 0, "patterns": []}
    
    # Extract sleep hours
    sleep_hours = list(map(lambda entry: entry["sleep_hours"], entries))
    
    # Calculate average
    average_sleep = sum(sleep_hours) / len(sleep_hours)
    
    # Identify patterns
    patterns = []
    
    # Pattern: Insufficient sleep
    if average_sleep < 6:
        patterns.append({
            "type": "insufficient_sleep",
            "description": "You're averaging less than 6 hours of sleep",
            "severity": "high"
        })
    
    # Pattern: Inconsistent sleep
    if max(sleep_hours) - min(sleep_hours) >= 3:
        patterns.append({
            "type": "inconsistent_sleep",
            "description": "Your sleep schedule is inconsistent",
            "severity": "medium"
        })
    
    return {
        "average": average_sleep,
        "patterns": patterns
    }

# Pure function to generate insights
def generate_insights(mood_entries):
    """Generate insights from mood data - Functional Programming example"""
    if not mood_entries:
        return []
    
    # Use functional composition to generate insights
    mood_patterns = identify_mood_patterns(mood_entries)
    sleep_analysis = analyze_sleep_patterns(mood_entries)
    
    # Combine insights
    insights = []
    
    # Add mood pattern insights
    insights.extend(map(
        lambda pattern: {
            "type": "mood_pattern",
            "description": pattern["description"],
            "severity": pattern["severity"]
        },
        mood_patterns
    ))
    
    # Add sleep pattern insights
    insights.extend(map(
        lambda pattern: {
            "type": "sleep_pattern",
            "description": pattern["description"],
            "severity": pattern["severity"]
        },
        sleep_analysis["patterns"]
    ))
    
    # Add exercise insights
    exercise_days = list(filter(lambda entry: entry["exercised"], mood_entries))
    exercise_percentage = len(exercise_days) / len(mood_entries) * 100
    
    if exercise_percentage < 30:
        insights.append({
            "type": "exercise",
            "description": "You've exercised on less than 30% of days",
            "severity": "medium"
        })
    
    # Sort insights by severity
    severity_order = {"high": 0, "medium": 1, "low": 2}
    sorted_insights = sorted(
        insights,
        key=lambda insight: severity_order[insight["severity"]]
    )
    
    return sorted_insights
