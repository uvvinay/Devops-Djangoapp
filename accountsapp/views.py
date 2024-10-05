from django.shortcuts import render,redirect
from .models import Customer,Products,Orders
from .forms import CreateUserForm,customeruserform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib import staticfiles
from django.contrib.auth.decorators import login_required
from .decerator import unathenicated_user

# Create your views here.

@login_required(login_url='login')
#@allowed_users(allowed_role=[])
def home(request):
    customers= Customer.objects.all()
    products=Products.objects.all()
    orders=Orders.objects.all()

    Total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    out_for_delivery = orders.filter(status='OutforDelivered').count()
    contex={
        'customers':customers,
        'products':products,
        'orders':orders,
        'Total_orders':Total_orders,
        'pending_orders':pending_orders,
        'delivered_orders':delivered_orders,
        'out_for_delivery':out_for_delivery
    }
    return render(request, 'accounts/dashboard.html',contex)

@login_required(login_url='login')
#@allowed_users(allowed_role=[])
def PRODUCTS(request):
    product=Products.objects.all()
    contex = {
        'product':product
    }
    return render(request, 'accounts/products.html',contex)


@login_required(login_url='login')
#@allowed_users(allowed_role=[])
def ORDERS(request):
    orders=Orders.objects.all()
    contex = {
        'orders':orders
    }

    return render(request, 'accounts/orders.html',contex)

@login_required(login_url='login')
#@allowed_users(allowed_role=['STAFF'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders=customer.orders_set.all()

    Total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    out_for_delivery = orders.filter(status='OutforDelivered').count()
    contex = {
        'customer': customer,
        'orders': orders,
        'Total_orders': Total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'out_for_delivery': out_for_delivery
    }
    return render(request, 'accounts/customer.html', contex)


#@unathenicated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        contex = {'form': form}
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("login")

        return render(request, 'accounts/register.html', contex)

def LOGIN(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "successfully login")
                return redirect('home')
            else:
                messages.warning(request, "invalid user name or password")
        return render(request, "accounts/login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def userview(request):
    user=request.user
    form=customeruserform(instance=user)
    return render(request, 'accounts/user.html',{'form':form})
