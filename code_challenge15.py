#anime watchlist maker
#while loop


animelist = []
proceed = True
print("--Welcome to Anime watch list--")
print("--Enter 'close' to stop listing--")

while proceed == True:
    anime = input("Input your desired anime: ")

    if anime.lower() == "close":
        print("--Your watchlist has been updated--")
        break

    animelist.append(anime)
    print(f"{anime} (has been added to your watch list)")

for i in animelist:
    print(f"- {i}")
    