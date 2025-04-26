"""
Prolog Interface - Python interface to Prolog rules

This module provides an interface between Python and Prolog rules
for the Mental Health Support System.
"""

# In a real implementation, we would use PySwip or a similar library
# to interface with actual Prolog. For simplicity and to avoid
# dependencies, we'll simulate the Prolog behavior in Python.

class PrologInterface:
    """Interface to Prolog rules - Logical Programming example"""
    
    def __init__(self):
        """Initialize the Prolog interface"""
        # Define mood categories
        self.mood_categories = {
            1: "negative", 2: "negative", 3: "negative",
            4: "low", 5: "low",
            6: "neutral",
            7: "positive", 8: "positive", 9: "positive", 10: "positive"
        }
        
        # Define coping strategies
        self.coping_strategies = {
            "deep_breathing": "Try this deep breathing exercise: Breathe in for 4 counts, hold for 4, and exhale for 6. Repeat 5 times.",
            "mindfulness": "Practice mindfulness: Focus on your surroundings and identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "physical_activity": "Take a 10-minute walk or do some light stretching to release tension and improve your mood.",
            "journaling": "Write down your thoughts and feelings in a journal. This can help process emotions and gain perspective.",
            "social_connection": "Reach out to a friend or family member for support. Social connection can improve mood and reduce stress.",
            "gratitude": "Write down three things you're grateful for today, no matter how small.",
            "music": "Listen to music that matches the mood you want to achieve, not necessarily your current mood.",
            "nature": "Spend 15 minutes outside in nature, which has been shown to reduce stress and improve mood.",
            "progressive_relaxation": "Try progressive muscle relaxation: Tense and then release each muscle group in your body, starting from your toes and working up to your head.",
            "distraction": "Engage in a pleasant activity that will distract you from negative thoughts, such as reading, watching a show, or playing a game."
        }
        
        # Define which strategies are suitable for which mood categories
        self.mood_strategy_map = {
            "deep_breathing": ["negative", "low", "neutral"],
            "mindfulness": ["negative", "low", "neutral", "positive"],
            "physical_activity": ["negative", "low", "neutral", "positive"],
            "journaling": ["negative", "low", "neutral", "positive"],
            "social_connection": ["low", "neutral", "positive"],
            "gratitude": ["low", "neutral", "positive"],
            "music": ["negative", "low", "neutral", "positive"],
            "nature": ["negative", "low", "neutral", "positive"],
            "progressive_relaxation": ["negative", "low"],
            "distraction": ["negative", "low"]
        }
        
        # Define which strategies are suitable for which concerns
        self.concern_strategy_map = {
            "stress": ["deep_breathing", "mindfulness", "physical_activity", "journaling", "music", "nature", "progressive_relaxation"],
            "anxiety": ["deep_breathing", "mindfulness", "physical_activity", "journaling", "music", "nature", "progressive_relaxation", "distraction"],
            "depression": ["physical_activity", "journaling", "social_connection", "gratitude", "music", "nature", "distraction"],
            "sleep": ["physical_activity", "progressive_relaxation"],
            "concentration": ["mindfulness"],
            "motivation": ["gratitude", "music"],
            "social": ["social_connection"]
        }
        
        # Define symptom to condition mapping
        self.symptom_condition_map = {
            "sleep_issues": ["stress", "anxiety", "depression"],
            "fatigue": ["stress", "depression"],
            "concentration_problems": ["stress", "anxiety", "depression"],
            "irritability": ["stress", "anxiety"],
            "worry": ["anxiety", "stress"],
            "sadness": ["depression"],
            "loss_of_interest": ["depression"],
            "physical_tension": ["anxiety", "stress"],
            "racing_thoughts": ["anxiety"],
            "appetite_changes": ["depression", "stress"]
        }
    
    def get_mood_category(self, mood_rating):
        """Get the mood category for a given mood rating"""
        return self.mood_categories.get(mood_rating, "neutral")
    
    def get_coping_strategies(self, mood_rating, concerns=None):
        """
        Get coping strategies based on mood and concerns
        This simulates the Prolog rule: suitable_strategy(Strategy, MoodCategory, Concern)
        """
        if concerns is None:
            concerns = []
        
        mood_category = self.get_mood_category(mood_rating)
        
        # Find strategies suitable for the mood
        suitable_strategies = []
        for strategy, suitable_moods in self.mood_strategy_map.items():
            if mood_category in suitable_moods:
                # If no concerns, add all strategies suitable for the mood
                if not concerns:
                    suitable_strategies.append({
                        "name": strategy,
                        "description": self.coping_strategies[strategy]
                    })
                else:
                    # Check if strategy is suitable for any of the concerns
                    for concern in concerns:
                        if concern in self.concern_strategy_map and strategy in self.concern_strategy_map[concern]:
                            suitable_strategies.append({
                                "name": strategy,
                                "description": self.coping_strategies[strategy]
                            })
                            break
        
        # Return top 3 strategies
        return suitable_strategies[:3]
    
    def analyze_symptoms(self, symptoms):
        """
        Analyze symptoms and suggest possible conditions
        This simulates the Prolog rules for symptom analysis
        """
        # Count symptoms for each condition
        condition_counts = {"stress": 0, "anxiety": 0, "depression": 0}
        
        for symptom in symptoms:
            if symptom in self.symptom_condition_map:
                for condition in self.symptom_condition_map[symptom]:
                    condition_counts[condition] += 1
        
        # Determine primary concern
        primary_concern = max(condition_counts, key=condition_counts.get)
        
        # Determine severity
        count = condition_counts[primary_concern]
        if count <= 2:
            severity = "low"
        elif count <= 4:
            severity = "moderate"
        else:
            severity = "high"
        
        return {
            "primary_concern": primary_concern,
            "severity": severity,
            "condition_counts": condition_counts
        }
    
    def get_recommendations(self, analysis_result):
        """Get recommendations based on symptom analysis"""
        primary_concern = analysis_result["primary_concern"]
        severity = analysis_result["severity"]
        
        recommendations = []
        
        # Add coping strategies based on primary concern
        if primary_concern in self.concern_strategy_map:
            strategies = self.concern_strategy_map[primary_concern]
            for strategy in strategies[:2]:  # Top 2 strategies
                recommendations.append({
                    "type": "coping_strategy",
                    "name": strategy,
                    "description": self.coping_strategies[strategy]
                })
        
        # Add general recommendation based on severity
        if severity == "low":
            recommendations.append({
                "type": "general",
                "description": "Your symptoms are mild. Continue monitoring and practice self-care."
            })
        elif severity == "moderate":
            recommendations.append({
                "type": "general",
                "description": "Consider speaking with a counselor or mental health professional if symptoms persist."
            })
        else:  # high
            recommendations.append({
                "type": "general",
                "description": "We recommend consulting with a mental health professional to discuss your symptoms."
            })
        
        return recommendations
