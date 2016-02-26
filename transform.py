# Author: Ashwin Bansod
# Description : This file reads the raw html file,
#               extracts the required data from it and then
#               writes the formatted required data into output file.

from bs4 import BeautifulSoup

# Opening the html file using Beautiful soup
soup = BeautifulSoup(open("superbowl.html", encoding="utf-8"), 'html.parser')

# Extracting the required data from htm file.
cleaned_html_file = ""
for row in soup.find_all("tr")[+1:]:
    for td in row.find_all("td"):
        cleaned_html_file += td.get_text()


# Read cleaned HTML file using BeautifulSoup
soup = BeautifulSoup(cleaned_html_file, 'html.parser', from_encoding="utf-8")

# Open output file "result.csv" in write mode
out = open('result.csv', 'w')

# We have to skip first table and only print values of 2nd table
# So maintain tablecount and skip all the tables other than table 2
tablecount = 0
rowcounter = 0
for table in soup.find_all("table", attrs={"class": "wikitable sortable"}):
    tablecount += 1

    # Skip all tables other than table 2
    if tablecount != 2:
        continue

    # For every row in the the table.
    # Print the values of required fields in result.csv
    for row in table.find_all("tr"):
        # Check for headers and write it in result.csv
        dataset = []
        for col in row.find_all("th"):
            header = col.get_text()
            dataset.append(header)

        if len(dataset) > 0:
            header = ""
            for val in dataset:
                # Skip the tables 'City,Attendance,Ref' as it is not part of output csv
                if val in "City,Attendance,Ref":
                    continue
                elif val == "Game":    # Change the header as per requirement
                    header += str("Game number")
                elif val == "Date":    # Instead of date only year is expected in output csv
                    header += str("Year")
                else:
                    header += str(val)

                header += str(",")
            header = header[:-1]
            out.write(str(header))
            del header

            # Reduce row counter as header is excluded from row counts
            rowcounter -= 1

        del dataset

        # Iterate through all the other rows of table
        # and get the respective value from <td> tag
        dataset = []
        Colcount = 1
        for col in row.find_all("td"):
            # Skip the column values corresponding to 'City', 'Attendance', 'Ref' as it is not part of output csv
            # These columns are expressed as column numbers
            if Colcount in range(7, 10):
                continue

            # Get the value of each column in expected format.
            if Colcount == 1:                                           # Game Number
                DataVal = (col.get_text()).split("!")[-1].strip()
            elif Colcount == 2:                                         # Year
                DataVal = (col.get_text()).split(",")[-1].strip()
            elif Colcount == 3:                                         # Winning Team
                DataVal = (col.get_text()).split("!")[0].strip()
            elif Colcount == 4:                                         # score
                DataVal = str((col.get_text()).split("!")[-1].strip())
            elif Colcount == 5:                                         # Loosing Team
                DataVal = (col.get_text()).split("!")[0].strip()
            elif Colcount == 6:                                         # Venue
                DataVal = (col.get_text()).split("!")[0].strip()
            else:
                DataVal = col.get_text()

            dataset.append(DataVal)
            Colcount += 1

        DataVal = ""
        for val in dataset:
            DataVal += str(val)
            DataVal += str(",")

        DataVal = DataVal[:-1]
        out.write(DataVal)
        out.write("\n")

        # Only first fifty rows of table are to be printed.
        rowcounter += 1
        if rowcounter == 50 :
            break
        del dataset
        del DataVal
