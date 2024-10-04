from django.http.response import HttpResponse
from django.shortcuts import redirect

def unathenicated_user(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.authenicated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
#def allowed_users(allowed_role=[]):
#    def decorator(view_func):
#        def wrapper_func(request, *args, **kwargs):
#            group = None
#            if request.user.group.exits():
#                group = request.user.group.all()[0].name
#            if group in allowed_role:
#                return view_func
#            else:
#                return HttpResponse('u r not authorised to view this page')
#        return wrapper_func
#    return decorator
def admin_only(func_view):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():

           group =request.user.groups.all()[0].name

        if group == 'user':
            return redirect('user-page')
        if group=='admin':
            return func_view(request, *args, **kwargs)
    return wrapper_func