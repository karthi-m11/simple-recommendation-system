# Simple Recommendation System
# Internship Task 4

# Sample items with categories
items = {
    "Inception": ["Sci-Fi", "Action"],
    "Titanic": ["Romance", "Drama"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "Avengers": ["Action", "Fantasy"],
    "The Notebook": ["Romance", "Drama"],
    "Matrix": ["Sci-Fi", "Action"],
    "Schindler's List (1993)": ["War", "History"],
    "The Lord of the Rings": ["Fantasy"]
}

# Get user preferences
user_input = input("Enter your preferred genres (comma separated): ")
user_preferences = user_input.split(",")

# Clean input
user_preferences = [genre.strip().title() for genre in user_preferences]

# Recommendation logic
recommendations = []

for item, genres in items.items():
    for genre in genres:
        if genre in user_preferences:
            recommendations.append(item)
            break

# Display results
print("\nRecommended Items:")

if recommendations:
    for rec in recommendations:
        print("-", rec)
else:
    print("No recommendations found based on your preferences.")

input("\nPress Enter to exit...")





