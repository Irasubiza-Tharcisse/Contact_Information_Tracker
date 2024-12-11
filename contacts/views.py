from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact
# Create your views here.

def login_F(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_staff:
      login(request,user)
      return redirect('profile')
    return render(request, 'account/login.html')
  else:
    return render(request, 'account/login.html')
def login_view(request):
    return render(request, 'account/login.html')

#Admin dashboard 
@login_required
def profile_view(request):
  user = request.user
  context={
    'username': user.username,
  }
  return render(request, 'contacts/profile.html',context)



#logout
def logout_view(request):
  logout(request)
  return redirect('login_page')


# all contacts
@login_required
def all_contacts_view(request):
  contacts = Contact.objects.all()
  user = request.user
  context={
    'username': user.username,
    'contacts': contacts,
  }
  return render(request, 'contacts/all_contacts.html',context)

# edit contact
@login_required
def contact_edit_view(request,contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  if request.method == 'POST':
    contact.name = request.POST.get('name')
    contact.email = request.POST.get('email')
    contact.phone = request.POST.get('phone')
    contact.address = request.POST.get('address')
    contact.contact_type = request.POST.get('contact_type')
    contact.save()
    messages.success(request, f'Contact for {contact.name} was updated successfully')
    return redirect('all_contacts')
  return render(request,'contacts/contact_edit.html',{'contact':contact})


# delete contact
@login_required
def delete_contact_view(request,contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  if request.method == 'POST':
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('all_contacts')
  return render(request, 'contacts/delete_contact.html', {'contact': contact})
  