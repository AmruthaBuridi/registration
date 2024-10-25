

from django.shortcuts import render, redirect
from Application1.models import Student1
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def sample3(request):
    return render(request, "application1/s3.html")

def sample1(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_number=request.POST['phone_number']
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        
        # Check if passwords match
        if password != conform_password:
            return HttpResponse("Passwords do not match")
        
        # Sending email

        
        try:
            subject = "Workshop Registration Confirmation"
            message = f"""
Dear {username},<br><br>

Thank you for registering for the <strong>Data Science with R</strong> workshop, scheduled on <strong>1st November 2024</strong>. We are excited to have you join us!<br><br>

Here are the details of the workshop:<br>
- <strong>Date:</strong> 1st November 2024<br>
- <strong>Time:</strong> 10:00 AM to 12:00 PM<br>
- <strong>Mode:</strong> Online<br><br>

If you have any questions or need further information, feel free to contact us at <a href="mailto:amruthaburidi321@gmail.com">amruthaburidi321@gmail.com</a>.<br><br>

We look forward to your participation!<br><br>

Best regards,<br>
<strong>Amrutha Buridi</strong>
"""
            send_mail(
                subject,
                "",
                settings.EMAIL_HOST_USER,  # Corrected here
                [email],
                fail_silently=False,
                html_message=message
            )
        except Exception as e:
            return HttpResponse(f"Email sending failed: {str(e)}")
        
        # Saving the employee record
        try:
            student = Student1.objects.create(
                username=username,
                email=email,
                phone_number=phone_number,
                password=password,  # Assuming password is stored as plain text (not recommended)
                conform_password=conform_password  # Consider storing hashed password instead
            )
            return HttpResponse(f"Student {username} registered successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    
    return render(request, 'Application1/s1.html')

# Create your views here.
