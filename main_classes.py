# Classe que representa o resultado da batalha
class BattleResult():
    def __init__(self):
        self.observers = []
        self.winner_name = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, winner_name):
        for observer in self.observers:
            observer.update(winner_name)

    def set_winner(self, winner_name):
        self.winner_name = winner_name
        self.notify_observers(winner_name)

# Classe que representa um jogador
class Player():
    def __init__(self, player_name):
        self.player_name = player_name

    def update(self, winner_name):
        if self.player_name == winner_name:
            print(f"Parabéns, você venceu a batalha!")
        else:
            print(f"Você perdeu a batalha. O vencedor é: {winner_name}")

