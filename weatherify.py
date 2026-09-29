print("           WEATHERIFY")
print("   Weather and Lifestyle Assistant")
print("===================================")

#user details
name = input("Enter your name: ")
phoneno = int(input("Enter your phone number: "))
city = input("Enter your city: ")
temp = float(input("Enter temperature in Celsius: "))
weather = input("Enter weather: ").lower().strip()

print("\n========== USER DETAILS ==========")
print("Hello", name)
print("Phone number:", phoneno)
print("City:", city)
print("Temperature:", temp, "°C")
print("Weather:", weather)

#phoneno check
def digits(phoneno):
    count = 0
    while phoneno > 0:
        phoneno = phoneno // 10
        count = count + 1

    if count == 10:
        print("Valid 10-digit number")
    else:
        print("Not a 10-digit number")

#suggestion for clothing
def clothing(temp):
    print("\n========== CLOTHING ==========")

    if temp < -50:
        print("Extreme cold! Wear thermal layers,")
        print("a heavy parka, gloves, and boots.")
    elif temp < -30:
        print("Wear a thick winter coat, thermal")
        print("clothes, gloves, and a hat.")
    elif temp < 0:
        print("Wear a winter jacket, sweater,")
        print("gloves, and warm shoes.")
    elif temp < 10:
        print("Wear a warm jacket and full sleeves.")
    elif temp < 20:
        print("Wear a light jacket or sweater.")
    elif temp < 30:
        print("Wear comfortable clothes.")
    elif temp < 40:
        print("Wear light cotton clothes and a cap.")
    elif temp <= 60:
        print("Extreme heat! Wear loose, light")
        print("coloured cotton clothes.")
        print("Stay in a cool place.")
    else:
        print("Temperature is outside -60 to 60°C.")

#umbrella
def umbrella(weather):
    print("\n========== UMBRELLA ==========")
    if weather in ["rainy", "drizzly"]:
        print("Carry an umbrella!")
    elif weather in ["stormy", "thunderstorm"]:
        print("Stay indoors. Avoid going outside.")
    else:
        print("You may not need an umbrella.")

#breathable clothes
def humidity(weather):
    if weather == "humid":
        print("\nWear breathable cotton clothes.")
        print("Drink plenty of water!")

#sunglasses and sunscreen
def sun(weather):
    if weather == "sunny":
        print("\nWear sunglasses and apply sunscreen!")

#suggestion for songs
def songs(weather):
    print("\n========== SONGS ==========")

    if weather == "sunny":
        print("Listen to happy and energetic songs.")
    elif weather == "rainy":
        print("Listen to romantic and relaxing songs.")
    elif weather == "cloudy":
        print("Listen to calm and peaceful songs.")
    elif weather == "windy":
        print("Listen to upbeat songs.")
    elif weather == "snowy":
        print("Listen to soft and cozy songs.")
    elif weather == "foggy":
        print("Listen to slow and soothing songs.")
    elif weather == "humid":
        print("Listen to refreshing and cheerful songs.")
    elif weather == "stormy":
        print("Listen to relaxing songs.")
    elif weather == "thunderstorm":
        print("Listen to calming music indoors.")
    elif weather == "drizzly":
        print("Listen to soft acoustic songs.")
    else:
        print("Listen to your favourite songs.")

#suggestion for food
def food(weather):
    print("\n========== FOOD ==========")

    if weather == "sunny":
        print("Eat watermelon and fresh fruits.")
    elif weather == "rainy":
        print("Enjoy hot pakoras and soup.")
    elif weather == "cloudy":
        print("Eat warm snacks and drink tea.")
    elif weather == "windy":
        print("Eat light meals and warm soup.")
    elif weather == "snowy":
        print("Enjoy hot soup and warm meals.")
    elif weather == "foggy":
        print("Eat a hot breakfast.")
    elif weather == "humid":
        print("Eat salads and juicy fruits.")
    elif weather == "stormy":
        print("Enjoy warm homemade food.")
    elif weather == "thunderstorm":
        print("Eat a warm meal indoors.")
    elif weather == "drizzly":
        print("Enjoy hot soup or noodles.")
    else:
        print("Eat your favourite food.")

#tips for health
def health(temp):
    print("\n========== HEALTH TIPS ==========")

    if temp >= 32:
        print("Drink water and avoid excessive heat.")
    elif temp <= 18:
        print("Keep yourself warm.")
    else:
        print("Stay hydrated and dress comfortably.")

    print("Take medicines only if prescribed by a doctor.")

#all function
print("\n========== RECOMMENDATIONS ==========")

digits(phoneno)

if -60 <= temp <= 60:
    clothing(temp)
else:
    print("Temperature must be between -60 and 60°C.")

umbrella(weather)
humidity(weather)
sun(weather)
songs(weather)
food(weather)
health(temp)

print("\nThank you for using WEATHERIFY!")