string = "combien onf ,12.25 et 13. 20"
if ". " in string.split(",")[1]:
    string = " ".join([string.split(",")[0],string.split(",")[1].replace(". ",".")])
print(string)