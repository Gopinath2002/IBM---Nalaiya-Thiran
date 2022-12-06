import csv
from flask import Flask, render_template, url_for, request, redirect
from flask import *
from predict import *

app = Flask(__name__)


def branchNameToCode(input_branch):
    index = 0
    branch_code = 'Empty'
    for branch_name in list_Branch_Names:
        if input_branch == branch_name:
            branch_code = list_Branch_Codes[index]
        index += 1
    return branch_code


def collegeNameToCode(input_college):
    index = 0
    college_code = 'Empty'
    for college_name in list_College_Names:
        if input_college == college_name:
            college_code = list_College_Codes[index]
        index += 1
    return college_code


with open('BranchNames.csv', 'r') as file_Branch_Names:
    csv_reader = csv.reader(file_Branch_Names)
    temp_list = list(csv_reader)
    list_Branch_Names = list()
    for i in temp_list:
        list_Branch_Names.append(i[0])

with open('CollegeNames.csv', 'r') as file_College_Names:
    csv_reader = csv.reader(file_College_Names)
    temp_list = list(csv_reader)
    list_College_Names = list()
    for i in temp_list:
        list_College_Names.append(i[0].split(',')[0])


with open('CollegeCodes.csv', 'r') as file_College_Codes:
    csv_reader = csv.reader(file_College_Codes)
    temp_list = list(csv_reader)
    list_College_Codes = list()
    for i in temp_list:
        list_College_Codes.append(i[0])

with open('BranchCodes.csv', 'r') as file_Branch_Codes:
    csv_reader = csv.reader(file_Branch_Codes)
    temp_list = list(csv_reader)
    list_Branch_Codes = list()
    for i in temp_list:
        list_Branch_Codes.append(i[0])

list_Community = ["OC", "BC", "BCM", "MBC", "DNC", "SC", "SCA", "ST"]


@app.route('/', methods=["GET", "POST"])
def predict():
    return render_template("index.html", percent=0, dept=list_Branch_Names, College_name=list_College_Names, College_code=list_College_Codes, dept_code=list_Branch_Codes, com=list_Community, predRank="", predRound="")


@app.route('/result', methods=["GET", "POST"])
def result():
    input_marks = float(request.form.get('CutOff'))
    input_college = request.form.get('Preferred_College')
    input_branch = request.form.get('Preferred_Branch')
    input_community = request.form.get('Community')
    print('Marks: ', input_marks, '\t', type(input_marks))
    print('College: ', input_college, '\t', len(
        input_college), '\t', type(input_college))
    print('Branch: ', input_branch, '\t', len(
        input_branch), '\t', type(input_branch))
    print('Community: ', input_community, '\t', len(
        input_community), '\t', type(input_community))
    branch_code = branchNameToCode(input_branch)
    print('Branch Code:', branch_code, '\t', len(
        branch_code), '\t', type(branch_code))
    college_code = collegeNameToCode(input_college)
    print('College Code:', college_code, '\t', len(
        college_code), '\t', type(college_code))
    input_rank = request.form.get('Rank')
    input_round = request.form.get('Round')

    if (input_rank == ''):
        input_rank = predictRank(input_marks)
        input_round = predictRound(input_rank)
        display_pred_rank = 'Predicted Rank: ' + str(input_rank)
        display_pred_round = 'Predicted Round: ' + str(input_round)

    else:
        input_rank = int(input_rank)
        input_round = int(input_round)
        display_pred_rank = ''
        display_pred_round = ''

    print('Rank: ', input_rank, '\t', type(input_rank))
    print('Round: ', input_round, '\t', type(input_round))
    return render_template("index.html", percent=76, dept=list_Branch_Names, College_name=list_College_Names, College_code=list_College_Codes, dept_code=list_Branch_Codes, com=list_Community, predRank=display_pred_rank, predRound=display_pred_round)


@app.route('/Landing', methods=["GET", "POST"])
def landing():
    return render_template("Landing Page.html")


@app.route('/collegeinfo', methods=["GET", "POST"])
def info():
    return render_template("/college_info/college.html")


if __name__ == '__main__':
    app.run(debug=True)
