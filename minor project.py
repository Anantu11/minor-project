pip install django
django-admin startproject olympics_project
cd olympics_project
python manage.py startapp analysis
INSTALLED_APPS = [
    ...
    'analysis',
]
from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    medals = models.IntegerField()

    def __str__(self):
        return self.name
python manage.py makemigrations
python manage.py migrate
from django.shortcuts import render
from .models import Athlete

def home(request):
    athletes = Athlete.objects.all()
    return render(request, 'analysis/home.html', {'athletes': athletes})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analysis.urls')),
]
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Olympic Data Analysis</title>
    <link rel="stylesheet" href="{% static 'analysis/style.css' %}">
</head>
<body>
    <h1>Olympic Data Analysis</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Country</th>
            <th>Sport</th>
            <th>Medals</th>
        </tr>
        {% for athlete in athletes %}
        <tr>
            <td>{{ athlete.name }}</td>
            <td>{{ athlete.country }}</td>
            <td>{{ athlete.sport }}</td>
            <td>{{ athlete.medals }}</td>
        </tr>
        {% endfor %}
    </table>
    <script src="{% static 'analysis/script.js' %}"></script>
</body>
</html>
STATIC_URL = '/static/'
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    padding: 10px;
    border: 1px solid #ddd;
}document.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('table');
    const headers = table.querySelectorAll('th');
    const rows = table.querySelectorAll('tr:not(:first-child)');

    headers.forEach((header, index) => {
        header.addEventListener('click', () => {
            const sortedRows = Array.from(rows).sort((rowA, rowB) => {
                const cellA = rowA.querySelectorAll('td')[index].innerText;
                const cellB = rowB.querySelectorAll('td')[index].innerText;
                return cellA.localeCompare(cellB);
            });

            sortedRows.forEach(row => table.appendChild(row));
        });
    });
});
'DOMContentLoaded', () => {
    const table = document.querySelector('table');
    const headers = table.querySelectorAll('th');
    const rows = table.querySelectorAll('tr:not(:first-child)');

    headers.forEach((header, index) => {
        header.addEventListener('click', () => {
            const sortedRows = Array.from(rows).sort((rowA, rowB) => {
                const cellA = rowA.querySelectorAll('td')[index].innerText;
                const cellB = rowB.querySelectorAll('td')[index].innerText;
                return cellA.localeCompare(cellB);
            });

            sortedRows.forEach(row => table.appendChild(row));
        });
    });
});
git init

