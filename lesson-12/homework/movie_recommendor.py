import requests, json

# important details
api_key = "cd716ece17c93fce3a8a04587092c2f5"
account_id = 21781267
url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
movie_url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers_g = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDcxNmVjZTE3YzkzZmNlM2E4YTA0NTg3MDkyYzJmNSIsIm5iZiI6MTczODA4MTkyNi45ODQsInN1YiI6IjY3OTkwNjg2YTZlNDEyODNmMTJiNzA2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aJmGf1WoSW4i1xAHYHiqTR4KrBFj-eT0bsFbZZQPr_w"
}

headers_m = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDcxNmVjZTE3YzkzZmNlM2E4YTA0NTg3MDkyYzJmNSIsIm5iZiI6MTczODA4MTkyNi45ODQsInN1YiI6IjY3OTkwNjg2YTZlNDEyODNmMTJiNzA2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aJmGf1WoSW4i1xAHYHiqTR4KrBFj-eT0bsFbZZQPr_w"
}

response = requests.get(url, headers=headers_g)
movie_res = requests.get(movie_url, headers=headers_m)

with open("genres.json", "w") as file:
    json.dump(response.json(), file, indent=4)
print(response)

with open("movies.json", "w") as file:
    json.dump(movie_res.json(), file, indent=4)
print(movie_res)


# initial prompt to know about user's preferences
user_choice = set({})
while len(user_choice) <= 6:
    print("\nHey!\nChoose your top 3 picks:\n\t1. Lucy\n\t2. Inside Job\n\t3. All Quiet in the Western Front\n\t4. Insode Out 2\n\t5. Pixels\n\t6. Avengers: Endgame")
    inp = int(input("Choose please: "))
    if inp in [1,2,3,4,5,6]:
        if inp == 1: user_choice.update([28, 878, 53])
        elif inp == 2: user_choice.update([99, 80, 28])
        elif inp == 3: user_choice.update([10752, 37, 36])
        elif inp == 4: user_choice.update([16, 10751, 12])
        elif inp == 5: user_choice.update([16, 35, 28])
        elif inp == 6: user_choice.update([18, 28, 14, 12])
    else: print("PLease input your top picks")
    
print("Thank you. Our recommendations:")
with open("movies.json", "r") as file:
    movies = json.load(file)

# gives recs
def give_recommendation():
    recommendations = []

    for movie in movies['results']:

        movie_genres = set(movie['genre_ids'])
        
        # merges the similar numbers in one set, from user_choice and movie_genres
        matching_genres = movie_genres.intersection(user_choice)

        if matching_genres:
            recommendations.append(
                {
                'title': movie['original_title'],
                'matching_genres': matching_genres,
                'overview': movie['overview'],
                'popularity': movie['popularity'],
                'release_date': movie['release_date']
                }
            )

    for rec in recommendations:
        print(f"\n{rec['title']}\n\t{rec['overview']}\n\tPopularity: {rec['popularity']}\n\tRelease date: {rec['release_date']}")

    print(len(recommendations))

give_recommendation()
print(len(movies['results']))


