from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account.models import User, Supplier, Category, Color, Design, Product, SalesOrder, SalesOrderDetail


def checkSessionVars(request):
    if 'id' in request.session and 'is_admin' in request.session:
        if request.session['is_admin'] == 1:
            return True
    else:
        return False


def index(request):
    if checkSessionVars(request):
        return render(request, 'adminpanel/index.html', {'request': request})
    return HttpResponseRedirect(reverse('login'))


##################################################################################################
##################################################################################################
###################################           Users                #########################################
##################################################################################################
##################################################################################################

def show_user(request):
    if checkSessionVars(request):
        users = User.objects.filter(is_admin=False)
        return render(request, 'adminpanel/show_user.html', {'users': users})


def update_user_page(request):
    if checkSessionVars(request):
        try:
            user = User.objects.filter(id=request.POST.get('id')).get()
            return render(request, 'adminpanel/update_user.html', {'user': user})
        except:
            return HttpResponseRedirect(reverse('show_user'))
    return HttpResponseRedirect(reverse('login'))


def update_user(request):
    try:
        User.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                              email=request.POST.get('email'),
                                                              address=request.POST.get('address'),
                                                              dob=request.POST.get('dob'),
                                                              m_no=request.POST.get('m_no'))
        return HttpResponseRedirect(reverse('show_user'))
    except:
        return HttpResponseRedirect(reverse('show_user'))


def del_user(request):
    if checkSessionVars(request):
        try:
            User.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_user'))
        except:
            return HttpResponseRedirect(reverse('show_user'))


##################################################################################################
##################################################################################################
###################################           Suppliers                #########################################
##################################################################################################
##################################################################################################
def show_supplier(request):
    if checkSessionVars(request):
        suppliers = Supplier.objects.all()
        return render(request, 'adminpanel/show_supplier.html', {'suppliers': suppliers})
    return HttpResponseRedirect(reverse('login'))


def add_supplier_view_page(request):
    if checkSessionVars(request):
        return render(request, 'adminpanel/add_supplier.html')
    return HttpResponseRedirect(reverse('login'))


def add_supplier(request):
    if checkSessionVars(request):
        try:
            tName = request.POST.get('name')
            tAddress = request.POST.get('address')
            tm_no = request.POST.get('m_no')
            putData = Supplier(name=tName, address=tAddress, m_no=tm_no)
            putData.save()
            return HttpResponseRedirect(reverse('show_supplier'))
        except:
            return HttpResponseRedirect(reverse('show_supplier'))
    return HttpResponseRedirect(reverse('login'))


def update_supplier_page(request):
    if checkSessionVars(request):
        try:
            supplier = Supplier.objects.filter(id=request.POST.get('id')).get()
            return render(request, 'adminpanel/update_supplier.html', {'supplier': supplier})
        except:
            return HttpResponseRedirect(reverse('show_supplier'))
    return HttpResponseRedirect(reverse('login'))


def update_supplier(request):
    try:
        Supplier.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                                  address=request.POST.get('address'),
                                                                  m_no=request.POST.get('m_no'))
        return HttpResponseRedirect(reverse('show_supplier'))
    except:
        return HttpResponseRedirect(reverse('show_supplier'))


def del_supplier(request):
    if checkSessionVars(request):
        try:
            Supplier.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_supplier'))
        except:
            return HttpResponseRedirect(reverse('show_supplier'))


##################################################################################################
##################################################################################################
###################################           Category                #########################################
##################################################################################################
##################################################################################################
def show_category(request):
    if checkSessionVars(request):
        category = Category.objects.all()
        return render(request, 'adminpanel/show_category.html', {'category': category})
    return HttpResponseRedirect(reverse('login'))


def add_category(request):
    if checkSessionVars(request):
        try:
            tName = request.POST.get('name')
            putData = Category(name=tName)
            putData.save()
            return HttpResponseRedirect(reverse('show_category'))
        except:
            return HttpResponseRedirect(reverse('show_category'))
    return HttpResponseRedirect(reverse('login'))


def del_category(request):
    if checkSessionVars(request):
        try:
            Category.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_category'))
        except:
            return HttpResponseRedirect(reverse('show_category'))


##################################################################################################
##################################################################################################
###################################           Colors                #########################################
##################################################################################################
##################################################################################################
def show_color(request):
    if checkSessionVars(request):
        color = Color.objects.all()
        return render(request, 'adminpanel/show_color.html', {'color': color})
    return HttpResponseRedirect(reverse('login'))


def add_color(request):
    if checkSessionVars(request):
        try:
            tName = request.POST.get('name')
            putData = Color(name=tName)
            putData.save()
            return HttpResponseRedirect(reverse('show_color'))
        except:
            return HttpResponseRedirect(reverse('show_color'))
    return HttpResponseRedirect(reverse('login'))


def del_color(request):
    if checkSessionVars(request):
        try:
            Color.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_color'))
        except:
            return HttpResponseRedirect(reverse('show_color'))


##################################################################################################
##################################################################################################
###################################           Designs                #########################################
##################################################################################################
##################################################################################################
def show_design(request):
    if checkSessionVars(request):
        design = Design.objects.all()
        return render(request, 'adminpanel/show_design.html', {'design': design})
    return HttpResponseRedirect(reverse('login'))


def add_design(request):
    if checkSessionVars(request):
        try:
            tName = request.POST.get('name')
            putData = Design(name=tName)
            putData.save()
            return HttpResponseRedirect(reverse('show_design'))
        except:
            return HttpResponseRedirect(reverse('show_design'))
    return HttpResponseRedirect(reverse('login'))


def del_design(request):
    if checkSessionVars(request):
        try:
            Design.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_design'))
        except:
            return HttpResponseRedirect(reverse('show_design'))


##################################################################################################
##################################################################################################
###################################           Products                #########################################
##################################################################################################
##################################################################################################
def show_product(request):
    if checkSessionVars(request):
            # products = Product.objects.all().select_related('colors')
            # products = Product.objects.all().values('name', 'price').annotate(n=F('name'), a=F('price'))
            # products = Product.objects.all().annotate(n=F('name'), a=F('price'))
            products = Product.objects.all()
            return render(request, 'adminpanel/show_product.html', {'products': products})
    return HttpResponseRedirect(reverse('login'))


def add_product_view_page(request):
    if checkSessionVars(request):
        category = Category.objects.all()
        color = Color.objects.all()
        design = Design.objects.all()
        supplier = Supplier.objects.all()
        return render(request, 'adminpanel/add_product.html',
                      {'color': color, 'design': design, 'category': category, 'supplier': supplier})
    return HttpResponseRedirect(reverse('login'))


def add_product(request):
    if checkSessionVars(request):
        try:
            tname = request.POST.get('name')
            tdescription = request.POST.get('description')
            tqoh = request.POST.get('qoh')
            tprice = request.POST.get('price')
            tcategory = request.POST.get('category')
            tcolor = request.POST.get('color')
            tdesign = request.POST.get('design')
            tsupplier = request.POST.get('supplier')
            putData = Product(name=tname, description=tdescription, qoh=tqoh, price=tprice,
                              cat_id=Category.objects.get(id=tcategory),
                              color_id=Color.objects.get(id=tcolor), design_id=Design.objects.get(id=tdesign),
                              supplier_id=Supplier.objects.get(id=tsupplier))
            putData.save()
            return HttpResponseRedirect(reverse('show_product'))
        except:
            return HttpResponseRedirect(reverse('show_product'))
    return HttpResponseRedirect(reverse('login'))


def update_product_page(request):
    if checkSessionVars(request):
        try:
            product = Product.objects.filter(id=request.POST.get('id')).get()
            category = Category.objects.all()
            color = Color.objects.all()
            design = Design.objects.all()
            supplier = Supplier.objects.all()
            return render(request, 'adminpanel/update_product.html',
                          {'product': product, 'color': color, 'design': design, 'category': category,
                           'supplier': supplier})
        except:
            return HttpResponseRedirect(reverse('show_product'))
    return HttpResponseRedirect(reverse('login'))


def update_product(request):
    try:
        Product.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                                 description=request.POST.get('description'),
                                                                 qoh=request.POST.get('qoh'),
                                                                 price=request.POST.get('price'),
                                                                 cat_id=request.POST.get('cat_id'),
                                                                 color_id=request.POST.get('color_id'),
                                                                 design_id=request.POST.get('design_id'),
                                                                 supplier_id=request.POST.get('supplier_id'))
        return HttpResponseRedirect(reverse('show_product'))
    except:
        return HttpResponseRedirect(reverse('show_product'))


def del_product(request):
    if checkSessionVars(request):
        try:
            Product.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_product'))
        except:
            return HttpResponseRedirect(reverse('show_product'))



##################################################################################################
##################################################################################################
###################################           Sales                #########################################
##################################################################################################
##################################################################################################

def show_sales(request):
    if checkSessionVars(request):
        sales = SalesOrderDetail.objects.all()
        return render(request, 'adminpanel/show_sales.html', {'sales': sales})


def update_sales_page(request):
    if checkSessionVars(request):
        try:
            sales = SalesOrderDetail.objects.filter(id=request.POST.get('id')).get()
            return render(request, 'adminpanel/update_sales.html', {'sales': sales})
        except:
            return HttpResponseRedirect(reverse('show_sales'))
    return HttpResponseRedirect(reverse('login'))


def update_sales(request):
    try:
        SalesOrderDetail.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                              email=request.POST.get('email'),
                                                              address=request.POST.get('address'),
                                                              dob=request.POST.get('dob'),
                                                              m_no=request.POST.get('m_no'))
        return HttpResponseRedirect(reverse('show_sales'))
    except:
        return HttpResponseRedirect(reverse('show_sales'))


def del_sales(request):
    if checkSessionVars(request):
        try:
            SalesOrderDetail.objects.get(id=request.POST.get('id')).delete()
            return HttpResponseRedirect(reverse('show_sales'))
        except:
            return HttpResponseRedirect(reverse('show_sales'))
