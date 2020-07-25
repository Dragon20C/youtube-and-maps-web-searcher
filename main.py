import webbrowser

while True:
    user = input("What do you want to so a youtube search or a google maps search?").lower()
    if user == "youtube":
        print("Please type what you want to search on youtube?")
        user = input()
        webbrowser.open("https://www.youtube.com/results?search_query=" + user)
        break
    elif user == "google maps" or user == "maps" or user == "map":
        print("Please type what you want to search on google maps?")
        user = input()
        webbrowser.open("https://www.google.com/maps/place/" + user)
        break
    else:
        print("That isn't a valid option")
