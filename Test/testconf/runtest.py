import os
from utils.uitlsfunction import readdate, readAndUpdateCounter, keepreports

reportName = f"{readdate()}_{readAndUpdateCounter()}"

# For running testCases
# command = f"pytest -s --alluredir=ReportAllure/{reportName} --html=ReportHtml/report_{reportName}.html --self-contained-html testcase"
command = f"pytest -s testcase"
os.system(command)

#  Send email
# sender = ''
# password = ''
# receivers = ''
# sendemail(sender, password, receivers, reportName)

# number of allure & html reports to keep
# number = 2
# keepreports(number)

# For generating report
# command = f"allure serve ReportAllure/{reportFolderName}"
# os.system(command)
