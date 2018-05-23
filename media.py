import webbrowser


class Movie():

    def __init__(
        i,
        movie_title,
        poster_image,
        trailer_youtube
            ):

            i.title = movie_title
            i.poster_image_url = poster_image
            i.trailer_youtube_url = trailer_youtube


def show_trailer(j):
    webbrowswer.open(j.trailer_youtube_url)
