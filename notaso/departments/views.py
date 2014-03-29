from django.shortcuts import render, get_object_or_404

from universities.models import University
from professors.models import Professor
from comments.models import Comment
from .models import Department


def department_view(request, slug, department_slug):
    uni = get_object_or_404(University, slug=slug)
    department = get_object_or_404(Department, slug=department_slug)
    professors = Professor.objects.filter(
        university=uni,
        department=department).order_by('score')
    data = {
        'university': uni,
        'department': department,
        'grade': department.get_grade(uni),
        'professors': Professor.objects.filter(
            university=uni,
            department=department).order_by('first_name'),
        'hi_professors': professors.reverse()[:5],
        'low_professors': professors[:5],
        'recent_comments': Comment.objects.filter(
            professor__in=Professor.objects.filter(
                university=uni,
                department=department)).exclude(
        body__exact='').order_by('-created_at')[:5]

    }
    return render(request, 'department.html', data)