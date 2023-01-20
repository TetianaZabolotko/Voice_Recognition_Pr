import json


file = "gm2021q4-selected.json"
def import_fields(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)

        # handle exceptions
        
        for field in data['episodes']['120515582'].keys():
            print(field)

if __name__ == '__main__':
    print('Fields :\n')
    import_fields("gm2021q4-selected.json")