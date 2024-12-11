from django.shortcuts import render
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# view all users
@login_required
def all_users_view(request):
  users = User.objects.all()
  user = request.user
  context={
    'username': user.username,
    'users': users,
  }
  return render(request, 'account/all_users.html',context)


#edit user
@login_required
def edit_user_view(request, user_id):
  user = get_object_or_404(User, id=user_id)
  if request.method == 'POST':
    user.username = request.POST.get('username')
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    user.password = request.POST.get('password')
    user.save()
    messages.success(request, f'Account for {user.username} was updated successfully')
    return redirect('all_users')
  else:
    context={
      'username': user.username,
      'user': user,
    }
    return render(request,'account/confirm_edit.html',context)

def delete_user(request, user_id):
  user = get_object_or_404(User, id=user_id)

  if request.method == 'POST':
      user.delete()
      messages.success(request, 'User deleted successfully!')
      return redirect('all_users')  # Redirect to the user management page

  return render(request, 'account/confirm_delete.html', {'user': user})


