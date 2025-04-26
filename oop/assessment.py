"""
Assessment Class - Object-Oriented Programming Paradigm

This module implements the Assessment class for the Mental Health Support System.
"""

class Assessment:
    """Assessment class - Object-Oriented Programming example"""
    
    def __init__(self, assessment_id, title, description):
        """Initialize a new Assessment object"""
        self.assessment_id = assessment_id
        self.title = title
        self.description = description
        self.questions = []
    
    def add_question(self, question_text, options):
        """Add a question to the assessment"""
        self.questions.append({
            "text": question_text,
            "options": options
        })
    
    def calculate_score(self, responses):
        """Calculate assessment score"""
        if len(responses) != len(self.questions):
            return {"error": "Number of responses doesn't match number of questions"}
        
        # Simple scoring: sum of response values
        score = sum(responses)
        
        # Determine result based on score
        if score <= len(responses) * 1:
            level = "Low"
            description = "Your symptoms are minimal."
        elif score <= len(responses) * 2:
            level = "Moderate"
            description = "You're experiencing some symptoms that may benefit from support."
        else:
            level = "High"
            description = "Your symptoms suggest you might benefit from professional support."
        
        return {
            "score": score,
            "level": level,
            "description": description
        }


class StressAssessment(Assessment):
    """Stress Assessment - Demonstrates inheritance in OOP"""
    
    def __init__(self):
        """Initialize a Stress Assessment with predefined questions"""
        super().__init__(
            "stress_assessment",
            "Stress Assessment",
            "This assessment helps identify your current stress levels."
        )
        
        # Add standard stress assessment questions
        self.add_question(
            "How often have you felt that you were unable to control the important things in your life?",
            ["Never (0)", "Almost Never (1)", "Sometimes (2)", "Fairly Often (3)", "Very Often (4)"]
        )
        self.add_question(
            "How often have you felt nervous and stressed?",
            ["Never (0)", "Almost Never (1)", "Sometimes (2)", "Fairly Often (3)", "Very Often (4)"]
        )
        self.add_question(
            "How often have you found that you could not cope with all the things that you had to do?",
            ["Never (0)", "Almost Never (1)", "Sometimes (2)", "Fairly Often (3)", "Very Often (4)"]
        )
        self.add_question(
            "How often have you felt difficulties were piling up so high that you could not overcome them?",
            ["Never (0)", "Almost Never (1)", "Sometimes (2)", "Fairly Often (3)", "Very Often (4)"]
        )
    
    def interpret_results(self, score):
        """Provide specific interpretation for stress assessment"""
        if score <= 4:
            return "Your stress levels appear to be manageable."
        elif score <= 8:
            return "You're experiencing moderate stress. Consider implementing stress management techniques."
        else:
            return "You're experiencing high levels of stress. Consider speaking with a mental health professional."


class AnxietyAssessment(Assessment):
    """Anxiety Assessment - Demonstrates inheritance in OOP"""
    
    def __init__(self):
        """Initialize an Anxiety Assessment with predefined questions"""
        super().__init__(
            "anxiety_assessment",
            "Anxiety Assessment",
            "This assessment helps identify symptoms of anxiety."
        )
        
        # Add standard anxiety assessment questions
        self.add_question(
            "How often have you been feeling nervous, anxious, or on edge?",
            ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]
        )
        self.add_question(
            "How often have you not been able to stop or control worrying?",
            ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]
        )
        self.add_question(
            "How often have you been worrying too much about different things?",
            ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]
        )
        self.add_question(
            "How often have you had trouble relaxing?",
            ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]
        )
    
    def interpret_results(self, score):
        """Provide specific interpretation for anxiety assessment"""
        if score <= 4:
            return "Your anxiety levels appear to be within a normal range."
        elif score <= 8:
            return "You're experiencing moderate anxiety. Consider learning anxiety management techniques."
        else:
            return "You're experiencing significant anxiety symptoms. Consider speaking with a mental health professional."
