from random import choice
from random import sample
print(""" Greetings! I'm James, the Classic Film Bot.""")
print("""Pick a Genre and a Decade of release between 1960 and 1990, and I will recommend to
you 2 movies to watch! There are ten genres and 4 decades of release to pick from. """)
def get_classic_movies():
    Horror60s = ["What Ever Happened to Baby Jane?", "The Terror", "House of Usher"]
    Horror70s = ["The Exorcist", "I Spit on Your Grave", "EraserHead"]
    Horror80s = ["Firestarter", "Poltergeist", "Scanners"]
    Horror90s = ["Candyman", "Anaconda", "Mikey"]
    ScienceFiction60s = ["The Time Machine", "The Last Man on Earth", "Crack in the World"]
    ScienceFiction70s = ["Fantastic Planet", "Rollerball", "Mad Max"] 
    ScienceFiction80s = ["John Carpenter’s They Live", "Scanners", "Videodrome"]
    ScienceFiction90s = ["Ghost in the Shell", "Species", "Deep Impact"]
    Comedy60s = ["The Party", "Paint Your Wagon", "CinderFella"]
    Comedy70s = ["Paper Moon", "Monty Python’s Life of Brian", "Meatballs" ]
    Comedy80s = ["The Lost Boys", "Risky Business", "My Dinner with Andre" ]
    Comedy90s = ["The Big Lebowski", "Liar Liar", "Billy Madison"]
    Thriller60s= ["Dr. No", "The Great Escape", "Judex"]
    Thriller70s = ["The Cat o’ Nine Tails", "The Andromeda Strain", "Vanishing Point"]
    Thriller80s = ["Manhunter", "The Shining", "Blood Simple"]
    Thriller90s = ["Primal Fear", "Closet Land", "Mortal Thoughts"]
    Action60s = ["Bullitt", "Yojimbo", "Sanjuro"]
    Action70s = ["A Bridge Too Far", "Westworld", "The Omega Man"]
    Action80s = ["Midnight Run", "RoboCop", "Above the Law"]
    Action90s = ["Golden Eye", "The Fifth Element", "Days of Thunder"]
    Anime60s = ["Dororo", "Jack and the Witch", "Alakazsm the Great"]
    Anime70s = ["Space Battleship Yamato", "Animal Treasure Island", "30,000 Miles Under the Sea"]
    Anime80s = ["Grave of the Fireflies", "Wicked City", "Lily C.A.T"]
    Anime90s = ["The End of Evangelion", "Princess Mononoke", "Whisper of the Heart"]
    Documentary60s = ["Inquiring Nuns", "Primary (1960)", "Monterey Pop"]
    Documentary70s = ["Goodbye Uncle Tom", "The Legend of Bigfoot", "Bugs Bunny: Superstar"]
    Documentary80s = ["Burden of Dreams", "Koyaanisqatsi", "Imagine: John Lennon"]
    Documentary90s = ["When We Were Kings", "The War Room", "Kurt and Courtney"]
    Romance60s = ["Cleopatra (1963)",  "Breakfast at Tiffany’s", "From Russia with Love"]
    Romance70s = ["Love Story", "Manhattan", "The Great Gatsby"]
    Romance80s = ["The Princess Bride", "Flashdance", "About Last Night"]
    Romance90s = ["Cruel Intentions", "What Dreams May Come", "Notting Hill"]
    Genre = [Horror60s, Horror70s, Horror80s, Horror90s, ScienceFiction60s,
    ScienceFiction70s, ScienceFiction80s, ScienceFiction90s, Comedy60s, Comedy70s,
    Comedy80s, Comedy90s, Thriller60s, Thriller70s, Thriller80s, Thriller90s, Action60s,
    Action70s, Action80s, Action90s, Anime60s, Anime70s, Anime80s, Anime90s, Documentary60s, 
    Documentary70s,Documentary80s, Documentary90s, Romance60s, Romance70s, Romance80s, Romance90s]
    Pick = 1
    GenreNDecade = ""
    GenreNDecade = input("""So what type of movies are you looking for? """)
    if GenreNDecade == "60s Science Fiction":
        Pick = sample(ScienceFiction60s,2)
    elif GenreNDecade in "70s Science Fiction":
        Pick = sample(ScienceFiction70s,2)
    elif GenreNDecade in "80s Science Fiction":
        Pick = sample(ScienceFiction80s,2)
    elif GenreNDecade in "90s Science Fiction":
        Pick = sample(ScienceFiction90s,2)
    elif GenreNDecade in "60s Horror":
        Pick = sample(Horror60s,2)
    elif GenreNDecade in "70s Horror":
        Pick = sample(Horror70s,2)
    elif GenreNDecade in "80s Horror":
        Pick = sample(Horror80s,2)
    elif GenreNDecade in "90s Horror":
        Pick = sample(Horror90s,2)
    elif GenreNDecade in "60s Comedy":
        Pick = sample(Comedy60s,2)
    elif GenreNDecade in "70s Comedy":
        Pick = sample(Comedy70s,2)
    elif GenreNDecade in "80s Comedy":
        Pick = sample(Comedy80s,2)
    elif GenreNDecade in "90s Comedy":
        Pick = sample(Comedy90s,2)
    elif GenreNDecade in "60s Thriller":
        Pick = sample(Thriller60s,2)
    elif GenreNDecade in "70s Thriller":
        Pick = sample(Thriller70s,2)
    elif GenreNDecade in "80s Thriller":
        Pick = sample(Thriller80s,2)
    elif GenreNDecade in "90s Thriller":
        Pick = sample(Thriller90s,2)
    elif GenreNDecade in "60s Action":
        Pick = sample(Action60s,2)
    elif GenreNDecade in "70s Action":
        Pick = sample(Action70s,2)
    elif GenreNDecade in "80s Action":
        Pick = sample(Action80s,2)
    elif GenreNDecade in "90s Action":
        Pick = sample(Action90s,2)
    elif GenreNDecade in "60s Anime":
        Pick = sample(Anime60s,2)
    elif GenreNDecade in "70s Anime":
        Pick = sample(Anime70s,2)
    elif GenreNDecade in "80s Anime":
        Pick = sample(Anime80s,2)
    elif GenreNDecade in "90s Anime":
        Pick = sample(Anime90s,2)
    elif GenreNDecade in "60s Documentary":
        Pick = sample(Documentary60s,2)
    elif GenreNDecade in "70s Documentary":
        Pick = sample(Documentary70s,2)
    elif GenreNDecade in "80s Documentary":
        Pick = sample(Documentary80s,2)
    elif GenreNDecade in "90s Documentary":
        Pick = sample(Documentary90s,2)
    elif GenreNDecade in "60s Romance":
        Pick = sample(Romance60s,2)
    elif GenreNDecade in "70s Romance":
        Pick = sample(Romance70s,2)
    elif GenreNDecade in "80s Romance":
        Pick = sample(Romance80s,2)
    elif GenreNDecade in "90s Romance":
        Pick = sample(Romance90s,2)
    else:
        return "Jimmy the Classic Robot does not recogonize this category"
    return(F"""Your recommended movies are '{Pick[0]}' and '{Pick[1]}'. Check them out on my internet before you have watch, if you'd like.
ENJOY, human!""")

print("""
Genres: Horror, Science Fiction, Thriller, Comedy, Action, Documentary, Romance, and Anime.
Time periods: The 1960s, 1970s, 1980s, and 1990s.
INSTRUCTIONS: Type in the 2-digit decade, followed by an "s", a space and then the genre. 
!!EXAMPLE: If you want a science fiction movie set in the 1970s, type in '70s Science Fiction'.!!""")
christ = 1
while True:
    christ = get_classic_movies()
    print(christ)
    follow_up = (input("Would you like to choose another category? (Type YES OR NO) "))
    if follow_up in "YESYesYEsyesyESyeS":
        continue
    elif follow_up in "NOnoNonO":
        print("Bye!, have a great time!")
        break
    else:
        print("I can't quite understand that.. I'm only a filmbot. I'm not AI! I'll restart anyway....")