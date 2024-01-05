from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host='Abhijnans-MacBook-Pro.local',
    user='root',
    password='189@2003ihba',
    database='temp_class2'
)

# Fetch data from the database
query = "SELECT * FROM `CSE A-3`"
df = pd.read_sql_query(query, db_connection)

# Define the route for the webpage
@app.route('/')
def index():
    # Perform data analysis and create the pie chart
    attendance_status_labels = ['Low Attendance', 'Moderate Attendance', 'High Attendance']
    attendance_status_bins = [0, 75, 90, 100]
    attendance_status_counts = pd.cut(df['ATTENDANCE PERCENTAGE'], bins=attendance_status_bins, labels=attendance_status_labels).value_counts()

    # Create pie chart using Plotly Express
    pie_chart_attendance_status = px.pie(
        names=attendance_status_counts.index,
        values=attendance_status_counts.values,
        title='Pie Chart for Class Attendance Status'
    )

    # Save the plot as HTML
    plot_html = pie_chart_attendance_status.to_html(full_html=False)

    # Render the HTML template with the plot
    return render_template('index.html', plot_html=plot_html)

if __name__ == '__main__':
    app.run(debug=True)
