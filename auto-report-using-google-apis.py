import csv

# Extract data from csv file
timing_data = []
with open('filename.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

column_chart_data = [["Test Name", "Diff from Avg"]]
table_data = [["Test Name", "Run Time (s)"]]

for row in timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_runtime = float(row[1])
    avg_run_time = float(row[2])       
    diff_from_avg = avg_run_time - current_runtime
    column_chart_data.append([test_name, diff_from_avg])
    table_data.append([test_name, current_runtime])

print (column_chart_data)
print (table_data)

# Using Google Chart API
from string import Template

html_string = Template("""<html><head><script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
      var data = google.visualization.arrayToDataTable([
       #labels, $data
      ],
      false); 
            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
    }
  }
</script>
</head><body>
<div id="chart_div" style="width:800; height:600"></div>
</body></html>""")

chart_data_str = ''
for row in column_chart_data[1:]:
    chart_data_str += '%s, \n'%row

completed_html = html_string.substitute(labels=column_chart_data[0], data=chart_data_str)

with open('column_chart.html', 'w') as f:
    f.write(completed_html)


# Create Column Chart
data_list = []
with open('TestAnalysisData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        data_list.append(row)

chart_data = [data_list[0]]
for row in data_list[1:]:
    num_asserts = int(row[1])
    num_failed_asserts = int(row[2])
    chart_data.append([row[0], num_asserts, num_failed_asserts])

chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s,\n'%row

completed_html = html_string.substitute(labels=chart_data[0], data=chart_data_str)

with open('Chart.html', 'w') as f:
    f.write(completed_html)


# Google Sheet API 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('ServiceAccountTest').sheet1
# Update data in the sheet
sheet.update_cell(1, 1, "test")
# Get value from the sheet
sheet.row_values(1)
# Get all data
sheet.get_all_values()
my_data = [[1, 2, 3], [4, 5, 6]]
for row_index, row in enumerate(my_data):
    for col_index, value in enumerate(row):
        sheet.update_cell(row_index+1, col_index+1, value)


# Test Report Webpage
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('TestRunData').sheet1

spreadsheet_data = sheet.get_all_values()
run_times = []
for row in spreadsheet_data:
    del row[0]
    del row[1]

    run_times.append(row)

csv_data = []
with open('LatestTestRunData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        csv_data.append(row)

run_date = csv_data[1][2]
spreadsheet_header_row = run_times[0]
spreadsheet_header_row.append(run_date)
del spreadsheet_header_row[0]

for spreadsheet_row, csv_row in zip(run_times[1:], csv_data[1:]):
    new_value = csv_row[1]
    spreadsheet_row.append(new_value)
    del spreadsheet_row[0]

for row_index, row in enumerate(run_times):
    for col_index, cell in enumerate(row):
        sheet.update_cell(row_index+1, col_index+3, cell)

avg_data = sheet.col_values(2)

chart_data = [["Test Name", "Diff From Avg"]]
for avg, current in zip(avg_data[1:],csv_data[1:]):
    diff = float(avg) - float(current[1])
    chart_data.append([current[0],diff])

from string import Template
htmlString = Template("""<html><head><script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
      var data = google.visualization.arrayToDataTable([
       #labels, $data
      ],
      false); 
            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
    }
  }
</script>
</head><body>
<div id="chart_div" style="width:800; height:600"></div>
</body></html>""")


chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s,\n'%row

completedHtml = htmlString.substitute(labels=chart_data[0], data=chart_data_str)

with open('Chart.html', 'w') as f:
    f.write (completedHtml)