# Simple Recommendation System
# Internship Task 4

def main():
    print("=== Simple Recommendation System ===\n")

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

    user_input = input("Enter your preferred genres (comma separated): ")
    user_preferences = [g.strip().title() for g in user_input.split(",")]

    recommendations = []

    for item, genres in items.items():
        for genre in genres:
            if genre in user_preferences:
                recommendations.append(item)
                break

    print("\nRecommended Items:")
    if recommendations:
        for rec in recommendations:
            print("-", rec)
    else:
        print("No recommendations found.")

    input("\nPress Enter to close...")

if __name__ == "__main__":
    main()
