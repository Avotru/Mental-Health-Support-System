"""
Mental Health Support System - Main Application

This is the main application file that integrates all components of the
Mental Health Support System, demonstrating multiple programming paradigms.
"""

import streamlit as st
import datetime
import sys
import os

# Add the project root to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import modules from different paradigms
from procedural.data_handling import initialize_data, generate_sample_data, add_mood_entry
from oop.user import User
from oop.assessment import StressAssessment, AnxietyAssessment
from functional.analysis import calculate_average_mood, identify_mood_patterns, generate_insights
from logical.prolog_interface import PrologInterface
from ai.gemini_integration import GeminiAIClient

# Initialize session state
def init_session_state():
    """Initialize the session state with default values"""
    if 'initialized' not in st.session_state:
        # Initialize data
        data = initialize_data()
        
        # Generate sample data
        data["mood_entries"] = generate_sample_data()
        
        # Create user instance (OOP)
        user = User(
            data["user_info"]["user_id"],
            data["user_info"]["username"],
            data["user_info"]["email"]
        )
        
        # Add mood entries to user
        for entry in data["mood_entries"]:
            user.add_mood_entry(entry)
        
        # Create assessments (OOP)
        stress_assessment = StressAssessment()
        anxiety_assessment = AnxietyAssessment()
        
        # Initialize Prolog interface (Logical)
        prolog = PrologInterface()
        
        # Initialize Gemini AI client
        gemini = GeminiAIClient()
        
        # Store everything in session state
        st.session_state.data = data
        st.session_state.user = user
        st.session_state.stress_assessment = stress_assessment
        st.session_state.anxiety_assessment = anxiety_assessment
        st.session_state.prolog = prolog
        st.session_state.gemini = gemini
        st.session_state.page = "Dashboard"
        st.session_state.initialized = True

# Dashboard page
def show_dashboard():
    """Show the dashboard page"""
    st.title("Mental Health Dashboard")
    
    # Get recent mood entries
    mood_entries = st.session_state.user.get_recent_mood_entries()
    
    # Use functional programming to analyze mood data
    avg_mood = calculate_average_mood(mood_entries)
    mood_patterns = identify_mood_patterns(mood_entries)
    insights = generate_insights(mood_entries)
    
    # Display mood statistics
    st.subheader("Mood Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Mood", f"{avg_mood:.1f}/10")
    with col2:
        if mood_patterns:
            trend = "Improving" if any(p["type"] == "improving_mood" for p in mood_patterns) else \
                   "Declining" if any(p["type"] == "declining_mood" for p in mood_patterns) else \
                   "Stable"
            st.metric("Trend", trend)
        else:
            st.metric("Trend", "Stable")
    
    # Display mood chart
    st.subheader("Mood Tracking")
    
    # Extract dates and ratings for chart
    dates = [entry["timestamp"].split("T")[0] for entry in reversed(mood_entries)]
    ratings = [entry["mood_rating"] for entry in reversed(mood_entries)]
    
    # Create a simple chart using Streamlit
    st.line_chart({
        "Mood Rating": ratings
    })
    
    # Display insights
    st.subheader("Insights")
    if insights:
        for insight in insights[:3]:  # Show top 3 insights
            st.info(insight["description"])
    else:
        st.info("No insights available yet. Continue tracking your mood to generate insights.")
    
    # Get coping strategies using logical programming
    st.subheader("Recommended Coping Strategies")
    
    # Get the most recent mood entry
    if mood_entries:
        recent_entry = mood_entries[0]
        mood_rating = recent_entry["mood_rating"]
        concerns = recent_entry.get("concerns", [])
        
        # Use logical programming to get strategies
        strategies = st.session_state.prolog.get_coping_strategies(mood_rating, concerns)
        
        for strategy in strategies:
            st.success(strategy["description"])
    else:
        st.success("Complete a daily check-in to get personalized coping strategies.")

# Daily Check-in page
def show_daily_checkin():
    """Show the daily check-in page"""
    st.title("Daily Check-in")
    
    with st.form("checkin_form"):
        st.subheader("How are you feeling today?")
        mood_rating = st.slider("Rate your mood (1-10)", 1, 10, 5)
        
        st.subheader("Journal Entry")
        journal_entry = st.text_area("What's on your mind today?", height=150)
        
        st.subheader("Health Metrics")
        col1, col2 = st.columns(2)
        with col1:
            sleep_hours = st.number_input("Hours of sleep last night", 0, 12, 7)
        with col2:
            exercised = st.checkbox("Did you exercise today?")
        
        st.subheader("Concerns (if any)")
        concerns = []
        col1, col2 = st.columns(2)
        with col1:
            if st.checkbox("Stress"):
                concerns.append("stress")
            if st.checkbox("Anxiety"):
                concerns.append("anxiety")
            if st.checkbox("Depression"):
                concerns.append("depression")
        with col2:
            if st.checkbox("Sleep issues"):
                concerns.append("sleep")
            if st.checkbox("Concentration problems"):
                concerns.append("concentration")
            if st.checkbox("Motivation"):
                concerns.append("motivation")
        
        submitted = st.form_submit_button("Submit Check-in")
        
        if submitted:
            # Use procedural programming to add mood entry
            new_entry = add_mood_entry(
                st.session_state.data,
                mood_rating,
                journal_entry,
                concerns,
                sleep_hours,
                exercised
            )
            
            # Use OOP to add entry to user
            st.session_state.user.add_mood_entry(new_entry)
            
            # Use AI to analyze journal entry
            if journal_entry:
                analysis = st.session_state.gemini.analyze_journal_entry(journal_entry)
                
                st.subheader("AI Analysis")
                st.write(analysis["summary"])
            
            # Use logical programming to get coping strategies
            strategies = st.session_state.prolog.get_coping_strategies(mood_rating, concerns)
            
            if strategies:
                st.subheader("Recommended Coping Strategy")
                st.success(strategies[0]["description"])
            
            # Use AI to generate personalized response
            response = st.session_state.gemini.generate_coping_response(
                mood_rating, concerns, journal_entry
            )
            
            st.subheader("Personalized Response")
            st.info(response)
            
            st.success("Check-in recorded successfully!")

# Assessments page
def show_assessments():
    """Show the assessments page"""
    st.title("Mental Health Assessments")
    
    assessment_type = st.selectbox(
        "Select an assessment",
        ["Stress Assessment", "Anxiety Assessment"]
    )
    
    if assessment_type == "Stress Assessment":
        assessment = st.session_state.stress_assessment
    else:  # Anxiety Assessment
        assessment = st.session_state.anxiety_assessment
    
    st.write(assessment.description)
    
    with st.form("assessment_form"):
        responses = []
        
        for i, question in enumerate(assessment.questions):
            st.subheader(f"Question {i+1}")
            st.write(question["text"])
            response = st.radio(
                "Select your answer",
                options=question["options"],
                key=f"q{i}"
            )
            # Extract the numeric value from the option (e.g., "Never (0)" -> 0)
            value = int(response.split("(")[1].split(")")[0])
            responses.append(value)
        
        submitted = st.form_submit_button("Submit Assessment")
        
        if submitted:
            # Use OOP to calculate score
            result = assessment.calculate_score(responses)
            
            st.subheader("Assessment Results")
            st.write(f"Score: {result['score']}")
            st.write(f"Level: {result['level']}")
            st.write(result['description'])
            
            # Use OOP method for specific interpretation
            if hasattr(assessment, 'interpret_results'):
                interpretation = assessment.interpret_results(result['score'])
                st.write(interpretation)
            
            # Use AI to provide recommendations
            recommendations = st.session_state.gemini.analyze_assessment_results(
                assessment_type.split()[0].lower(),
                result['score'],
                result['level']
            )
            
            st.subheader("AI Recommendations")
            st.info(recommendations)
            
            # Use logical programming to analyze symptoms
            symptoms = []
            if assessment_type == "Stress Assessment":
                if result['score'] > 8:
                    symptoms.extend(["sleep_issues", "fatigue", "concentration_problems", "irritability"])
                elif result['score'] > 4:
                    symptoms.extend(["sleep_issues", "irritability"])
            else:  # Anxiety Assessment
                if result['score'] > 8:
                    symptoms.extend(["worry", "physical_tension", "racing_thoughts", "sleep_issues"])
                elif result['score'] > 4:
                    symptoms.extend(["worry", "physical_tension"])
            
            if symptoms:
                analysis = st.session_state.prolog.analyze_symptoms(symptoms)
                
                st.subheader("Additional Insights")
                st.write(f"Primary concern: {analysis['primary_concern'].capitalize()}")
                st.write(f"Severity: {analysis['severity'].capitalize()}")
                
                recommendations = st.session_state.prolog.get_recommendations(analysis)
                
                st.subheader("Recommended Strategies")
                for rec in recommendations:
                    if rec["type"] == "coping_strategy":
                        st.success(rec["description"])
                    else:
                        st.info(rec["description"])

# Resources page
def show_resources():
    """Show the resources page"""
    st.title("Mental Health Resources")
    
    resource_type = st.selectbox(
        "Select resource type",
        ["Coping Strategies", "Crisis Support", "Educational Resources"]
    )
    
    if resource_type == "Coping Strategies":
        st.subheader("Coping Strategies by Concern")
        
        concern = st.selectbox(
            "Select a concern",
            ["Stress", "Anxiety", "Depression", "Sleep", "Concentration", "Motivation"]
        )
        
        # Use logical programming to get strategies for the concern
        strategies = st.session_state.prolog.concern_strategy_map.get(concern.lower(), [])
        
        if strategies:
            for strategy in strategies:
                description = st.session_state.prolog.coping_strategies.get(strategy, "")
                st.success(f"**{strategy.replace('_', ' ').title()}**: {description}")
        else:
            st.info("No specific strategies found for this concern.")
    
    elif resource_type == "Crisis Support":
        st.subheader("Crisis Support Information")
        
        st.write("If you're experiencing a mental health crisis, please reach out for help:")
        
        st.info("""
        - **National Suicide Prevention Lifeline**: 988 or 1-800-273-8255
        - **Crisis Text Line**: Text HOME to 741741
        - **Emergency Services**: 911
        
        Remember, it's okay to ask for help. You don't have to face difficult times alone.
        """)
    
    else:  # Educational Resources
        st.subheader("Educational Resources")
        
        st.write("Learn more about mental health with these resources:")
        
        st.info("""
        - **National Institute of Mental Health**: [nimh.nih.gov](https://www.nimh.nih.gov)
        - **Mental Health America**: [mhanational.org](https://www.mhanational.org)
        - **American Psychological Association**: [apa.org](https://www.apa.org)
        
        Understanding mental health is an important step in taking care of yourself.
        """)

# Settings page
def show_settings():
    """Show the settings page"""
    st.title("Settings")
    
    # Get current user preferences
    preferences = st.session_state.user.preferences
    
    with st.form("settings_form"):
        st.subheader("Notification Settings")
        notifications_enabled = st.checkbox(
            "Enable check-in reminders",
            value=preferences.get("notifications_enabled", True)
        )
        
        check_in_time = st.time_input(
            "Daily check-in reminder time",
            datetime.time(
                hour=int(preferences.get("check_in_time", "18:00").split(":")[0]),
                minute=int(preferences.get("check_in_time", "18:00").split(":")[1])
            )
        )
        
        st.subheader("Appearance")
        theme = st.selectbox(
            "Theme",
            ["Light", "Dark"],
            index=0 if preferences.get("theme", "light") == "light" else 1
        )
        
        submitted = st.form_submit_button("Save Settings")
        
        if submitted:
            # Update preferences using OOP
            new_preferences = {
                "notifications_enabled": notifications_enabled,
                "check_in_time": f"{check_in_time.hour:02d}:{check_in_time.minute:02d}",
                "theme": theme.lower()
            }
            
            st.session_state.user.update_preferences(new_preferences)
            st.success("Settings updated successfully!")

# Main application
def main():
    """Main application function"""
    st.set_page_config(
        page_title="Mental Health Support System",
        page_icon="❤️",
        layout="wide"
    )
    
    # Initialize session state
    init_session_state()
    
    # Sidebar navigation
    st.sidebar.title("Mental Health Support System")
    
    # Navigation
    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Daily Check-in", "Assessments", "Resources", "Settings"]
    )
    
    # Display the selected page
    if page == "Dashboard":
        show_dashboard()
    elif page == "Daily Check-in":
        show_daily_checkin()
    elif page == "Assessments":
        show_assessments()
    elif page == "Resources":
        show_resources()
    elif page == "Settings":
        show_settings()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info(
        "This application demonstrates multiple programming paradigms: "
        "procedural, object-oriented, functional, and logical programming."
    )

if __name__ == "__main__":
    main()
