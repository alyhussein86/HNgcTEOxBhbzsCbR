import os
import csv
import collections


def main():
    # open current file with Read-only mode
    file_name = open("ACME-HappinessSurvey2020.csv", "r")
    # read content
    reader = csv.DictReader(file_name)
    # input to list of dictionary
    mydict_list = list(reader)

    # for row in mydict.count:
    #     print(row)
    for dicts in mydict_list:
        for keys in dicts:
            dicts[keys] = int(dicts[keys])

    for dicts in mydict_list:
        for keys in dicts:
            # calculate average rating for each customer and satisfaction percentage
            rating_average = (dicts["X1"] + dicts["X2"] + dicts["X3"] +
                              dicts["X4"] + dicts["X5"] + dicts["X6"])/6
            score = rating_average/5 * 100
            # Print output on screen
            if (dicts["Y"] == 0):  # if Y = 0 => customer is unhappy
                print("Customer is unhappy, ",
                      "with satisfaction rating of:", round(score), "%")
            elif (dicts["Y"] == 1):  # if Y = 1 => customer is unhappy
                print("Customer is happy, ",
                      "with satisfaction rating of:", round(score), "%")

    # print("Total no. of rows: %d" % (reader.line_num))


if __name__ == "__main__":
    main()
