from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account.models import User, Supplier, Category, Color, Design, Product, SalesOrder, SalesOrderDetail, Cart, \
    CartDetail, Stock
from time import gmtime, strftime


# Create your views here.
def checkSessionVars(request):
    if 'id' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 0:
            return True
    else:
        return False


##################################################################################################
##################################################################################################
###################################           Index                #########################################
##################################################################################################
##################################################################################################

def index(request):
    if checkSessionVars(request):
        products = Product.objects.all()
        return render(request, 'userpanel/index.html', {'products': products})
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           Contact                #########################################
##################################################################################################
##################################################################################################
def contact(request):
    if checkSessionVars(request):
        return render(request, 'userpanel/contact.html')
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           About                #########################################
##################################################################################################
##################################################################################################
def about(request):
    if checkSessionVars(request):
        return render(request, 'userpanel/about.html')
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           product details                #########################################
##################################################################################################
##################################################################################################
def product_detail(request):
    if checkSessionVars(request):
        product = Product.objects.filter(id=request.POST.get('id')).get()
        stock = Stock.objects.filter(product_id=request.POST.get('id')).get()
        return render(request, 'userpanel/product-detail.html', {'product': product, 'stock': stock})
    return HttpResponseRedirect(reverse('login'))


def product_add_to_cart(request):
    if checkSessionVars(request):
        id = request.POST.get('id')
        quantity = int(request.POST.get('quantity'))
        tProduct = Product.objects.get(id=id)
        total = tProduct.price * quantity
        try:
            cart = Cart.objects.get(user_id=User.objects.get(id=request.session['id']))
            if cart.status == False:
                Cart.objects.filter(user_id=User.objects.get(id=request.session['id'])).update(status=True)
                result = CartDetail.objects.filter(
                    cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])),
                    product_id=Product.objects.get(id=id)).update(
                    quantity=quantity,
                    date_add=strftime("%d-%m-%y", gmtime()), total=total)
                if result == 0:
                    CartDetail(quantity=quantity, date_add=strftime("%d-%m-%y", gmtime()),
                               product_id=Product.objects.get(id=id),
                               cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])),
                               total=total).save()
            elif cart.status == True:
                result = CartDetail.objects.filter(
                    cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])),
                    product_id=Product.objects.get(id=id)).update(
                    quantity=quantity, date_add=strftime("%d-%m-%y", gmtime()), total=total)
                if result == 0:
                    CartDetail(quantity=quantity, date_add=strftime("%d-%m-%y", gmtime()),
                               product_id=Product.objects.get(id=id),
                               cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])),
                               total=total).save()
        except:
            Cart(user_id=User.objects.get(id=request.session['id']), status=True).save()
            CartDetail(quantity=quantity, date_add=strftime("%d-%m-%y", gmtime()),
                       product_id=Product.objects.get(id=id),
                       cart_id=Cart.objects.get(user_id=request.session['id'], status=True), total=total).save()

        product = Product.objects.filter(id=request.POST.get('id')).get()
        stock = Stock.objects.filter(product_id=request.POST.get('id')).get()
        return render(request, 'userpanel/product-detail.html', {'product': product, 'stock': stock})
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           shoping cart                #########################################
##################################################################################################
##################################################################################################
def shoping_cart(request):
    if checkSessionVars(request):
        try:
            cart_details = CartDetail.objects.filter(
                cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])))
            total = 0
            for dtls_obj in cart_details:
                total += dtls_obj.total
            return render(request, 'userpanel/shoping-cart.html', {'cart_details': cart_details, 'total': total})
        except:
            return HttpResponseRedirect(reverse('userpanel'))
    return HttpResponseRedirect(reverse('login'))


def product_remove_from_cart(request):
    if checkSessionVars(request):
        obj = CartDetail.objects.filter(id=request.POST.get('id')).get()
        obj.delete()
        cart_details = CartDetail.objects.filter(
            cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])))
        total = 0
        for dtls_obj in cart_details:
            total += dtls_obj.total
        return render(request, 'userpanel/shoping-cart.html', {'cart_details': cart_details, 'total': total})
    return HttpResponseRedirect(reverse('login'))


def checkout(request):
    if checkSessionVars(request):

        SalesOrder(address=request.POST.get('address'), date=strftime("%d_%m_%y_%H_%M_%S", gmtime()), status=False,
                   user_id=User.objects.get(id=request.session['id'])).save()

        sales_id = SalesOrder.objects.filter(user_id=User.objects.get(id=request.session['id']), status=False).last()
        cart_details = CartDetail.objects.filter(
            cart_id=Cart.objects.get(user_id=User.objects.get(id=request.session['id'])))

        for item in cart_details:
            SalesOrderDetail(quantity=item.quantity, total=item.total,
                             product_id=item.product_id, sales_order_id=sales_id).save()

            t_stock = Stock.objects.filter(product_id=item.product_id.id).first()
            t_available = t_stock.available - item.quantity
            t_sales = t_stock.sales + item.quantity
            Stock.objects.filter(product_id=item.product_id.id).update(sales=t_sales, available=t_available)

        cart = Cart.objects.get(user_id=User.objects.get(id=request.session['id']))
        cart.delete()
        return HttpResponseRedirect(reverse('userpanel'))
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           Account                #########################################
##################################################################################################
##################################################################################################

def show_myaccount(request):
    if checkSessionVars(request):
        user = User.objects.filter(id=request.session['id']).first()
        return render(request, 'userpanel/show_myaccount.html', {'user': user})
    return HttpResponseRedirect(reverse('login'))


def edit_profile(request):
    if checkSessionVars(request):
        User.objects.filter(id=request.session['id']).update(
            name=request.POST.get('name'), email=request.POST.get('email'), address=request.POST.get('address'),
            dob=request.POST.get('dob'), m_no=request.POST.get('m_no')
        )
        return HttpResponseRedirect(reverse('show_myaccount'))
    return HttpResponseRedirect(reverse('login'))


def show_change_pass(request):
    if checkSessionVars(request):
        old_p_status = False
        update = False
        c_p_status = False
        return render(request, 'userpanel/show_change_pass.html',
                      {'c_p_status': c_p_status, 'update': update, 'old_p_status': old_p_status})
    return HttpResponseRedirect(reverse('login'))


def edit_password(request):
    if checkSessionVars(request):
        old_p_status = False
        update = False
        c_p_status = False
        user = User.objects.filter(id=request.session['id']).first()
        old_pass = request.POST.get('o_password')
        n_pass = request.POST.get('n_password')
        c_pass = request.POST.get('c_password')
        if old_pass == user.password:
            if n_pass == c_pass:
                User.objects.filter(id=request.session['id']).update(
                    password=n_pass
                )
                update = True
                old_p_status = False
            else:
                c_p_status = True
        else:
            update = False
            old_p_status = True
        return render(request, 'userpanel/show_change_pass.html',
                      {'c_p_status': c_p_status, 'update': update, 'old_p_status': old_p_status})
    return HttpResponseRedirect(reverse('login'))
