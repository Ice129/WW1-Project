from datastructures import Serviceman

def process_csv(csv: dict):
    for entry in csv:
        iterator = 1
        for info in entry:
            if iterator != 1:
                if iterator == 2:
                    print(f"Surname: {entry[info]}")
            iterator+=1