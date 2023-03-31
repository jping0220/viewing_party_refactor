class Person:
    def __init__(self, name, friends):
        self.name = name
        self.friends = friends
        self.watchlist = []
        self.watched_movies = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_movie_to_watchlist(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
            if movie in self.watchlist:
                self.watchlist.remove(movie)

