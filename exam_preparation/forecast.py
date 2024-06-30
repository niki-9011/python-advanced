def forecast(*input_data):
    def sorting_data():
        data = []

        for weather, towns in towns_data.items():
            if towns:
                data.extend([f"{t} - {weather}" for t in sorted(towns)])
        return data

    towns_data = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for town, weather in input_data:
        towns_data[weather].append(town)

    result = sorting_data()

    return '\n'.join(result)



#Part below is part from automatic judge system from SoftUni
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
