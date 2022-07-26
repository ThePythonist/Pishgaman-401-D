info = [
    {"name": "Parsa", "Birth": 1387, "Education": "Middle School"},
    {"name": "Amirali", "Birth": 1384, "Education": "High School"},
    {"name": "Ali", "Birth": 1373, "Education": "Bachelor"},
    {"name": "Ramin", "Birth": 1368, "Education": "PhD"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Table of information</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Birth</th>
    <th>Education</th>
  </tr>
"""

for person in info:
    html += f"""
    <tr>
    <td>{person['name']}</td>
    <td>{person['Birth']}</td>
    <td>{person['Education']}</td>
    </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Information.html","w").write(html)
print("Done")
