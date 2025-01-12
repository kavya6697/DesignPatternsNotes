### Flyweight Design Pattern

### Scenario: Game Application Optimization

from abc import ABC, abstractmethod

# Flyweight (Abstract Class)
class Avatar(ABC):
    @abstractmethod
    def display(self, player_name, health, position):
        pass


# Concrete Flyweight (Shared Avatar)
class SharedAvatar(Avatar):
    def __init__(self, avatar_model):
        self.avatar_model = avatar_model  # The intrinsic state (shared data)

    def display(self, player_name, health, position):
        print(f"Displaying {self.avatar_model} for {player_name} at position {position} with health {health}")


# Flyweight Factory (Responsible for managing the flyweights)
class AvatarFactory:
    def __init__(self):
        self._avatars = {}

    def get_avatar(self, avatar_model):
        # If the avatar is not created yet, create and store it
        if avatar_model not in self._avatars:
            self._avatars[avatar_model] = SharedAvatar(avatar_model)
            print(f"Creating new avatar model: {avatar_model}")
        return self._avatars[avatar_model]


# Client Class (Player in the game)
class Player:
    def __init__(self, player_name, avatar_model, health, position):
        self.player_name = player_name
        self.avatar_model = avatar_model  # Avatar model shared across multiple players
        self.health = health
        self.position = position

    def display(self, avatar_factory):
        # Get the shared avatar from the factory
        avatar = avatar_factory.get_avatar(self.avatar_model)
        avatar.display(self.player_name, self.health, self.position)


# Game Simulation
def game_simulation():
    # Create an AvatarFactory to manage avatar instances
    avatar_factory = AvatarFactory()

    # Create players with different states but sharing the same avatar model
    player1 = Player("Player1", "Knight Avatar", 100, (10, 20))
    player2 = Player("Player2", "Knight Avatar", 80, (30, 40))
    player3 = Player("Player3", "Archer Avatar", 90, (50, 60))
    player4 = Player("Player4", "Knight Avatar", 95, (70, 80))

    # Displaying each player
    player1.display(avatar_factory)
    player2.display(avatar_factory)
    player3.display(avatar_factory)
    player4.display(avatar_factory)


# Run the game simulation
game_simulation()


### Expected Output
# Creating new avatar model: Knight Avatar
# Displaying Knight Avatar for Player1 at position (10, 20) with health 100
# Displaying Knight Avatar for Player2 at position (30, 40) with health 80
# Creating new avatar model: Archer Avatar
# Displaying Archer Avatar for Player3 at position (50, 60) with health 90
# Displaying Knight Avatar for Player4 at position (70, 80) with health 95