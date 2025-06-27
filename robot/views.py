from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .data_sender_in_taligram import send_data_taligram,Order_detail_Send
from robot.models import Person,Services,Product,HomePageImgSlider,AdvisoryCommitteeMember,ContactMessage,UserCartItem, Order, OrderItem,ScientificCommitteeMember
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q # Not strictly needed for this, but good for future search
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

def index(request):
    services = Services.objects.filter(visibility='show')
    sliders = HomePageImgSlider.objects.all()

    # Get all visible products, ordered by category and date (you can change the order logic)
    all_products = Product.objects.filter(visibility='show').order_by('category', '-date_added')

    # Group by category and get one product per category
    seen_categories = set()
    unique_category_products = []

    for product in all_products:
        if product.category not in seen_categories:
            unique_category_products.append(product)
            seen_categories.add(product.category)

    return render(request, 'robot/index.html', {
        'services': services,
        'products': unique_category_products,  # one product per category
        'sliders': sliders,
    })

def about(request):
    all_people = Person.objects.all()
    return render(request, 'robot/About.html', {'people': all_people})

def admin_dashboard(request):
    return render(request, 'robot/Admin_Dashboard.html')


@login_required
def checkout(request):
    cart_items = UserCartItem.objects.filter(user=request.user)
    products = Product.objects.filter(visibility='show')

    items = []
    subtotal = 0

    for item in cart_items:
        product = next((p for p in products if p.id == item.product_id), None)
        if product:
            item_total = product.price * item.product_count
            subtotal += item_total
            items.append({
                'name': product.name,
                'price': product.price,
                'quantity': item.product_count,
                'total': item_total,
                'image_url': product.image1.url
            })

    shipping = 150 if subtotal > 0 else 0
    total = subtotal + shipping
    if total==0:
        return redirect('your_cart')
    if request.method == 'POST':
        if total==0:
            return redirect('your_cart')
        # Get form fields
        first_name = request.POST.get('billingFirstName')
        last_name = request.POST.get('billingLastName')
        email = request.POST.get('billingEmail')
        phone = request.POST.get('billingPhone')
        address1 = request.POST.get('billingAddress1')
        address2 = request.POST.get('billingAddress2')
        city = request.POST.get('billingCity')
        state = request.POST.get('billingState')
        zip_code = request.POST.get('billingZip')
        payment_method = request.POST.get('paymentMethod')

        # Save order
        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            payment_method=payment_method,
            subtotal=subtotal,
            shipping=shipping,
            total=total,
            status='pending',
            estimated_delivery=timezone.now().date() + datetime.timedelta(days=5)
        )

        for item in cart_items:
            product = next((p for p in products if p.id == item.product_id), None)
            if product:
                OrderItem.objects.create(
                    order=order,
                    product_name=product.name,
                    product_image=product.image1,
                    price=product.price,
                    quantity=item.product_count,
                    total=product.price * item.product_count
                )

        # Send Telegram Notification
        order_message = f"""
🎉 New Order Alert! 🎉
❤️ Order Id: _____ {order.id}_____
👤 Customer: {first_name} {last_name}
📧 Email: {email}
📞 Phone: {phone}

🏠 Address:
📍 {address1}
🏢 {address2 if address2 else 'N/A'}
🌆 {city}, 🗺️ {state} - {zip_code}

🛒 Order Summary:
"""

        for item in items:
            order_message += f"""
📦 {item['name']}
🔢 Quantity: {item['quantity']}
💵 Price: ₹{item['price']}
🧮 Total: ₹{item['total']}
🖼️ Image: {request.build_absolute_uri(item['image_url'])}
"""

        order_message += f"""
💰 Payment: {payment_method.upper()}
🧾 Subtotal: ₹{subtotal}
🚚 Shipping: ₹{shipping}
💳 Total: ₹{total}

📦 Status: Pending
⏰ Placed On: {timezone.now().strftime('%A, %d %B %Y - %I:%M %p')}
"""

        Order_detail_Send(order_message)
        # ✅ Save last order data in session
# Convert all Decimal values to float to avoid JSON error
        request.session['last_order'] = {
    'order_id': order.id,
    'name': f"{first_name} {last_name}",
    'email': email,
    'subtotal': float(subtotal),
    'shipping': float(shipping),
    'total': float(total),
    'items': [
            {
                'name': item['name'],
                'price': float(item['price']),
                'quantity': item['quantity'],
                'total': float(item['total']),
                'image_url': item['image_url'],
            }
            for item in items
    ]
}

        # ✅ Delete items from user's cart
        UserCartItem.objects.filter(user=request.user).delete()
        return redirect('order_confirmed')

    return render(request, 'robot/Checkout.html', {
        'items': items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })




@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get('subject')
        message = request.POST.get("message")
        NoofList = ContactMessage.objects.all().count()
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # 👉 Save to DB or send email here
        send_data_taligram(
                f"📄 New Form Submission\n\n"
                f"🔢 Serial No: {NoofList+1}\n"
                f"👤 Name: {name}\n"
                f"📧 Email: {email}\n"
                f"📞 Phone: {subject}\n"
                f"💬 Message: {message}"
            )  # or save it
        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')
    return render(request, 'robot/Contact.html')

def home(request):
    return render(request, 'robot/Home.html')

def order_confirmed(request):
    last_order = request.session.get('last_order')

    if not last_order:
        return redirect('home')  # or show a friendly message

    return render(request, 'robot/Order_Confirmed.html', {
        'order': last_order
    })



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    user_name = request.GET.get('user_name')
    product_count = request.GET.get('product_count')

    # Handle cart logic
    if user_name and product_count:
        try:
            user = User.objects.get(username=user_name)
            count = int(product_count)
            if count > 0:
                item, created = UserCartItem.objects.get_or_create(
                    user=user,
                    product_id=product.id,
                    defaults={'product_count': count}
                )
                if not created:
                    item.product_count += count
                    item.save()

                # ✅ Redirect to same page without query params
                return redirect('product_detail', product_id=product.id)

        except (User.DoesNotExist, ValueError):
            pass  # Invalid user or count; do nothing

    # Just render the product page
    return render(request, 'robot/Product_Detail.html', {'product': product})

def services(request):
    services = Services.objects.all()

    return render(request, 'robot/Services.html' ,{'services': services})



def services_open(request):
    return render(request, 'robot/Services_open.html')





def shop(request):
    # Get all products that are set to 'show'
    products_list = Product.objects.filter(visibility='show')

    # --- Category Filtering ---
    selected_category = request.GET.get('category')
    if selected_category:
        products_list = products_list.filter(category=selected_category)

    # --- Sorting ---
    sort_by = request.GET.get('sort_by', 'popularity') # Default to popularity
    if sort_by == 'price_asc':
        products_list = products_list.order_by('price')
    elif sort_by == 'price_desc':
        products_list = products_list.order_by('-price')
    elif sort_by == 'newest':
        products_list = products_list.order_by('-date_added')
    else: # 'popularity' or any other default
        products_list = products_list.order_by('-date_added') # Or some other default logic for popularity


    # --- Pagination ---
    paginator = Paginator(products_list, 9) # Show 9 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    # Get unique categories for the sidebar filter
    categories = Product.objects.order_by().values_list('category', flat=True).distinct()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category, # Pass selected category to template
        'sort_by': sort_by, # Pass current sort_by to template
    }
    return render(request, 'robot/Shop.html', context)



@login_required
def your_cart(request):
    products = Product.objects.filter(visibility='show')
    cart_items = UserCartItem.objects.filter(user=request.user)

    subtotal = 0
    has_products = False  # default

    for item in cart_items:
        product = None
        for p in products:
            if p.id == item.product_id:
                product = p
                break

        if product:
            has_products = True
            subtotal += product.price * item.product_count

    if subtotal > 0:
        shipping = 150
    else:
        shipping = 0

    total = subtotal + shipping

    return render(request, 'robot/Your_Cart.html', {
        'products': products,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
        'has_products': has_products  # send this flag to template
    })

@login_required
def update_cart_quantity(request):
    item_id = request.GET.get('id')
    action = request.GET.get('action')
    item = get_object_or_404(UserCartItem, id=item_id, user=request.user)

    if action == 'increase':
        item.product_count += 1
    elif action == 'decrease':
        item.product_count = max(1, item.product_count - 1)
    item.save()

    return redirect('your_cart')

@login_required
def remove_from_cart(request):
    item_id = request.GET.get('id')
    item = get_object_or_404(UserCartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('your_cart')



def advisory_committee(request):
    committee_members = ScientificCommitteeMember.objects.all()  # get all members
    advisory_members = AdvisoryCommitteeMember.objects.all()  # get all members
    return render(request, 'robot/advisory-committee.html', {
        'committee_members': committee_members,
        'advisory_members':advisory_members,
    })



def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'robot/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)  # Find user with this email
            user = authenticate(request, username=user_obj.username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                form ='wrong password'
                return render(request, 'robot/login.html',{'formp': form})

        except User.DoesNotExist:
                form ='user not exist!'
                return render(request, 'robot/login.html',{'forme': form})


    return render(request, 'robot/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def order_tracking(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'robot/order_tracking.html', {'orders': orders})



def custom_404(request, exception):
    return redirect(request,'')