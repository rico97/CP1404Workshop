color_names = {"Aliceblue":	"#f0f8ff", "Antiquewhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000", "Blanchedalmond": "#ffebcd", "Blueviolet": "#8a2be2", "Brown": "#a52a2a", "Burlywood": "#deb887", "Cadetblue": "#5f9ea0", "Coral": "#ff7f50" }
name = input("Enter a name:").capitalize()
for key,value in color_names.items():
    if name == key:
        print(value)
if name not in color_names.keys():
    print("No color hex detected for that name")