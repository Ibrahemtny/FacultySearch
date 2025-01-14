

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

url = 'https://mscs.uic.edu/people/faculty/'
response = requests.get(url)

facultyList = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    facultyDataList = soup.find_all('article', class_='profile-teaser')

    for facultyData in facultyDataList:
        nameElem = facultyData.find('span', class_='n')
        titleElem = facultyData.find('span', class_='t')
        deptElem = facultyData.find('div', class_='d')
        contactElem = facultyData.find('div', class_='c')

        if contactElem:
            phoneElem = contactElem.find('span', class_='p')
            phone = phoneElem.text.strip() if phoneElem else "N/A"

            emailElem = contactElem.find('span', class_='e').find('a') if contactElem.find('span', class_='e') else None
            email = emailElem.text.strip() if emailElem else "N/A"

            facultyList.append({
                'N': nameElem.find('a').text.strip() if nameElem else "N/A",
                'T': titleElem.text.strip() if titleElem else "N/A",
                'D': deptElem.text.strip() if deptElem else "N/A",
                'P': phone,
                'E': email
            })

    print("Web scraping completed.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        st = request.form['search_type']

        if st == 'faculty':
            fn = request.form['faculty_name']
            fi = fFacultyInfo(fn)
            return render_template('result.html', faculty_info=fi, search_type='faculty')

        elif st == 'class':
            cn = request.form['class_name']
            fl = fFacultyByClass(cn)
            return render_template('result.html', faculty_list=fl, search_type='class')

    return redirect(url_for('home'))

def fFacultyInfo(name):
    for faculty in facultyList:
        if faculty['N'].lower() == name.lower():
            return {'E': faculty['E'], 'O': gOfficeHours(faculty['N'])}
    return None

def fFacultyByClass(cn):
    fl = []
    for faculty in facultyList:
        if hMultipleSections(faculty['N'], cn):
            fl.append(faculty['N'])
    return fl

def hMultipleSections(name, cn):
    return len(name) % 2 == 0

def gOfficeHours(name):
    return 'Monday 2-4 PM'

if __name__ == '__main__':
    app.run(debug=True, port=1000)
