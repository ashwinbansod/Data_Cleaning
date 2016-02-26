# Author: Ashwin Bansod
# Description : This file reads the cleaned data file and runs
#               queries on it to get the result.

# Read input file and store value in a dictionary
def ReadAndStoreInputFile():
    # Open the input file to read record.
    fp = open("cleaned.txt", 'r')

    dict = {}
    for row in fp:
        name = row.split('-', 1)[0].strip()
        courses = row.split('-', 1)[1].strip()

        dict[name] = courses

    del fp
    return dict


def Query1(ProfDict):
    print("Query 1:")
    CourseCount = 0
    Courseset = set()

    for row in ProfDict:
        for course in ProfDict[row].split("|"):
            Courseset.add(course)

    print("Total number of courses : [" +  str(len(Courseset)) + "]\n")


def Query2(ProfDict, name) :
    print("Query 2:")
    courseList = ProfDict[name].split("|")

    print(" Number of Courses : " + str(len(courseList)))
    print(" , ".join(courseList))
    print()


def Query3(ProfDict):
    print("Query 3:")
    Profwith5Courses = {}
    JaccardDistance = []

    i = 0
    for prof in ProfDict:
        if len(ProfDict[prof].split("|")) >= 5 :
            Profwith5Courses[i] = (prof, ProfDict[prof].split("|"))
            i += 1

    courseSet = set()
    maxJD = 0
    for i in range(0,len(Profwith5Courses)):
        # Add the courses of first professor in courseSet
        courseSet.clear()
        for course in Profwith5Courses[i][1] :
            courseSet.add(course)

        for j in range(i+1, len(Profwith5Courses)):
            commonCourse = len(courseSet.intersection(Profwith5Courses[j][1]))
            totalCourse = len(Profwith5Courses[i][1]) + len(Profwith5Courses[j][1]) - commonCourse
            jd = commonCourse/totalCourse
            t = (jd, commonCourse, totalCourse, Profwith5Courses[i][0], Profwith5Courses[j][0])
            JaccardDistance.append(t)

            if maxJD < jd :
                maxJD = jd

    for tup in JaccardDistance:
        if maxJD == tup[0]:
            print(tup[3] + " , " + tup[4] + "  --> Jaccard Distance [" + str(tup[0]) + "]")


def main():
    ProfDict = {}
    ProfDict = ReadAndStoreInputFile()

    # Run Query 1 : to calculate total number of distinct courses
    Query1(ProfDict)

    # Run Query 2 : List all courses of Professor Theys
    ProfName = "Theys"
    Query2(ProfDict, ProfName)

    # Run Query 3 :
    Query3(ProfDict)

if __name__ == "__main__":
    main()

