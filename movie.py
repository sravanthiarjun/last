import media
import fresh_tomatoes

ranga = media.Movie("rangastalam",
                    "it is a family entertainment story and emotional",
                    "https://bit.ly/2kcHbu1", "https://bit.ly/2KIrPsoE")
ok = media.Movie("ok bangaram", "pure love story", "https://bit.ly/2J0YHiT",
                 "https://bit.ly/2KJ4d6V")
love = media.Movie("lovers", "beautiful and amzing love story",
                   "https://bit.ly/2IXRO1K", "https://bit.ly/2x1LlOK")
nenu = media.Movie("nenulocal", "girl was afraid of her father",
                   "https://bit.ly/2s3B5Q2", "https://bit.ly/2LjF2ZK")
gol = media.Movie("golmol", "friendship and honest movie",
                  "https://bit.ly/2kcHbu1", "https://bit.ly/2GFfuTs")

movies = [ranga, ok, love, nenu, gol]
fresh_tomatoes.open_page(movies)
