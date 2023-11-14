def summarise_data(file, col_index):
    try:
        with open(file, "r", encoding="utf-8") as file_object:
            # Attempt to open the file
            data = []
            data_max, data_min, data_sum, count, avg = 0, 0, 0, 0, 0
            # Initialise variables
            for line in file_object:  # Read each line in the file
                data.append([])
                line = line.strip()
                line = line.split(",")
                if not isinstance(col_index, int) or len(line) < col_index:
                    # Check if col_index is valid
                    return "IndexError - col_index out of range."
                data[count].append(int(line[col_index]))
                for number in data[count]:  # Assign values to variables
                    if number > data_max:
                        data_max = number
                    if number < data_min or data_min == 0:
                        # data_min == 0 to avoid assigning 0 to data_min
                        data_min = number
                    data_sum += number
                count += 1
            avg = round(data_sum/count, 2)  # Calculate average
            return [data_max, data_min, data_sum, count, avg]
    except (FileNotFoundError, ValueError):  # Catch errors
        return "ValueError - invalid value in data."


if __name__ == "__main__":
    #  test valid arguments
    print(summarise_data("data.txt", 1))

    #  test out of range col_index, data.txt only has 3 columns
    print(summarise_data("data.txt", 5))

    # test invalid col_index, col_index should be integer
    print(summarise_data("data.txt", "a"))

    # test invalid value in file, contains a "abc" in the second column
    print(summarise_data("data2.txt", 1))
