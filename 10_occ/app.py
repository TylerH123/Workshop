#teamFakeMoonLanding_huangT_bhuiyanS
#Tyler Huang
#SoftDev1 pd2
#K10: Jinja Tuning
#2019-09-20


from flask import Flask, render_template
import csv, random
app = Flask(__name__)

@app.route("/")
def homePage():
    print("moon landing")
    coll = {"the moon landing was fake", "okay maybe it was real", "but birds definitely aren't real"}
    return render_template(
        'my_foist_template.html',
        foo = "teamFakeMoonLanding",
        collection = coll)

occupations = {} #the dictionary where we will input the values from the csv file
jobClass = [] #list of keys (occupations) from occupations dictionary
percentage = [] #list of values (percentages) from occupations dictionary

with open( "occupations.csv") as csv_file: #opens csv file to read in python
    csv_reader = csv.reader( csv_file, delimiter = ",") #csv reader funtion using "," as the delimiter
    for row in csv_reader: #for loop iterates through each line of the csv file
        occupations[ row[0]] = row[1] #sets the first part of the line as the key and the second part as the value of the key in the dictionary
    del occupations[ "Job Class"] #delete header
    del occupations[ "Total"] #delete footer
    for occupation in occupations: #for loop iterates through each job in the occupations dictionary
        jobClass.append( occupation) #adds the job to the jobClass list
        percentage.append( float( occupations[ occupation])) #adds the percentage to percentage list after casting to float

def randomOccupation():
    return random.choices( jobClass, weights = percentage, k = 1)[0] #returns a random occupation using percentages as weights

@app.route("/occupyflaskt")
def occupationscsvToHTML():
    print("occupations csv to html")
    return render_template(
        'occupations_csv_to_HTML_table.html',
        teamName = "Team Fake Moon Landing",
        teamMembers = "Saad Bhuiyan and Tyler Huang",
        description = "We used Python, Flask, Jinja2, and HTML to take a data set (occupations.csv) and print the data in a table form.",
        randomOccupation = randomOccupation(),
        dictionary = zip(jobClass, percentage) #to be able to loop through two lists using jinja2, we had to zip them together
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
