import fresh_tomatoes
import movie


avatar = movie.Movie("Avatar",
                     "A marine on an alien planet",
                     "avatar-2.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers = movie.Movie("Avengers",
                       "Super Heros fighting against evil",
                       "avengers1.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

ultron = movie.Movie("Avengers: Ultron Age",
                     '''Super Heros trying
                     to kill their own AI.''',
                     "ultron.jpg",
                     "https://www.youtube.com/watch?v=tmeOjFno6Do")

infinitive_war = movie.Movie("Avengers: Infinitive War",
                             '''Super Heros fighting
                             against the evil lord of universe''',
                             "war.jpg",
                             "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

jhon_wick = movie.Movie("John Wick",
                        '''A retierd killer lost everything and
                        a guy distroys his world and
                        he will have his revange''',
                        "john-wick1.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

jhon_wick2 = movie.Movie("John Wick: Another day to Kill",
                         '''A old friend comes to charge a special debt,
                         and his life is a mass again''',
                         "john-wick-2-guns.jpg",
                         "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

movies = [avatar, avengers, ultron, infinitive_war, jhon_wick, jhon_wick2]
fresh_tomatoes.open_movies_page(movies)
# fresh_tomatoes abre todo um script com layout para o web site de trailers.
