Description: The clean.py python scripts reads class.txt file and formats and cleans the data.
             It corrects the incorrect/ mis-spelled words in the file and
             removes the duplicate courses and finally writes the corrected data in cleaned.txt file.

             Query.py python script reads the cleaned.txt file and executes the required queries on data
             and outputs the result of the query.


Execution Steps:
1. Place the class.txt file in same folder as script.
2. Run the clean.py script. It will generate cleaned.txt file.
   NOTE: The execution of clean.py takes some time. The progress of the script can be checked on terminal.
         As long as the script is running and performing its tasks, dots will be printed on screen.
         This indicates that script is running and cleaning the file.
3. Once the execution of clean.py is completed, execute query.py to get the final results.


List of Files:
1. clean.py
2. query.py
3. cleaned.txt
4. README_1.txt


Required packages:
1. nltk
2. enchant


Data cleaning:
- 'Intro' is converted to 'Introduction'
- '&' is converted to 'and'
- 'Temporalitiez' is converted to 'Temporalities'
- The data cleaning function gets the suggestion form the enchant library. It then computes
  edit distance of every suggestion from the input word. It then returns the word with
  minimum edit distance. If there are multiple suggestions with edit distance equal to minimum
  edit distance, it chooses the first one with same length.


Issues:
- 'Biopolitics' in converted to 'Geopolitics'
- Some of the words that are not in enchant english dictionary 'en_US' are used as
  original words without any corrections.


Contributors:
1. Krutarth Joshi
2. Ayush Katariya
3. Kushagra Thapar
4. Dhaval Doshi
