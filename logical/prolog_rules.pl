/* 
Prolog Rules for Mental Health Support System - Logical Programming Paradigm

This file contains Prolog rules for coping strategies and symptom analysis.
*/

% Define mood categories
mood_category(1, negative).
mood_category(2, negative).
mood_category(3, negative).
mood_category(4, low).
mood_category(5, low).
mood_category(6, neutral).
mood_category(7, positive).
mood_category(8, positive).
mood_category(9, positive).
mood_category(10, positive).

% Define concerns
concern(stress).
concern(anxiety).
concern(depression).
concern(sleep).
concern(concentration).
concern(motivation).
concern(social).

% Define coping strategies
coping_strategy(deep_breathing, "Try this deep breathing exercise: Breathe in for 4 counts, hold for 4, and exhale for 6. Repeat 5 times.").
coping_strategy(mindfulness, "Practice mindfulness: Focus on your surroundings and identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.").
coping_strategy(physical_activity, "Take a 10-minute walk or do some light stretching to release tension and improve your mood.").
coping_strategy(journaling, "Write down your thoughts and feelings in a journal. This can help process emotions and gain perspective.").
coping_strategy(social_connection, "Reach out to a friend or family member for support. Social connection can improve mood and reduce stress.").
coping_strategy(gratitude, "Write down three things you're grateful for today, no matter how small.").
coping_strategy(music, "Listen to music that matches the mood you want to achieve, not necessarily your current mood.").
coping_strategy(nature, "Spend 15 minutes outside in nature, which has been shown to reduce stress and improve mood.").
coping_strategy(progressive_relaxation, "Try progressive muscle relaxation: Tense and then release each muscle group in your body, starting from your toes and working up to your head.").
coping_strategy(distraction, "Engage in a pleasant activity that will distract you from negative thoughts, such as reading, watching a show, or playing a game.").

% Define which strategies are suitable for which mood categories
suitable_for_mood(deep_breathing, negative).
suitable_for_mood(deep_breathing, low).
suitable_for_mood(deep_breathing, neutral).
suitable_for_mood(mindfulness, negative).
suitable_for_mood(mindfulness, low).
suitable_for_mood(mindfulness, neutral).
suitable_for_mood(mindfulness, positive).
suitable_for_mood(physical_activity, negative).
suitable_for_mood(physical_activity, low).
suitable_for_mood(physical_activity, neutral).
suitable_for_mood(physical_activity, positive).
suitable_for_mood(journaling, negative).
suitable_for_mood(journaling, low).
suitable_for_mood(journaling, neutral).
suitable_for_mood(journaling, positive).
suitable_for_mood(social_connection, low).
suitable_for_mood(social_connection, neutral).
suitable_for_mood(social_connection, positive).
suitable_for_mood(gratitude, low).
suitable_for_mood(gratitude, neutral).
suitable_for_mood(gratitude, positive).
suitable_for_mood(music, negative).
suitable_for_mood(music, low).
suitable_for_mood(music, neutral).
suitable_for_mood(music, positive).
suitable_for_mood(nature, negative).
suitable_for_mood(nature, low).
suitable_for_mood(nature, neutral).
suitable_for_mood(nature, positive).
suitable_for_mood(progressive_relaxation, negative).
suitable_for_mood(progressive_relaxation, low).
suitable_for_mood(distraction, negative).
suitable_for_mood(distraction, low).

% Define which strategies are suitable for which concerns
suitable_for_concern(deep_breathing, stress).
suitable_for_concern(deep_breathing, anxiety).
suitable_for_concern(mindfulness, stress).
suitable_for_concern(mindfulness, anxiety).
suitable_for_concern(mindfulness, concentration).
suitable_for_concern(physical_activity, stress).
suitable_for_concern(physical_activity, anxiety).
suitable_for_concern(physical_activity, depression).
suitable_for_concern(physical_activity, sleep).
suitable_for_concern(journaling, stress).
suitable_for_concern(journaling, anxiety).
suitable_for_concern(journaling, depression).
suitable_for_concern(social_connection, depression).
suitable_for_concern(social_connection, social).
suitable_for_concern(gratitude, depression).
suitable_for_concern(gratitude, motivation).
suitable_for_concern(music, stress).
suitable_for_concern(music, anxiety).
suitable_for_concern(music, depression).
suitable_for_concern(music, motivation).
suitable_for_concern(nature, stress).
suitable_for_concern(nature, anxiety).
suitable_for_concern(nature, depression).
suitable_for_concern(progressive_relaxation, stress).
suitable_for_concern(progressive_relaxation, anxiety).
suitable_for_concern(progressive_relaxation, sleep).
suitable_for_concern(distraction, anxiety).
suitable_for_concern(distraction, depression).

% Rule to find suitable coping strategies based on mood and concerns
suitable_strategy(Strategy, MoodCategory, Concern) :-
    suitable_for_mood(Strategy, MoodCategory),
    suitable_for_concern(Strategy, Concern).

% Rule to find suitable coping strategies based on mood only
suitable_strategy_mood_only(Strategy, MoodCategory) :-
    suitable_for_mood(Strategy, MoodCategory).

% Rule to find suitable coping strategies based on concern only
suitable_strategy_concern_only(Strategy, Concern) :-
    suitable_for_concern(Strategy, Concern).

% Define symptom categories
symptom(sleep_issues).
symptom(fatigue).
symptom(concentration_problems).
symptom(irritability).
symptom(worry).
symptom(sadness).
symptom(loss_of_interest).
symptom(physical_tension).
symptom(racing_thoughts).
symptom(appetite_changes).

% Define which symptoms suggest which conditions
suggests(sleep_issues, stress).
suggests(sleep_issues, anxiety).
suggests(sleep_issues, depression).
suggests(fatigue, stress).
suggests(fatigue, depression).
suggests(concentration_problems, stress).
suggests(concentration_problems, anxiety).
suggests(concentration_problems, depression).
suggests(irritability, stress).
suggests(irritability, anxiety).
suggests(worry, anxiety).
suggests(worry, stress).
suggests(sadness, depression).
suggests(loss_of_interest, depression).
suggests(physical_tension, anxiety).
suggests(physical_tension, stress).
suggests(racing_thoughts, anxiety).
suggests(appetite_changes, depression).
suggests(appetite_changes, stress).

% Rule to analyze symptoms and suggest possible conditions
analyze_symptoms(Symptoms, Condition) :-
    member(Symptom, Symptoms),
    suggests(Symptom, Condition).

% Rule to count how many symptoms suggest a condition
symptom_count(Symptoms, Condition, Count) :-
    findall(Symptom, (member(Symptom, Symptoms), suggests(Symptom, Condition)), MatchingSymptoms),
    length(MatchingSymptoms, Count).

% Rule to determine primary concern based on symptom count
primary_concern(Symptoms, Condition) :-
    symptom_count(Symptoms, stress, StressCount),
    symptom_count(Symptoms, anxiety, AnxietyCount),
    symptom_count(Symptoms, depression, DepressionCount),
    StressCount >= AnxietyCount,
    StressCount >= DepressionCount,
    Condition = stress.
primary_concern(Symptoms, Condition) :-
    symptom_count(Symptoms, anxiety, AnxietyCount),
    symptom_count(Symptoms, depression, DepressionCount),
    AnxietyCount >= DepressionCount,
    Condition = anxiety.
primary_concern(Symptoms, Condition) :-
    Condition = depression.

% Rule to determine severity based on symptom count
severity(Symptoms, Condition, low) :-
    symptom_count(Symptoms, Condition, Count),
    Count =< 2.
severity(Symptoms, Condition, moderate) :-
    symptom_count(Symptoms, Condition, Count),
    Count > 2,
    Count =< 4.
severity(Symptoms, Condition, high) :-
    symptom_count(Symptoms, Condition, Count),
    Count > 4.
