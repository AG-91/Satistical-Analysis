import numpy as np


def csv_reader(file_name):
    # opening the file with correct encoding in r mode
    with open(file_name, mode='r', encoding="utf-8-sig") as csv_file:
        res = []
        for sub in csv_file:
            res.append(sub.replace("\n", "").replace('"', ""))
        lines = []
        for line in res:
            # splitting the values after each comma
            line = line.split(',')
            # appending the lines to the output list
            lines.append(line)

    # returning parsed csv file data as a list of lists
    return lines


def stats(parsed_data):
    arr = np.array(parsed_data)
    vector = np.vectorize(np.float)

    # claculating mean, min, max, and standard deviation
    arr_mean = np.mean(vector(arr[0:, 1:][1:]), axis=0)
    arr_min = np.min(vector(arr[0:, 1:][1:]), axis=0)
    arr_max = np.max(vector(arr[0:, 1:][1:]), axis=0)
    arr_std = np.std(vector(arr[0:, 1:][1:]), axis=0)

    # printing out the result statistics in a readable fashion
    print(f"Header:                      {arr[0, 1:]}\n"
          f"Mean:                        {arr_mean}\n"
          f"Minimum:                     {arr_min}\n"
          f"Maximum:                     {arr_max}\n"
          f"Standard Deviation:          {arr_std}\n")

    return arr_mean, arr_std, arr_max, arr_min


if __name__ == '__main__':
    parsed_csv = csv_reader('weather-data/outside-temperature-1617.csv')
    stats(parsed_csv)
