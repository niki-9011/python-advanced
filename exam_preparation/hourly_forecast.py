def forecast(*args, **kwargs):
    sunny = {}
    cloudy = {}
    rainy = {}
    result = []

    for x in args:
        if x[1] == "Sunny":
            sunny[x[0]] = x[1]
        elif x[1] == "Cloudy":
            cloudy[x[0]] = x[1]
        elif x[1] == "Rainy":
            rainy[x[0]] = x[1]

    if sunny:
        sunny = sorted(sunny.items(), key=lambda s: (s[0]))
    if cloudy:
        cloudy = sorted(cloudy.items(), key=lambda c: (c[0]))
    if rainy:
        rainy = sorted(rainy.items(), key=lambda r: (r[0]))

    result.extend(sunny), result.extend(cloudy), result.extend(rainy)

    return "\n".join([f"{key} - {value}" for key, value in result])


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
