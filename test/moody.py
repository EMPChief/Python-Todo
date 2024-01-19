mood = "happy"
strength = 6.6
rank = 1
color_codes = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

filenames = ['Document.txt', 'Report.txt', 'Presentation.txt']
for i, filename in enumerate(filenames):
    print(f"{i}-{filename}")
    
ips = ['100.122.133.105', '100.122.133.111']
input_nr = int(input("Type the number of the IP you want to see: "))
print(f"You chose {ips[input_nr]}")

temperatures = [float(3.7), int(4.5), "hello"]

rainfall = [3.7, 4, 'hello', ['hello']]

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.pop(1)