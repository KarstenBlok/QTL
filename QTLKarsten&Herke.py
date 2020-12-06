import string
import itertools
def read_file(bestand):
    marker = ""
    file_dictionary = {}
    data = []

    with open(bestand) as file:
        # zorgt ervoor dat het bestand pas vanaf regel 7 wordt gelezen
        for i in range(7):
            line = file.readline()
        # alles regels met een marker beginnen met een letter. deze functie kijkt of de regel begint met een letter.
        # als dit het geval is, maakt hij van de marker een key voor de dictionary. alle regels tot de volgende marker
        # worden toegevoegd aan de dictionary.
        for line in file:
            if line.startswith(tuple(string.ascii_letters)):
                if marker:
                    merged = list(itertools.chain.from_iterable(data))
                    file_dictionary[marker] = merged
                    data = []
                marker = line.split()[0]
            else:
                data.append(line.split())
        file_dictionary[marker] = merged
    return file_dictionary


def vergelijkingen (file_dictionary):
    data_dict = {}
    for marker1 in range(len(file_dictionary.keys())):
        eerste_marker_list = list(file_dictionary.keys())
        for marker2 in range(marker1+1, len(file_dictionary)):
            tweede_marker = eerste_marker_list[marker2]
            aantal = 0
            for a in range(len(eerste_marker_list)):
                eerste_marker = eerste_marker_list[a]
                if file_dictionary[eerste_marker][a] == "-" or file_dictionary[tweede_marker][a] == "-":
                    continue
                elif file_dictionary[eerste_marker][a] != file_dictionary[tweede_marker][a]:
                    aantal += 1
                key = str(eerste_marker) + "-" + str(tweede_marker)
            data_dict[key] = aantal
    print(data_dict)


def main():
    bestand = "CvixLer-MarkerSubset-LG1.txt"
    file_dictionary = read_file(bestand)
    vergelijkingen(file_dictionary)

main()