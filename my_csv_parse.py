import csv

def filter_data_by_gender(gender) : 
    gender = gender.capitalize()
    filename = "imdb-movie-data.csv"
    result = []

    with open(filename) as csvfile:
        csv_content = csv.reader(csvfile)

        for line in csv_content:
            all_gender = line[2].split(',')
            if gender in all_gender :
                result.append(line)
        return result