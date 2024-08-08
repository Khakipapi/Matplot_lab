"""imports operator"""
import operator
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# heading
print("Jose Reyes")  # name
print("SDEV 300")  # course
print(date.today())  # date
print("Lab3")


class USStates:
    """Create an object for the 50 states """
    def __init__(self, us_states, capitol, state_pop, image, flower):
        self.us_states = us_states
        self.capitol = capitol
        self.state_pop = state_pop
        self.image = image
        self.flower = flower


# read in images
AL_IMAGE = 'flowers_lab3/kisspng-garden-roses-camellia-flower-pattern-camellia-flowers-5.png'
AK_IMAGE = 'flowers_lab3/forget me not .png'
AZ_IMAGE = 'flowers_lab3/Saguaro Blossoms.jpeg'
AR_IMAGE = 'flowers_lab3/Apple blossom_.jpeg'
CA_IMAGE = 'flowers_lab3/CaliforniaPoppy.png'
CO_IMAGE = 'flowers_lab3/RockyMountainColumbine.png'
DE_IMAGE = 'flowers_lab3/PeachBlossom.png'
FL_IMAGE = 'flowers_lab3/OrangeBlossom.png'
GA_IMAGE = 'flowers_lab3/CherokeeRose.png'
HI_IMAGE = 'flowers_lab3/PuaAloalo.png'
ID_IMAGE = 'flowers_lab3/Idaho State Flower _ Syringa.jpeg'
IL_IMAGE = 'flowers_lab3/State Flower of Illinois.jpeg'
IN_IMAGE = 'flowers_lab3/Indiana State Flower _ Peony.png'
IA_IMAGE = 'flowers_lab3/WildPraireRose.png'
KS_IMAGE = 'flowers_lab3/WildNativeSunflower.png'
KY_IMAGE = 'flowers_lab3/Goldenrod.png'
LA_IMAGE = 'flowers_lab3/Magnolia.png'
ME_IMAGE = 'flowers_lab3/WhitePineConeAndTassel.png'
MD_IMAGE = 'flowers_lab3/Black-eyed Susan.png'
MA_IMAGE = 'flowers_lab3/Mayflower.png'
MI_IMAGE = 'flowers_lab3/AppleBlossom.png'
MN_IMAGE = 'flowers_lab3/Lady Slipper.jpeg'
MS_IMAGE = 'flowers_lab3/Magnolia.png'
MO_IMAGE = 'flowers_lab3/White Hawthorn Blossom.jpeg'
MT_IMAGE = 'flowers_lab3/Bitterroot.jpeg'
NE_IMAGE = 'flowers_lab3/Goldenrod.png'
NV_IMAGE = 'flowers_lab3/Sagebrush.jpeg'
NH_IMAGE = 'flowers_lab3/Purple Lilac.jpeg'
NJ_IMAGE = 'flowers_lab3/PurpleViolet.jpeg'
NM_IMAGE = 'flowers_lab3/New Mexico State Flower _ Yucca.jpeg'
NY_IMAGE = 'flowers_lab3/New York State Flower_ Rose.png'
NC_IMAGE = 'flowers_lab3/Flowering Dogwood.jpeg'
ND_IMAGE = 'flowers_lab3/Wild Prairie Rose.jpeg'
OH_IMAGE = 'flowers_lab3/Ohio State Flower - Scarlet Carnation.jpeg'
OK_IMAGE = 'flowers_lab3/Oklahoma State Flower.jpeg'
OR_IMAGE = 'flowers_lab3/Oregon grape blossoms.jpeg'
PA_IMAGE = 'flowers_lab3/Mountain Laurel.jpeg'
RI_IMAGE = 'flowers_lab3/Rhode Island State Flower_ Violet.png'
SC_IMAGE = 'flowers_lab3/South Carolina State Flower, Yellow Jessamine ' \
           '(Gelsemium sempervirens),.jpeg'
SD_IMAGE = 'flowers_lab3/South Dakota State Flower _ Pasque Flower.jpeg'
TN_IMAGE = 'flowers_lab3/Tennessee State Cultivated Flower_ Iris.png'
TX_IMAGE = 'flowers_lab3/Bluebonnets!.jpeg'
UT_IMAGE = 'flowers_lab3/Sego lily .jpeg'
VT_IMAGE = 'flowers_lab3/Vermont State Flower _ Red Clover.jpeg'
VA_IMAGE = 'flowers_lab3/Dogwood.jpeg'
WA_IMAGE = 'flowers_lab3/Washington State Flower _ Coast Rhododendron.jpeg'
WV_IMAGE = 'flowers_lab3/West Virginia State Flower_ Rhododendron ' \
           '(Big Laurel).png'
WI_IMAGE = 'flowers_lab3/Wisconsin Wildflower _ Wood Violet _ Viola' \
           ' papilionacea_ The Wisconsin state flower.png'
WY_IMAGE = 'flowers_lab3/Wyoming State Flower, Indian Paintbrush.jpeg'

# population variables
AL_POP = 4893000
AK_POP = 736990
AZ_POP = 7278717
AR_POP = 3017804
CA_POP = 39512223
CO_POP = 5758736
DE_POP = 973764
FL_POP = 21477737
GA_POP = 10617423
HI_POP = 1415872
ID_POP = 1787065
IL_POP = 12671821
IN_POP = 6732219
IA_POP = 3155070
KS_POP = 2913314
KY_POP = 4467673
LA_POP = 4648794
ME_POP = 1344212
MD_POP = 6045680
MA_POP = 6892503
MI_POP = 9986857
MN_POP = 5639632
MS_POP = 2976149
MO_POP = 6137428
MT_POP = 1068778
NE_POP = 1826341
NV_POP = 2700551
NH_POP = 1316472
NJ_POP = 8791894
NM_POP = 2059180
NY_POP = 19378104
NC_POP = 9535475
ND_POP = 672591
OH_POP = 11536502
OK_POP = 3751354
OR_POP = 3831074
PA_POP = 12702379
RI_POP = 1052567
SC_POP = 4625364
SD_POP = 814180
TN_POP = 6346110
TX_POP = 25145561
UT_POP = 2763885
VT_POP = 625741
VA_POP = 8001024
WA_POP = 6724540
WV_POP = 1852996
WI_POP = 5686986
WY_POP = 563626

# state objects
alabama = USStates("Alabama", "Montgomery", AL_POP, AL_IMAGE, "Camellia")
alaska = USStates("Alaska", "Juneau", AK_POP, AK_IMAGE, "Forget Me Not")
arizona = USStates("Arizona", "Phoenix", AZ_POP, AZ_IMAGE, "Saguaro Blossoms")
arkansas = USStates("Arkansas", "Little Rock", AR_POP, AR_IMAGE, "Apple Blossoms")
california = USStates("California", "Sacramento", CA_POP, CA_IMAGE, "California Poppy")
colorado = USStates("Colorado", "Denver", CO_POP, CO_IMAGE, "Rocky Mountain Columbine")
delaware = USStates("Delaware", "Dover", DE_POP, DE_IMAGE, "Peach Blossom")
florida = USStates("Florida", "Tallahassee", FL_POP, FL_IMAGE, "Orange Blossom")
georgia = USStates("Georgia", "Atlanta", GA_POP, GA_IMAGE, "Cherokee Rose")
hawaii = USStates("Hawaii", "Honolulu", HI_POP, HI_IMAGE, "Pua Aloalo")
idaho = USStates("Idaho", "Boise", ID_POP, ID_IMAGE, "Syringa")
illinois = USStates("Illinois", "Springfield", IL_POP, IL_IMAGE, "Violet")
indiana = USStates("Indiana", "Springfield", IN_POP, IN_IMAGE, "Peony")
iowa = USStates("Iowa", "Des Moines", IA_POP, IA_IMAGE, "Wild Prairie Rose")
kansas = USStates("Kansas", "Topeka", KS_POP, KS_IMAGE, "Wild Native Sunflower")
kentucky = USStates("Kentucky", "Frankfort", KY_POP, KY_IMAGE, "Goldenrod")
louisiana = USStates("Louisiana", "Baton Rouge", LA_POP, LA_IMAGE, "Magnolia")
maine = USStates("Maine", "Augusta", ME_POP, ME_IMAGE, "White Pine Cone and Tassel")
maryland = USStates("Maryland", "Annapolis", MD_POP, MD_IMAGE, "Black-eyed Susan")
massachusetts = USStates("Massachusetts", "Boston", MA_POP, MA_IMAGE, "Mayflower")
michigan = USStates("Michigan", "Lansing", MI_POP, MI_IMAGE, "Apple Blossom")
minnesota = USStates("Minnesota", "Saint Paul", MN_POP, MN_IMAGE, "Pink and White Lady Slipper")
mississippi = USStates("Mississippi", "Jackson", MS_POP, MS_IMAGE, "Magnolia")
missouri = USStates("Missouri", "Jefferson City", MO_POP, MO_IMAGE, "White Hawthorn Blossom")
montana = USStates("Montana", "Helena", MT_POP, MT_IMAGE, "Bitterroot")
nebraska = USStates("Nebraska", "Lincoln", NE_POP, NE_IMAGE, "Goldenrod")
nevada = USStates("Nevada", "Carson City", NV_POP, NV_IMAGE, "Sagebrush")
new_hampshire = USStates("New Hampshire", "Concord", NH_POP, NH_IMAGE, "Purple Lilac")
new_jersey = USStates("New Jersey", "Trenton", NJ_POP, NJ_IMAGE, "Purple Violet")
new_mexico = USStates("New Mexico", "Santa Fe", NM_POP, NM_IMAGE, "Yucca")
new_york = USStates("New York", "Albany", NY_POP, NY_IMAGE, "Rose")
north_carolina = USStates("New Carolina", "Raleigh", NC_POP, NC_IMAGE, "Dogwood")
north_dakota = USStates("North Dakota", "Bismarck", ND_POP, ND_IMAGE, "Wild Prairie Rose")
ohio = USStates("Ohio", "Columbus", OH_POP, OH_IMAGE, "Scarlet Carnation")
oklahoma = USStates("Oklahoma", "Oklahoma City", OK_POP, OK_IMAGE, "Mistletoe")
oregon = USStates("Oregon", "Salem", OR_POP, OR_IMAGE, "Oregon Grape")
pennsylvania = USStates("Pennsylvania", "Harrisburg", PA_POP, PA_IMAGE, "Mountain Laurel")
rhode_island = USStates("Rhode Island", "Providence", RI_POP, RI_IMAGE, "Violet")
south_carolina = USStates("South Carolina", "Columbia", SC_POP, SC_IMAGE, "Yellow Jessamine")
south_dakota = USStates("South Dakota", "Pierre", SD_POP, SD_IMAGE, "Pasque Flower")
tennessee = USStates("Tennessee", "Nashville", TN_POP, TN_IMAGE, "Iris")
texas = USStates("Texas", "Austin", TX_POP, TX_IMAGE, "Bluebonnet")
utah = USStates("Utah", "Salt Lake City", UT_POP, UT_IMAGE, "Sego Lily")
vermont = USStates("Vermont", "Montpelier", VT_POP, VT_IMAGE, "Red Clover")
virginia = USStates("Virginia", "Richmond", VA_POP, VA_IMAGE, "Dogwood")
washington = USStates("Washington", "Olympia", WA_POP, WA_IMAGE, "Pink Rhododendron")
west_virginia = USStates("West Virgina", "Charleston", WV_POP, WV_IMAGE, "Rhododendron")
wisconsin = USStates("Wisconsin", "Madison", WI_POP, WI_IMAGE, "Wood Violet")
wyoming = USStates("Wyoming", "Cheyenne", WY_POP, WY_IMAGE, "Indian Paintbrush")

obj = {'AL': alabama, 'AK': alaska, 'AZ': arizona, 'AR': arkansas, 'CA': california,
       'CO': colorado, 'DE': delaware, 'FL': florida, 'GA': georgia, 'HI': hawaii,
       'ID': idaho, 'IN': indiana, 'IA': iowa, 'KS': kansas, 'KY': kentucky, 'LA': louisiana,
       'ME': maine, 'MD': maryland, 'MN': minnesota, 'MS': mississippi, 'MO': missouri,
       'MT': montana, 'NE': nebraska, 'NV': nevada, 'NH': new_hampshire,
       'NM': new_mexico, 'NY': new_york, 'NC': north_carolina,
       'ND': north_dakota, 'OH': ohio, 'OK': oklahoma, 'OR': oregon, 'PA': pennsylvania,
       'RI': rhode_island, 'SC': south_carolina, 'SD': south_dakota, 'TN': tennessee,
       'TX': texas, 'UT': utah, 'VT': vermont, 'VA': virginia, 'WA': washington,
       'WV': west_virginia,'WI': wisconsin, 'WY': wyoming}


def state_list():
    """Sate def"""
    for key in obj.values():
        print("")
        print('State: ' + key.us_states)
        print('Capitol: ' + key.capitol)
        print('Population: ' + str(key.state_pop))
        print('Flower: ' + key.flower)
        print("")


def search():
    """Search def"""
    input2 = input("Please enter the two letter state abbreviation: ")
    while len(input2) != 2 or input2 not in obj:
        print("Invalid Entry: must be two letters and a state!")
        input2 = input("Please enter the two letter state abbreviation: ")

    if input2 in obj:
        print("")
        show = mpimg.imread(obj.get(input2).image)
        show2 = plt.imshow(show)
        print(show2)
        plt.show()
        print("State: " + obj.get(input2).us_states)
        print("Capitol: " + obj.get(input2).capitol)
        print("Population: " + str(obj.get(input2).state_pop))
        print("Flower: " + obj.get(input2).flower)
        print("")


def bar_graph():
    """Bar graph"""
    count = 1
    x_1 = []
    y_1 = []
    for uss in (sorted(obj.values(), key=operator.attrgetter('state_pop'), reverse=True)):
        print("")
        x_1.append(uss.us_states)
        y_1.append(uss.state_pop)
        if count == 5:
            break
        count += 1

    plt.bar(x_1, y_1)
    plt.xlabel("States ")
    plt.ylabel("Million")
    plt.title("Population of the top 5 States")
    plt.show()


def update_pop():
    """Update population"""
    input3 = input("Please enter the state 2 letter abbreviation you which to update:  ")
    input3 = input3.upper()
    update = int(input("Enter the new population number:"))

    while len(input3) != 2 or input3 not in obj:
        print("Invalid Entry: must be two letters and a state!")
        input3 = input("Please enter the two letter state abbreviation:")
        input3 = input3.upper()

    if input3 in obj:
        print("")
        print('State: ' + obj.get(input3).us_states)
        print('Capitol: ' + obj.get(input3).capitol)
        print('Population: ' + str(obj.get(input3).state_pop))
        print('Flower: ' + obj.get(input3).flower)
        print("")
        print("update")
        new = {input3: USStates(obj.get(input3).us_states, obj.get(input3).capitol, update,
                                obj.get(input3).image, obj.get(input3).flower)}
        obj.update(new)

    print("")
    print('State: ' + obj.get(input3).us_states)
    print('Capitol: ' + obj.get(input3).capitol)
    print('Population: ' + str(obj.get(input3).state_pop))
    print('Flower: ' + obj.get(input3).flower)
    print("")


def exits():
    """Exit"""
    thanks = "Thank you for using this app"  # prompt
    return thanks  # returns prompt


print("\nWelcome to the program.\n"
      "This program will ask the for user input to display an object of all 50 states.\n"
      "search for a particular state and provide a graph of the top 5 populated states.")
CHOICE = 0
# while loop to re-run the menu until the exit program has been selected

while CHOICE != 5:
    print('''
******************************Menu*********************************
1. Display all U.S. States in Alphabetical order along with the
Capital, State Population, and Flower
2. Search for a specific state and display the appropriate Capital
name, State Population, and an image of the associated State Flower.
3. Provide a Bar graph of the top 5 populated States showing their
overall population.
4. Update the overall state population for a specific state.
5. Exit the program
    ''')
    choice = int(input('Enter your choice (1-5):'))
    opcode = [state_list, search, bar_graph, update_pop, exits]
    result = opcode[choice - 1]()
    if choice > 5 or choice == 0:
        print("Invalid entry: has to be a number from 1-5")
    elif choice == 5:
        print("Thank you for using this app ")
        break
    print(result)
