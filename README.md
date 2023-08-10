# Resume_Categorizer
A machine learning model that automatically categorize resumes based on their domain (e.g., sales, marketing, etc.). A script can be run via the command line to process a batch of resumes and categorize them then output results to both directory structures and a CSV file
<br>
<hr>
<br>
<b>Requirements:</b> <br>
You need to install <br>
•	Python 3.9.12 <br>
•	pickle <br>
•	shutil <br>
•	PyPDF2 <br>
•	Nltk <br>

<br>
<hr>
<br>

<b>How to run Guide:</b>
1.	Download the repository
2.	Open the Script.py file and set your output folder path in the line 70
3.	Open command prompt
4.	Navigate to the downloaded repository folder
5.	Type: python Script.py [ path of your directory / folder where the resumes are ] note: you need to use “ your dir ” (quotation). Also, you need to replace all the back slash with a Forword slash and a Forword slash at the end
6.	Example: python Script.py “D:/Downloads/Resumes/”
7.	After Execution You will find all the categorized resumes inside your output folder and also a CSV file containing filename and category of the resume
