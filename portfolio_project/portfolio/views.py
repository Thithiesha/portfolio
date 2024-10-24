from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Education, Project, Skill, Coursework, WorkExperience

def portfolio_view(request):
    education = Education.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    coursework = Coursework.objects.all()
    work_experience = WorkExperience.objects.all()
    
    # Assuming you want to set your GPA here, you can hardcode it or fetch it from elsewhere
    current_gpa = 4.00  # Replace with your actual GPA

    return render(request, 'portfolio/portfolio.html', {
        'education': education,
        'projects': projects,
        'skills': skills,
        'coursework': coursework,
        'current_gpa': current_gpa,
        'work_experience': work_experience,
    })

from django.core.mail import send_mail
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Save the contact info in the database (optional)
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send an email
        send_mail(
            'Portfolio Contact: ' + name,
            message,
            email,
            ['your_email@example.com'],
            fail_silently=False,
        )
        return redirect('portfolio')
    return render(request, 'portfolio/contact.html')




