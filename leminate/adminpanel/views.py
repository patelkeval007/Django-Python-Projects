import os
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account.models import User, Supplier, Category, Color, Design, Product, SalesOrder, SalesOrderDetail, Stock
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from time import gmtime, strftime
from .render import Render
import xlwt
from django.http import HttpResponse
import csv


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


def upload_design_csv(request):
    if checkSessionVars(request):
        try:
            csv_file = request.FILES["myfile"]
            if not csv_file.name.endswith('.csv'):
                print('Not csv file.')
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            # loop over the lines and save them in db. If error , store as string and then display
            for line in lines:
                fields = line.split(",")
                Design(name=fields[0]).save()

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

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            myfile.name = strftime("%d_%m_%y_%H_%M_%S", gmtime()) + '.jpg'
            filename = fs.save(myfile.name, myfile)

            putData = Product(name=tname, description=tdescription, qoh=tqoh, price=tprice, image=filename,
                              cat_id=Category.objects.get(id=tcategory),
                              color_id=Color.objects.get(id=tcolor), design_id=Design.objects.get(id=tdesign),
                              supplier_id=Supplier.objects.get(id=tsupplier))
            putData.save()
            Stock(purchase=tqoh, sales=0, available=tqoh, product_id=Product.objects.latest('id')).save()
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
        t_product = Product.objects.filter(id=request.POST.get('id')).first()
        t_qoh = t_product.qoh + int(request.POST.get('qoh'))
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            object = Product.objects.filter(id=request.POST.get('id')).get()
            img_path = getattr(settings, 'MEDIA_ROOT') + '\\' + object.image

            if os.path.exists(img_path):
                os.remove(img_path)

            fs = FileSystemStorage()
            myfile.name = strftime("%d_%m_%y_%H_%M_%S", gmtime()) + '.jpg'
            filename = fs.save(myfile.name, myfile)

            Product.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                                     description=request.POST.get('description'),
                                                                     qoh=t_qoh,
                                                                     price=request.POST.get('price'),
                                                                     image=filename,
                                                                     cat_id=request.POST.get('cat_id'),
                                                                     color_id=request.POST.get('color_id'),
                                                                     design_id=request.POST.get('design_id'),
                                                                     supplier_id=request.POST.get('supplier_id'))
            Stock.objects.filter(product_id=request.POST.get('id')).update(purchase=request.POST.get('qoh'))
        else:
            Product.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'),
                                                                     description=request.POST.get('description'),
                                                                     qoh=t_qoh,
                                                                     price=request.POST.get('price'),
                                                                     cat_id=request.POST.get('cat_id'),
                                                                     color_id=request.POST.get('color_id'),
                                                                     design_id=request.POST.get('design_id'),
                                                                     supplier_id=request.POST.get('supplier_id'))
            t_stock = Stock.objects.filter(product_id=request.POST.get('id')).first()
            t_available = t_stock.available + int(request.POST.get('qoh'))
            t_purchase = t_stock.purchase + int(request.POST.get('qoh'))
            Stock.objects.filter(product_id=request.POST.get('id')).update(purchase=t_purchase, available=t_available)
        return HttpResponseRedirect(reverse('show_product'))
    except:
        return HttpResponseRedirect(reverse('show_product'))


def del_product(request):
    if checkSessionVars(request):
        try:
            object = Product.objects.filter(id=request.POST.get('id')).get()
            img_path = getattr(settings, 'MEDIA_ROOT') + '\\' + object.image

            if os.path.exists(img_path):
                os.remove(img_path)

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


##################################################################################################
##################################################################################################
###################################           Stock                #########################################
##################################################################################################
##################################################################################################

def show_stock(request):
    if checkSessionVars(request):
        stock = Stock.objects.all()
        out_status = False
        for item in stock:
            if item.available == 0:
                out_status = True
        return render(request, 'adminpanel/show_stock.html', {'stocks': stock, 'out_status': out_status})


def show_out_stock(request):
    if checkSessionVars(request):
        stock = Stock.objects.all()
        return render(request, 'adminpanel/show_out_stock.html', {'stocks': stock})


##################################################################################################
##################################################################################################
###################################           Reports                #########################################
##################################################################################################
##################################################################################################

def show_report(request):
    return render(request, 'adminpanel/show_report.html')


################################# Stock Report #######################################################
def show_report_stock(request):
    return render(request, 'adminpanel/show_report_stock.html')


def stock_overall_pdf(request):
    stocks = Stock.objects.all()
    params = {
        'today': strftime("%d/%m/%y", gmtime()),
        'name': request.session['name'],
        'stocks': stocks,
    }
    return Render.render('adminpanel/stock_overall_pdf.html', params)


def stock_month_pdf(request):
    stocks = Stock.objects.all()
    date = request.POST.get('date')
    print(date)
    params = {
        'today': strftime("%d/%m/%y", gmtime()),
        'name': request.session['name'],
        'stocks': stocks,
    }
    return Render.render('adminpanel/stock_month_pdf.html', params)


def users_pdf(request):
    users = User.objects.all()
    date = request.POST.get('date')
    print(date)
    params = {
        'today': strftime("%d/%m/%y", gmtime()),
        'name': request.session['name'],
        'users': users,
    }
    return Render.render('adminpanel/users_pdf.html', params)


def users_excel(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')
    # decide file name
    response['Content-Disposition'] = 'attachment; filename="leminates_customers.xls"'
    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')
    # adding sheet
    ws = wb.add_sheet("sheet1")
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
    # column header names, you can use your own headers here
    columns = ['Name', 'Email', 'DOB', 'Address', 'Contact']
    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    data = User.objects.all()  # dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.name, font_style)
        ws.write(row_num, 1, my_row.email, font_style)
        ws.write(row_num, 2, my_row.dob, font_style)
        ws.write(row_num, 3, my_row.address, font_style)
        ws.write(row_num, 4, my_row.m_no, font_style)

    wb.save(response)
    return response


def sales_pdf(request):
    sales = SalesOrderDetail.objects.all()
    date = request.POST.get('date')
    print(date)
    params = {
        'today': strftime("%d/%m/%y", gmtime()),
        'name': request.session['name'],
        'sales': sales,
        'f_date':request.POST.get('f_date'),
        't_date':request.POST.get('t_date'),
    }
    return Render.render('adminpanel/sales_pdf.html', params)
