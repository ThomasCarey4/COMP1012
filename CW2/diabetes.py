"""
Please write your name
@author: Thomas Carey

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv
htmlTableTemplate = """
<style>
    table {{
        border-collapse: collapse;
    }}

    th, td {{
        border: 1px solid black;
        padding: 2px;
    }}

    tr:nth-child(odd) {{
        background-color: #8b8484;
    }}
</style>

<table>
    <thead>
        <tr>
            <th rowspan="3" style="background-color: white;">Attributes</th>
            <th colspan="4" style="background-color: white;">Class</th>
        </tr>
        <tr>
            <th colspan="2"
            style="text-align: center;
            font-weight: bold;
            background-color: white;">Positive</th>
            <th colspan="2"
            style="text-align: center;
            font-weight: bold;
            background-color: white;">Negative</th>
        </tr>
        <tr style="text-align: center; font-weight: bold;
        background-color: white;">
            <th>Yes</th>
            <th>No</th>
            <th>Yes</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody style="text-align: left; font-weight: normal;">
        {0}
    </tbody>
</table>
"""


class Diabetes:
    def __init__(self, filepath) -> None:
        self.header = []
        self.data = []
        try:  # try to open the file
            with open(filepath) as csvfile:
                reader = csv.reader(csvfile)
                self.header = next(reader)  # read the headers
                self.data = list(reader)  # read the data
        except FileNotFoundError:
            raise Exception("File not found")

    def get_dimension(self) -> list:
        return [len(self.data), len(self.data[0])]  # return the dimension

    def web_summary(self, filepath: str) -> None:
        # 0 == no, 1 == yes
        newData = [[], []]
        htmlRows = ""
        for header in self.header:  # Initialise the newData list
            newData[0].append([0, 0])
            newData[1].append([0, 0])
        for row in self.data:  # Count the number of yes/no for each attribute
            colNumber = 0
            pos = 0
            if row[-1] == "Positive":  # If the row class is positive
                pos = 1
            for item in row:
                if item == "No":
                    newData[pos][colNumber][0] += 1
                else:
                    newData[pos][colNumber][1] += 1
                colNumber += 1
        for i in range(2, len(newData[0]) - 1):  # Add rows to the html table
            htmlRows += "<tr>"
            htmlRows += "<td>" + str(self.header[i]) + "</td>"
            htmlRows += ("<td style=\"text-align: center;\">"
                         + str(newData[1][i][1]) + "</td>")
            htmlRows += ("<td style=\"text-align: center;\">"
                         + str(newData[1][i][0]) + "</td>")
            htmlRows += ("<td style=\"text-align: center;\">"
                         + str(newData[0][i][1]) + "</td>")
            htmlRows += ("<td style=\"text-align: center;\">"
                         + str(newData[0][i][0]) + "</td>")
            htmlRows += "</tr>"
        htmlOut = htmlTableTemplate.format(htmlRows)  # Add the html rows
        with open(filepath, "w") as htmlFile:
            htmlFile.write(htmlOut)  # Write the html to the file

    def count_instances(self, criteria) -> int:
        """
        criteria is a dictionary of the form {headerName: value,
                                              headerName2: value2}
            - You DO NOT have to include every header in the dictionary
        Example: count_instances({"Gender": "Female", "weakness": "Yes"})
        This will return the number of instances that satisfy the criteria
        """
        logicalList = [0 for row in self.header]  # Initialise the logical list
        instances = 0
        for key in criteria:
            if key in self.header:  # If the key is in the header
                logicalList[self.header.index(key)] = criteria[key]
        for row in self.data:
            if all(item1 == item2 for item1, item2  # Kind of a logical AND
                    in zip(logicalList, row) if item1 != 0):
                instances += 1
        return instances


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    print(d2.count_instances({"Gender": "Female", "weakness": "Yes"}))
