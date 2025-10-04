class Smartphone:
    """Base class representing a smartphone"""

    def __init__(self, brand, model, storage, battery_life, price):
        # Encapsulated attributes (private)
        self._brand = brand
        self._model = model
        self._storage = storage  # in GB
        self._battery_life = battery_life  # in hours
        self._price = price
        self._is_on = False
        self._battery_level = 100

    # Public methods to access private attributes (getters)
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_price(self):
        return self._price

    # Public methods to modify private attributes (setters)
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
            print(f"📱 Price updated to ${new_price}")
        else:
            print("❌ Price must be positive!")

    def power_on(self):
        if not self._is_on:
            self._is_on = True
            print(f"🔋 {self._brand} {self._model} is now ON")
        else:
            print("📱 Phone is already on")

    def power_off(self):
        if self._is_on:
            self._is_on = False
            print(f"🔌 {self._brand} {self._model} is now OFF")
        else:
            print("📱 Phone is already off")

    def make_call(self, number):
        if self._is_on and self._battery_level > 5:
            print(f"📞 Calling {number}...")
            self._battery_level -= 5
            return True
        else:
            print("❌ Cannot make call - check power or battery")
            return False

    def check_battery(self):
        print(f"🔋 Battery level: {self._battery_level}%")
        return self._battery_level

    def charge(self, minutes=30):
        charge_amount = minutes * 0.5  # 1% per 2 minutes
        self._battery_level = min(100, self._battery_level + charge_amount)
        print(
            f"⚡ Charged for {minutes} minutes. Battery: {self._battery_level:.1f}%")

    def display_info(self):
        return f"""
📱 {self._brand} {self._model}
💾 Storage: {self._storage}GB
🔋 Battery Life: {self._battery_life} hours
💰 Price: ${self._price}
📊 Status: {'ON' if self._is_on else 'OFF'}
"""


class GamingPhone(Smartphone):
    """Inherited class specifically for gaming phones"""

    def __init__(self, brand, model, storage, battery_life, price, gpu, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, battery_life, price)
        self._gpu = gpu
        self._cooling_system = cooling_system
        self._refresh_rate = refresh_rate  # in Hz
        self._game_mode = False

    def activate_game_mode(self):
        self._game_mode = True
        print(
            f"🎮 Game Mode activated! {self._refresh_rate}Hz refresh rate enabled")
        self._battery_level -= 10  # Game mode uses more battery

    def deactivate_game_mode(self):
        self._game_mode = False
        print("🎮 Game Mode deactivated")

    def play_game(self, game_name):
        if self._is_on and self._battery_level > 15:
            print(f"🎯 Playing {game_name} with {self._gpu} GPU")
            if not self._game_mode:
                self.activate_game_mode()
            self._battery_level -= 20
            return f"🔥 Gaming experience with {self._cooling_system} cooling!"
        else:
            return "❌ Cannot play game - check power or battery"

    # Overriding the display_info method (polymorphism)
    def display_info(self):
        base_info = super().display_info()
        gaming_features = f"""
🎮 Gaming Features:
   GPU: {self._gpu}
   Cooling: {self._cooling_system}
   Refresh Rate: {self._refresh_rate}Hz
   Game Mode: {'Active' if self._game_mode else 'Inactive'}
"""
        return base_info + gaming_features


class BudgetPhone(Smartphone):
    """Inherited class for budget smartphones"""

    def __init__(self, brand, model, storage, battery_life, price, dual_sim=False):
        super().__init__(brand, model, storage, battery_life, price)
        self._dual_sim = dual_sim
        self._data_saver = True

    def toggle_data_saver(self):
        self._data_saver = not self._data_saver
        status = "ON" if self._data_saver else "OFF"
        print(f"📊 Data Saver mode: {status}")

    def make_call(self, number):  # Overriding method (polymorphism)
        if self._is_on and self._battery_level > 3:  # Budget phones are more efficient
            print(f"📞 Calling {number} (Budget mode)...")
            self._battery_level -= 3
            return True
        else:
            print("❌ Cannot make call - check power or battery")
            return False

    # Overriding display_info method
    def display_info(self):
        base_info = super().display_info()
        budget_features = f"""
💰 Budget Features:
   Dual SIM: {'Yes' if self._dual_sim else 'No'}
   Data Saver: {'ON' if self._data_saver else 'OFF'}
"""
        return base_info + budget_features


class Animal:
    """Base class for all animals"""

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def move(self):
        return "🐾 The animal moves in its own way"

    def speak(self):
        return "🔊 The animal makes a sound"

    def display_info(self):
        return f"🐾 {self.name} lives in {self.habitat}"


class Fish(Animal):
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count

    def move(self):  # Polymorphism - different implementation
        return "🐠 Swimming gracefully through the water"

    def speak(self):
        return "💦 Glub glub! (Fish bubbles)"

    def display_info(self):
        return f"🐠 {self.name} lives in {self.habitat} and has {self.fin_count} fins"


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def move(self):  # Polymorphism - different implementation
        return "🦅 Soaring high in the sky with graceful wings"

    def speak(self):
        return "🎵 Tweet tweet! (Melodious chirping)"

    def display_info(self):
        return f"🦅 {self.name} lives in {self.habitat} with {self.wingspan}cm wingspan"


class Cheetah(Animal):
    def __init__(self, name, habitat, top_speed):
        super().__init__(name, habitat)
        self.top_speed = top_speed

    def move(self):  # Polymorphism - different implementation
        return f"🐆 Running at incredible speed of {self.top_speed} km/h!"

    def speak(self):
        return "🐾 Growl! (Powerful roar)"

    def display_info(self):
        return f"🐆 {self.name} lives in {self.habitat} and can run {self.top_speed} km/h"


# Vehicle classes demonstrating polymorphism
class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    def move(self):
        return "🚗 The vehicle moves"

    def honk(self):
        return "📢 Beep beep!"

    def display_info(self):
        return f"🚗 {self.brand} {self.model} - Max speed: {self.max_speed}"


class Car(Vehicle):
    def move(self):  # Polymorphism
        return "🚗 Driving smoothly on the road"

    def honk(self):
        return "📢 Honk honk! (Car horn)"


class Plane(Vehicle):
    def __init__(self, brand, model, max_speed, wingspan):
        super().__init__(brand, model, max_speed)
        self.wingspan = wingspan

    def move(self):  # Polymorphism
        return "✈️ Flying high above the clouds"

    def honk(self):
        return "🛩️ Woosh! (Jet engine roar)"

    def display_info(self):
        return f"✈️ {self.brand} {self.model} - Max speed: {self.max_speed}, Wingspan: {self.wingspan}m"


class Boat(Vehicle):
    def move(self):  # Polymorphism
        return "⛵ Sailing across the water"

    def honk(self):
        return "🚢 Toot toot! (Ship horn)"


# Demonstration function showing polymorphism in action
def demonstrate_polymorphism():
    print("=" * 50)
    print("🎭 POLYMORPHISM DEMONSTRATION")
    print("=" * 50)

    # Animals demonstrating polymorphism
    print("\n🐾 ANIMALS MOVING DIFFERENTLY:")
    animals = [
        Fish("Nemo", "ocean", 5),
        Bird("Eagle", "mountains", 200),
        Cheetah("Flash", "savannah", 120)
    ]

    for animal in animals:
        print(f"{animal.display_info()}")
        print(f"   Movement: {animal.move()}")
        print(f"   Sound: {animal.speak()}")
        print()

    # Vehicles demonstrating polymorphism
    print("\n🚗 VEHICLES MOVING DIFFERENTLY:")
    vehicles = [
        Car("Toyota", "Camry", 180),
        Plane("Boeing", "747", 900, 60),
        Boat("Yamaha", "Speedboat", 80)
    ]

    for vehicle in vehicles:
        print(f"{vehicle.display_info()}")
        print(f"   Movement: {vehicle.move()}")
        print(f"   Sound: {vehicle.honk()}")
        print()


# Main demonstration
if __name__ == "__main__":
    print("🏗️ ASSIGNMENT 1: SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 50)

    # Create different smartphone objects
    iphone = Smartphone("Apple", "iPhone 15", 128, 20, 999)
    gaming_phone = GamingPhone(
        "ASUS", "ROG Phone", 512, 18, 1299, "Adreno 660", "Vapor Chamber", 144)
    budget_phone = BudgetPhone("Xiaomi", "Redmi Note", 64, 36, 299, True)

    # Demonstrate smartphone functionalities
    phones = [iphone, gaming_phone, budget_phone]

    for phone in phones:
        print(phone.display_info())

        phone.power_on()
        phone.make_call("123-456-7890")
        phone.check_battery()

        # Demonstrate unique behaviors through polymorphism
        if isinstance(phone, GamingPhone):
            phone.play_game("Call of Duty")
        elif isinstance(phone, BudgetPhone):
            phone.toggle_data_saver()

        phone.charge(60)
        print("-" * 40)

    # Demonstrate polymorphism challenge
    demonstrate_polymorphism()
