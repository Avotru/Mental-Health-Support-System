# Mental Health Support System

This project demonstrates the integration of multiple programming paradigms (procedural, object-oriented, functional, and logical) to create an AI-driven healthcare solution focused on student mental health.

## Project Structure

```
mental_health_system/
├── app.py                      # Main application file that integrates all components
├── procedural/
│   └── data_handling.py        # Procedural functions for data collection and processing
├── oop/
│   ├── user.py                 # User class implementation
│   └── assessment.py           # Assessment class implementation
├── functional/
│   └── analysis.py             # Functional programming for pattern analysis
├── logical/
│   ├── prolog_rules.pl         # Actual Prolog rules for logical reasoning
│   └── prolog_interface.py     # Python interface to the Prolog rules
└── ai/
    └── gemini_integration.py   # Integration with Gemini AI for analysis
```

## Programming Paradigms

This project demonstrates four programming paradigms:

1. **Procedural Programming**: Used for data handling and basic operations in `procedural/data_handling.py`
2. **Object-Oriented Programming**: Used for modeling entities with state and behavior in `oop/user.py` and `oop/assessment.py`
3. **Functional Programming**: Used for data analysis and pattern recognition in `functional/analysis.py`
4. **Logical Programming**: Used for rule-based reasoning with Prolog in `logical/prolog_rules.pl` and `logical/prolog_interface.py`

## AI Integration

The system integrates with Google's Gemini AI (simulated) to provide:
- Journal entry analysis
- Personalized coping responses
- Assessment result interpretation

## Features

- **Dashboard**: View mood trends, insights, and recommended coping strategies
- **Daily Check-in**: Record mood, journal entries, and health metrics
- **Assessments**: Take mental health assessments with AI-powered recommendations
- **Resources**: Access coping strategies and mental health resources
- **Settings**: Customize application preferences

## Requirements

- Python 3.7 or higher
- Streamlit
- Other dependencies listed in requirements.txt

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run app.py
   ```

## Project Background

This project was developed for the BCS222 Programming Paradigms course to demonstrate how different programming paradigms can be integrated to solve complex problems in healthcare.
