import webbrowser

""" Create a class "Movie" to store the following information:
 1) Title
 2) Storyline
 3) Poster image
 4) Trailer
 For use with fresh_tomates site code"""

class Movie():

    def __init__(self, movie_title, movie_storyline, movie_poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = trailer_youtube
            
    def show_trailer(self):
        webbrowser.open(self.movie_trailer_url)
