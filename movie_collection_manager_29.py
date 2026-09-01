movies = []
maxsize = int(input("Enter maxsize: "))

while True:
    print("\n===== MOVIE COLLECTION MANAGER =====")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Remove Movie")
    print("5. Find Highest Rated Movie")
    print("6. Show Collection Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Add movie
    if choice == 1:
        if len(movies) >= maxsize:
            print("Movie collection is full!")
        else:
            name = input("Enter movie name: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating: "))

            movie = {
                "name": name,
                "genre": genre,
                "rating": rating
            }

            movies.append(movie)
            print("Movie added successfully!")

    # View movies
    elif choice == 2:
        if len(movies) == 0:
            print("No movies in the collection.")
        else:
            print("\nYour Movies:")
            for movie in movies:
                print("Movie:", movie["name"])
                print("Genre:", movie["genre"])
                print("Rating:", movie["rating"])
                print()

    # Search movie
    elif choice == 3:
        name = input("Enter movie name to search: ")
        found = False

        for movie in movies:
            if movie["name"].lower() == name.lower():
                print("Movie found!")
                print("Movie:", movie["name"])
                print("Genre:", movie["genre"])
                print("Rating:", movie["rating"])
                found = True
                break

        if found == False:
            print("Movie not found!")

    # Remove movie
    elif choice == 4:
        name = input("Enter movie name to remove: ")
        found = False

        for movie in movies:
            if movie["name"].lower() == name.lower():
                movies.remove(movie)
                print("Movie removed successfully!")
                found = True
                break

        if found == False:
            print("Movie not found!")

    # Find highest rated movie
    elif choice == 5:
        if len(movies) == 0:
            print("No movies in the collection.")
        else:
            highest = movies[0]

            for movie in movies:
                if movie["rating"] > highest["rating"]:
                    highest = movie

            print("Highest Rated Movie:", highest["name"])
            print("Rating:", highest["rating"])

    # Show collection statistics
    elif choice == 6:
        if len(movies) == 0:
            print("No movies in the collection.")
        else:
            total_movies = len(movies)
            total_rating = 0

            for movie in movies:
                total_rating = total_rating + movie["rating"]

            average_rating = total_rating / total_movies

            print("\nCOLLECTION STATISTICS")
            print("Total Movies:", total_movies)
            print("Maximum Capacity:", maxsize)
            print("Available Space:", maxsize - total_movies)
            print("Average Rating:", average_rating)

    # Exit
    elif choice == 7:
        print("Thank you for using Movie Collection Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
