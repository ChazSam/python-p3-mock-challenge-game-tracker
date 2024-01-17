class Game:

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
            
    def results(self):
       return [ x for x in Result.all if x.game == self ]
        
    def players(self):
        return list(set([ (x.player) for x in Result.all if x.game == self ]))

    def average_score(self, player):
        score = [ x.score for x in Result.all if x.player == player ]
        return sum(score) / len(score)

class Player:
    
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [ x for x in Result.all if x.player == self ]

    def games_played(self):
        return list(set([ x.game for x in Result.all if x.player == self ]))

    def played_game(self, game):
        played = [ x.game for x in Result.all if x.player == self and x.game == game ]
        if len(played) > 0:
            return True
       
        return False

    def num_times_played(self, game):
        played = [ x for x in Result.all if x.player == self and x.game == game ]
        return len(played)


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
