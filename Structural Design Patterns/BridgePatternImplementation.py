### Bridge Design Pattern

### Scenario: Remote Control Systems for Smart Homes

from abc import ABC, abstractmethod

# The Device interface defines common operations for different devices.
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def set_volume(self, level: int):
        pass

# Concrete Device Classes (e.g., TV and Fan)

class TV(Device):
    def turn_on(self):
        print("TV is now ON")
    
    def turn_off(self):
        print("TV is now OFF")
    
    def set_volume(self, level: int):
        print(f"TV volume set to {level}")

class Fan(Device):
    def turn_on(self):
        print("Fan is now ON")
    
    def turn_off(self):
        print("Fan is now OFF")
    
    def set_volume(self, level: int):
        print(f"Fan speed set to {level}")

# RemoteControl Abstraction

class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device
        self.is_powered = False  # Initialize is_powered
    
    @abstractmethod
    def power(self):
        pass
    
    @abstractmethod
    def volume(self, level: int):
        pass

# Concrete Remote Classes (e.g., BasicRemote and AdvancedRemote)

class BasicRemote(RemoteControl):
    def power(self):
        if self.is_powered:
            print("BasicRemote: Turning off the device")
            self.device.turn_off()
        else:
            print("BasicRemote: Turning on the device")
            self.device.turn_on()
        self.is_powered = not self.is_powered
    
    def volume(self, level: int):
        print("BasicRemote: Adjusting volume")
        self.device.set_volume(level)

class AdvancedRemote(RemoteControl):
    def power(self):
        if self.is_powered:
            print("AdvancedRemote: Turning off the device")
            self.device.turn_off()
        else:
            print("AdvancedRemote: Turning on the device")
            self.device.turn_on()
        self.is_powered = not self.is_powered
    
    def volume(self, level: int):
        print("AdvancedRemote: Adjusting volume")
        self.device.set_volume(level)
    
    def mute(self):
        print("AdvancedRemote: Muting the device")
        self.device.set_volume(0)

# Create some devices
tv = TV()
fan = Fan()

# Use the basic remote to control TV
basic_remote = BasicRemote(tv)
print("Using Basic Remote to control TV:")
basic_remote.power()  # Turn on TV
basic_remote.volume(10)  # Set TV volume

print("\nUsing Basic Remote to control Fan:")
basic_remote.device = fan  # Switch to controlling the Fan
basic_remote.power()  # Turn on Fan
basic_remote.volume(3)  # Set Fan speed

# Use the advanced remote to control the fan
advanced_remote = AdvancedRemote(fan)
print("\nUsing Advanced Remote to control Fan:")
advanced_remote.power()  # Turn on Fan
advanced_remote.volume(5)  # Set Fan speed
advanced_remote.mute()  # Mute the Fan

### Expected Output
# Using Basic Remote to control TV:
# BasicRemote: Turning on the device
# TV is now ON
# BasicRemote: Adjusting volume
# TV volume set to 10

# Using Basic Remote to control Fan:
# BasicRemote: Turning off the device
# Fan is now OFF
# BasicRemote: Adjusting volume
# Fan speed set to 3

# Using Advanced Remote to control Fan:
# AdvancedRemote: Turning on the device
# Fan is now ON
# AdvancedRemote: Adjusting volume
# Fan speed set to 5
# AdvancedRemote: Muting the device
# Fan speed set to 0


