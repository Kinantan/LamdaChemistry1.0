print(r"""\ 
 ___            __       ___      ___  ________       __      
|"  |          /""\     |"  \    /"  ||"      "\     /""\     
||  |         /    \     \   \  //   |(.  ___  :)   /    \    
|:  |        /' /\  \    /\\  \/.    ||: \   ) ||  /' /\  \   
 \  |___    //  __'  \  |: \.        |(| (___\ || //  __'  \  
( \_|:  \  /   /  \\  \ |.  \    /:  ||:       :)/   /  \\  \ 
 \_______)(___/    \___)|___|\__/|___|(________/(___/    \___)
                                                
                                                              

""")

def formatInput(textline):
    textline = textline.lower().strip()
    wordlist = textline.split()
    textline = " ".join(wordlist)
    return textline


def nobleGases(valenceE):
    if valenceE >= 118: return "[Og]"
    if valenceE >= 86: return "[Rn]"
    if valenceE >= 54: return "[Xe]"
    if valenceE >= 36: return "[Kr]"
    if valenceE >= 18: return "[Ar]"
    if valenceE >= 10: return "[Ne]"
    if valenceE >= 2: return "[He]"
    return ""


def atomicRounder(valenceE):
    if valenceE >= 118: return 118
    if valenceE >= 86: return 86
    if valenceE >= 54: return 54
    if valenceE >= 36: return 36
    if valenceE >= 18: return 18
    if valenceE >= 10: return 10
    if valenceE >= 2: return 2


global charge

electronList = ["1s^1", "1s^2", "2s^1", "2s^2", "2p^1", "2p^2", "2p^3", "2p^4", "2p^5", "2p^6", "3s^1", "3s^2",
                "3p^1", "3p^2", "3p^3", "3p^4", "3p^5", "3p^6", "4s^1", "4s^2", "3d^1", "3d^2", "3d^3", "3d^4",
                "3d^5", "3d^6", "3d^7", "3d^8", "3d^9", "3d^10", "4p^1", "4p^2", "4p^3", "4p^4", "4p^5", "4p^6",
                "5s^1", "5s^2", "4d^1", "4d^2", "4d^3", "4d^4", "4d^5", "4d^6", "4d^7", "4d^8", "4d^9", "4d^10",
                "5p^1", "5p^2", "5p^3", "5p^4", "5p^5", "5p^6", "6s^1", "6s^2", "4f^1", "4f^2", "4f^3", "4f^4",
                "4f^5", "4f^6", "4f^7", "4f^8", "4f^9", "4f^10", "4f^11", "4f^12", "4f^13", "4f^14", "5d^1", "5d^2",
                "5d^3", "5d^4", "5d^5", "5d^6", "5d^7", "5d^8", "5d^9", "5d^10", "6p^1", "6p^2", "6p^3", "6p^4", "6p^5",
                "6p^6", "7s^1", "7s^2", "5f^1", "5f^2", "5f^3", "5f^4", "5f^5", "5f^6", "5f^7", "5f^8", "5f^9", "5f^10",
                "5f^11", "5f^12", "5f^13", "5f^14", "6d^1", "6d^2", "6d^3", "6d^4", "6d^5", "6d^6", "6d^7", "6d^8",
                "6d^9", "6d^10", "7p^1", "7p^2", "7p^3", "7p^4", "7p^5", "7p^6"]
elementsAb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
              "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
              "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
              "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
              "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
              "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs",
              "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
elementsFull = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
                "Neon",
                "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorous", "Sulfur", "Chloride", "Argon",
                "Potassium",
                "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickle",
                "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium",
                "Strontium",
                "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium",
                "Silver",
                "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
                "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
                "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
                "Tungsten",
                "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth",
                "Polonium",
                "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium",
                "Neptunium",
                "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
                "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium"]

atomicNumber = 0
looping = True


while looping:
    choice = formatInput(input(
        "Lamda Electron Configuration Calculator!\nAre you entering the atomic number or element name?: "))
    if choice == "atomic number":
        atomicNumber = input("Please input the atomic number of your element: ")

        while not atomicNumber.isnumeric() or atomicNumber == "0":
            atomicNumber = input("Invalid input. Please enter a positive integer value: ")
        atomicNumber = int(atomicNumber)
        break
    elif choice == "element name":
        elementName = input("Please input the name of your element (abbreviated or full): ").capitalize()

        while elementName not in elementsAb and elementName not in elementsFull:
            elementName = input("Element name not recognized. Please try again.").capitalize()

        try:
            atomicNumber = elementsAb.index(elementName)
        except ValueError:
            atomicNumber = elementsFull.index(elementName)
        # you must add 1 to the atomic number as the index starts at 0, but the atomic number starts at 1
        atomicNumber = atomicNumber + 1
        break
    else:
        input("Invalid input. Please type ""atomic number"" or ""element name"". Press any button to continue")


while looping:
    charge = input(
        "Now that you have entered your element, please enter its change. (use + or -, or enter 0 if it has no charge): ")
    if not charge.lstrip("+-").isnumeric():
        charge = input("You have entered an invalid charge. Please input a valid charge: ")
    charge = int(charge)

    atomicNumber = atomicNumber - charge
    break

print("The name of your element is:", elementsFull[atomicNumber + charge - 1])
print("Your full electron configuration is: \n" + ' '.join(map(str, electronList[0:atomicNumber])))
print(("Your condensed electron configuration is: \n" + nobleGases(len(electronList[0:atomicNumber])) + " " +
       ' '.join(map(str, electronList[atomicRounder(atomicNumber):atomicNumber]))).strip())
