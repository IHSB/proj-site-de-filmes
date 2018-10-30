import webbrowser


class Movie():
    def __init__(self, movie_title, movie_story, poster_img, trailer_youtube):
        """Essa funcao contem a classe de cada um dos elementos.
        Leva como argumento:
        movie_title: contem titulo do filme.
        movie_storyline: contem a historia do filme.
        poster_image(str): contem o URL com link da imagem da capa do fime.
        trailer_youtube(str): contem o URL do youtube com o trailer do filme.
        """
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Essa funcao ira abrir o webbrowser com o trailer na pagina local.
        """
        webbrowser.open(self.trailer_youtube_url)
