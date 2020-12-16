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

        for line in file:
            if line.startswith(tuple(string.ascii_letters)) or not line.strip():
                if marker:
                    merged = list(itertools.chain.from_iterable(data))
                    if chi_quare(merged):
                        file_dictionary[marker] = merged
                    data = []
                if line.strip():
                    marker = line.split()[0]
            else:
                data.append(line.split())
        totaal = len(merged)
        file_dictionary[marker] = merged
    return file_dictionary, totaal


def chi_quare(merged):
    print(merged)
    count_a = merged.count("a")
    count_b = merged.count("b")
    expected_a = len(merged) / 2
    expected_b = len(merged) / 2

    temp_a = ((count_a - expected_a)**2) / expected_a
    temp_b = ((count_b - expected_b)**2) / expected_b

    outcome = temp_a + temp_b
    if outcome <= 3.84:
        return True
    else:
        return False

def vergelijkingen (file_dictionary):
    data_dict = {}
    for marker1 in range(len(file_dictionary.keys())):
        eerste_marker_list = list(file_dictionary.keys())
        for marker2 in range(marker1+1, len(file_dictionary)):
            tweede_marker = eerste_marker_list[marker2]
            aantal = 0
            for a in range(len(file_dictionary[eerste_marker_list[marker1]])):
                eerste_marker = eerste_marker_list[marker1]
                if file_dictionary[eerste_marker][a] == "-" or file_dictionary[tweede_marker][a] == "-":
                    continue
                elif file_dictionary[eerste_marker][a] != file_dictionary[tweede_marker][a]:
                    aantal += 1
                key = str(eerste_marker) + "/" + str(tweede_marker)
            data_dict[key] = aantal
    return data_dict


def factoren(data_dict, totaal):
    score_dict = {}
    for markers, counts in data_dict.items():
        score_dict[markers] = (counts/totaal)*100
    return(score_dict)


def distance(score_dict):
    afstandlijst = []
    score_list = sorted(score_dict.items(), key=lambda
            item: item[1])
    max_marker = score_list[0][0].split("/")[0]
    afstandlijst.append(("GROUP"+"/"+max_marker, 1))
    afstandlijst.append((max_marker+"/"+max_marker, 0))
    for i in range(len(score_list)):
        if max_marker in score_list[i][0]:
            afstandlijst.append(score_list[i])
        #for j in range(len(afstandlijst)):
         #       markers = afstandlijst[j][0].split(",")[0]
          #      marker_split = markers.split("-")
           #     if max_marker == marker_split[0]:
            #        afstandlijst_final.append((marker_split[1], score_list[i][1]))
             #   elif max_marker == marker_split[1]:
              #      afstandlijst_final.append((marker_split[1], score_list[i][0]))
    print(len(afstandlijst))
    return afstandlijst, max_marker


def write_csv(afstandlijst, max_marker):
    markers_lijst = []
    for j in range(len(afstandlijst)):
        markers = afstandlijst[j][0].split(",")[0]
        marker_split = markers.split("/")
        if max_marker == marker_split[0]:
            markers_lijst.append(marker_split[1])
        else:
            markers_lijst.append(marker_split[0])
    print(afstandlijst)
    with open('afstandlijst.mct', 'w') as output_file:
        for i in range(len(markers_lijst)):
            output_file.write(str(markers_lijst[i])+"\t")
            output_file.write(str(afstandlijst[i][1]))
            output_file.write("\n")


def main():
    bestand = "CvixLer-MarkerSubset-LG1.txt"
    file_dictionary, totaal = read_file(bestand)
    data_dict = vergelijkingen(file_dictionary)
    score_dict = factoren(data_dict, totaal)
    afstandlijst, max_marker = distance(score_dict)
    write_csv(afstandlijst, max_marker)


main()
