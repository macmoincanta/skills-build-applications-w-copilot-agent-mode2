# Test data for populating the octofit_db database

test_users = [
    {"email": "thundergod@mhigh.edu", "name": "Thor", "age": 30},
    {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "age": 35},
    {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "age": 32},
    {"email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff", "age": 28},
    {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "age": 40},
]

test_teams = [
    {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu"]},
    {"name": "Gold Team", "members": ["zerocool@mhigh.edu", "crashoverride@mhigh.edu", "sleeptoken@mhigh.edu"]},
]

test_activities = [
    {"user_email": "thundergod@mhigh.edu", "activity_type": "Cycling", "duration": 60, "date": "2025-04-08"},
    {"user_email": "metalgeek@mhigh.edu", "activity_type": "Crossfit", "duration": 120, "date": "2025-04-07"},
    {"user_email": "zerocool@mhigh.edu", "activity_type": "Running", "duration": 90, "date": "2025-04-06"},
    {"user_email": "crashoverride@mhigh.edu", "activity_type": "Strength", "duration": 30, "date": "2025-04-05"},
    {"user_email": "sleeptoken@mhigh.edu", "activity_type": "Swimming", "duration": 75, "date": "2025-04-04"},
]

test_leaderboard = [
    {"team_name": "Blue Team", "points": 200},
    {"team_name": "Gold Team", "points": 300},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
