movies = [ ("Inception", 8.8), ("Titanic", 7.8),
           ("Avengers", 8.0), ("The Room", 3.7),
           ("Interstellar", 8.6), ("Parasite", 8.6),
           ("The Dark Knight", 9.0) ]


def movie_filtering(score):
    result = []

    for movie in movies:
        if movie[1] >= score:
            result.append(movie)

    return result


min_score = float(input("최소 평점을 입력하세요: "))

filtered_movies = movie_filtering(min_score)

if len(filtered_movies) == 0:
    print("조건에 맞는 영화가 없습니다.")
else:
    print(f"{min_score} 이상 영화 목록:")
    for title, rating in filtered_movies:
        print(f"- {title}({rating})")