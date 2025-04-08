from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        # Debugging: Print user data before saving
        print("Creating users:", users)
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu']),
            Team(name='Gold Team', members=['zerocool@mhigh.edu', 'crashoverride@mhigh.edu', 'sleeptoken@mhigh.edu']),
        ]
        # Debugging: Print team data before saving
        print("Creating teams:", teams)
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user_email='thundergod@mhigh.edu', activity_type='Cycling', duration=60, date='2025-04-08'),
            Activity(user_email='metalgeek@mhigh.edu', activity_type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user_email='zerocool@mhigh.edu', activity_type='Running', duration=90, date='2025-04-06'),
            Activity(user_email='crashoverride@mhigh.edu', activity_type='Strength', duration=30, date='2025-04-05'),
            Activity(user_email='sleeptoken@mhigh.edu', activity_type='Swimming', duration=75, date='2025-04-04'),
        ]
        # Debugging: Print activity data before saving
        print("Creating activities:", activities)
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team_name='Blue Team', points=200),
            Leaderboard(team_name='Gold Team', points=300),
        ]
        # Debugging: Print leaderboard data before saving
        print("Creating leaderboard entries:", leaderboard_entries)
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        # Debugging: Print workout data before saving
        print("Creating workouts:", workouts)
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
