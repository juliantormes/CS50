# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 100


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")
    else:
        namefile = sys.argv[1]

    # Read teams into memory from file
    teams = []
    try:
        with open(namefile, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                team_data = {"team": row["team"], "rating": int(row["rating"])}
                teams.append(team_data)

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except KeyError:
        print("Error: Missing expected 'team' or 'rating' column in CSV file.")
    except ValueError:
        print("Error: Cannot convert rating to integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    counts = {}
    # Simulate N tournaments and keep track of win counts
    for i in range(N):
        winner = simulate_tournament(teams)

        if winner not in counts:
            counts[winner] = 1
        else:
            counts[winner] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    # Play the first round
    winners = simulate_round(teams)

    # Play all other rounds until have only 1 winner
    while len(winners) != 1:
        winners = simulate_round(winners)

    # Return the name of the winner
    return winners[0]["team"]


if __name__ == "__main__":
    main()
