import fresh_tomatoes
import media

"""File contains movie proflies for fresh_tomatoes site"""

# Section 1.0:

# Create movie profiles by assigning the titles to instances of the
# class "Movie", located in the "media" file.

# Movie instances should be added below, using the following format:

# <movie_name> = media.Movie(<movie_title_string>,
#                            <description_string>,
#                            <movie_poster_image_url>,
#                            <youtube_trailer_url>)

# DON'T FORGET TO ADD <movie_name> TO THE "movies" LIST,
# LOCATED IN "Section 2.0"


fort_tilden = media.Movie("Fort Tilden",
                          "A brutal Clueless for millenials",
                          "http://dl9fvu4r30qs1.cloudfront.net/30/81/"
                          "c0a3ac82472a800cd354d53f22f4/"
                          "fort-tilden-poster.jpg",
                          "https://www.youtube.com/watch?v=B5SL2-AZ2aU")
royal_tenenbaums = media.Movie("The Royal Tenenbaums",
                               "Absentee father tries to make ammends"
                               "with quirky family",
                               "https://upload.wikimedia.org/wikipedia/"
                               "en/thumb/3/3b/The_Tenenbaums.jpg/"
                               "220px-The_Tenenbaums.jpg",
                               "https://www.youtube.com/embed/8Eg6yIwP2vs")
dogville = media.Movie("Dogville",
                       "Woman flees mob and attemptes to take refuge"
                       "in small town America, but finds that town may"
                       "not be the refuge she thought it was",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/"
                       "1/10/Dogville_poster.jpg/215px-Dogville_poster.jpg",
                       "https://www.youtube.com/watch?v=KXcS5qo-nKg")
clueless = media.Movie("Clueless",
                       "Satirical snippet of life for Beverly Hills youth",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/"
                       "2/21/Clueless.jpg/220px-Clueless.jpg",
                       "https://www.youtube.com/watch?v=yHDcD_xhwAo")
tammy = media.Movie("Tammy",
                    "Melissa McCarthy vehicle",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/4/40/"
                    "Tammy_poster.jpg/220px-Tammy_poster.jpg",
                    "https://www.youtube.com/watch?v=N8d6Bpl2eAo")
victoria = media.Movie("Victoria",
                       "Tense, one-shot crime thriller",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/"
                       "f/fe/Victoria_%282015_film%29_POSTER.jpg/"
                       "220px-Victoria_%282015_film%29_POSTER.jpg",
                       "https://www.youtube.com/watch?v=Kp8wcV3GjW0")
kedi = media.Movie("Kedi",
                   "Portriates of Turkish trash-cats",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/4/"
                   "45/Kedi-film-poster.jpg/220px-Kedi-film-poster.jpg",
                   "https://www.youtube.com/watch?v=lKq7UqplcL8")
anomolisa = media.Movie("Anomolisa",
                        "3D-printed drama: Man meets the woman of"
                        "his dreams one night, but maybe for only that"
                        "one night...",
                        "https://upload.wikimedia.org/wikipedia/en/thumb"
                        "/0/0f/Anomalisa_poster.jpg/"
                        "220px-Anomalisa_poster.jpg",
                        "https://www.youtube.com/watch?v=WQkHA3fHk_0")
entrapment = media.Movie("Entrapment",
                         "Classic heist film",
                         "https://upload.wikimedia.org/wikipedia/en/"
                         "thumb/8/89/Entrapment_film.jpg/"
                         "215px-Entrapment_film.jpg",
                         "https://www.youtube.com/watch?v=71qhx1LlHAY")

# Section 2.0

# Create a list of the "Movie" instances, to be used in the
# "open_movies_page" function of the "fresh_tomatoes.py" site file

movies = [fort_tilden, royal_tenenbaums, dogville, clueless, tammy,
          victoria, kedi, anomolisa, entrapment]

# Section 3.0
# Open movie profiles in browser by calling "open_movies_page"
# function on "movies" list
fresh_tomatoes.open_movies_page(movies)
