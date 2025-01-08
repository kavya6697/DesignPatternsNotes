### Facade Pattern

### Scenario Used: Automatic Home Theater System

# Subsystems (Components of the Home Theater System)
class TV:
    def turn_on(self):
        print("Turning on the TV.")

    def set_input(self, input_source):
        print(f"Setting input to {input_source}.")


class DVDPlayer:
    def turn_on(self):
        print("Turning on the DVD player.")
    
    def play(self, movie):
        print(f"Playing the movie: {movie}.")


class SoundSystem:
    def turn_on(self):
        print("Turning on the sound system.")
    
    def set_surround_sound(self):
        print("Setting the sound system to surround sound.")


class Lights:
    def dim(self):
        print("Dimming the lights.")


# Facade: Simplifies interaction with the complex subsystem
class HomeTheaterFacade:
    def __init__(self, tv, dvd_player, sound_system, lights):
        self.tv = tv
        self.dvd_player = dvd_player
        self.sound_system = sound_system
        self.lights = lights
    
    def start_movie(self, movie):
        print("Starting the movie experience:")
        self.tv.turn_on()
        self.tv.set_input("DVD")
        self.dvd_player.turn_on()
        self.dvd_player.play(movie)
        self.sound_system.turn_on()
        self.sound_system.set_surround_sound()
        self.lights.dim()
        print("Movie is ready to be enjoyed!")


# Client code: User only interacts with the Facade
tv = TV()
dvd_player = DVDPlayer()
sound_system = SoundSystem()
lights = Lights()

# Create the Facade that simplifies the process
home_theater = HomeTheaterFacade(tv, dvd_player, sound_system, lights)

# User starts the movie experience
home_theater.start_movie("Inception")


### Expected Outcome
# Starting the movie experience:
# Turning on the TV.
# Setting input to DVD.
# Turning on the DVD player.
# Playing the movie: Inception.
# Turning on the sound system.
# Setting the sound system to surround sound.
# Dimming the lights.
# Movie is ready to be enjoyed!