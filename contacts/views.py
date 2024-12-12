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
    user_active = authenticate(username=username, password=password)
    if user_active is not None and user_active.is_staff:
      login(request,user_active)
      return redirect('profile')

    messages.error(request, f'hello {username}, check your username and password')
    return render(request, 'account/login.html')
  else:
    messages.error(request, 'invalid username or password')
    return render(request, 'account/login.html')


def login_view(request):
    return render(request, 'account/login.html')

#Admin dashboard 
@login_required
def profile_view(request):
  user_active = request.user
  context={
    'username': user_active.username,
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
  user_active = request.user
  context={
    'username': user_active.username,
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

  user_active = request.user
  context ={
    'username': user_active.username,
    'contact': contact,
  }
  return render(request,'contacts/contact_edit.html',context)


# delete contact
@login_required
def delete_contact_view(request,contact_id):
  contact = get_object_or_404(Contact, id=contact_id)
  if request.method == 'POST':
    
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('all_contacts')

  user_active = request.user
  context ={
    'username': user_active.username,
    'contact': contact,
  }
  return render(request, 'contacts/delete_contact.html', context)

# new contact
@login_required
def new_contact_view(request):
  users = User.objects.all()
  if request.method == 'POST':
    user_id = request.POST.get('user')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    contact_type = request.POST.get('contact_type')
    contact = Contact(user_id=user_id,name=name,email=email,phone=phone,address=address,contact_type=contact_type)
    contact.save()
    messages.success(request, f'Contact for {contact.name} was created successfully')
    return redirect('all_contacts')
  user_active = request.user
  context ={
    'username': user_active.username,
    'users': users,
  }
  return render(request, 'contacts/new_contact.html',context)
  
  