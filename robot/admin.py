
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import (
    Person,
    Product,
    Services,
    HomePageImgSlider,
    AdvisoryCommitteeMember,
    ContactMessage,
    Costomer_Oder_list_details,
    UserCartItem,
    Order, OrderItem,
    ScientificCommitteeMember,
)
from adminsortable2.admin import SortableAdminBase
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
import json
from django.utils.html import format_html



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview','id', 'category', 'price', 'visibility', 'date_added')
    list_filter = ('visibility', 'category','id','date_added')
    search_fields = ('id','name', 'category', 'description')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view
    def image_preview(self, obj):
        if obj.image1:
            return mark_safe(f' <a href="{obj.image1.url}"> <img src="{obj.image1.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'




@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):  # ❌ No sortable
    list_display = ('name', 'email', 'subject', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('name', 'email', 'subject')




# ✅ For top-level sorting, inherit from SortableAdminBase + admin.ModelAdmin
@admin.register(Person)
class PersonAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'image_preview','designation')
    search_fields = ('name', 'designation')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f' <a href="{obj.image_url.url}"> <img src="{obj.image_url.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'



@admin.register(Services)
class ServicesAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name','image_preview', 'price', 'visibility', 'date_added')
    list_filter = ('visibility',)
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f' <a href="{obj.image_url.url}"> <img src="{obj.image_url.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'



@admin.register(HomePageImgSlider)
class HomePageImgSliderAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'BtnText', 'Btnlink','image_preview')
    search_fields = ('name', 'BtnText')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f' <a href="{obj.image_url.url}"> <img src="{obj.image_url.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'



@admin.register(AdvisoryCommitteeMember)
class AdvisoryCommitteeMemberAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name','image_preview', 'designation', 'image')
    search_fields = ('name', 'designation')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f' <a href="{obj.image.url}"> <img src="{obj.image.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'


@admin.register(ScientificCommitteeMember)
class ScientificCommitteeMemberAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name','image_preview', 'designation', 'image')
    search_fields = ('name', 'designation')
    readonly_fields = ('image_preview',)  # ⬅️ this shows image in detail view

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f' <a href="{obj.image.url}"> <img src="{obj.image.url}" width="100px" height="auto" /></a>')
        return "No image uploaded"
    image_preview.short_description = 'Image Preview'



@admin.register(Costomer_Oder_list_details)
class Costomer_Oder_list_detailsAdmin(SortableAdminMixin, SortableAdminBase, admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email')
    # pass




class UserProductInline(admin.TabularInline):  # or admin.StackedInline
    model = UserCartItem
    extra = 0
    readonly_fields = ('product_display',)
    fields = ('product_display',)
    can_delete = False

    def product_display(self, obj):
        try:
            # Retrieve product by ID
            product = Product.objects.filter(id=obj.product_id).first()
            count = obj.product_count

            if product:
                image_html = (
                    f'<img src="{product.image1.url}" width="60" style="margin-right:10px;" />'
                    if product.image1 else "No image"
                )
                total_price = product.price * count
                return mark_safe(f"""
                    <div style="margin-bottom:10px; display:flex; align-items:center;">
                        {image_html}
                        <div>
                            <strong>{product.name}</strong><br/>
                            Quantity: {count}<br/>
                            Unit Price: ₹{product.price}<br/>
                            <strong>Total: ₹{total_price}</strong>
                        </div>
                    </div>
                """)
            else:
                return f"<div>Unknown Product ID {obj.product_id}</div>"

        except Exception as e:
            return f"<div style='color:red;'>Error: {str(e)}</div>"

    product_display.short_description = 'Cart Contents'




class UserCartItemAdmin(admin.ModelAdmin):
    list_display = ('user','product_id','product_count')
    search_fields = ('user', 'product_id','product_count')
    readonly_fields = ('product_display','product_id','product_count','user')
    list_filter = ('user','product_id','product_count')

    # fields = ('product_display',)
    def product_display(self, obj):
        try:
            # Retrieve product by ID
            product = Product.objects.filter(id=obj.product_id).first()
            count = obj.product_count

            if product:
                image_html = (
                    f'<img src="{product.image1.url}" width="60" style="margin-right:10px;" />'
                    if product.image1 else "No image"
                )
                total_price = product.price * count
                return mark_safe(f"""
                    <div style="margin-bottom:10px; display:flex; align-items:center;">
                        {image_html}
                        <div>
                            <strong>{product.name}</strong><br/>
                            Quantity: {count}<br/>
                            Unit Price: ₹{product.price}<br/>
                            <strong>Total: ₹{total_price}</strong>
                        </div>
                    </div>
                """)
            else:
                return f"no product"

        except Exception as e:
            return f"<div style='color:red;'>Error: {str(e)}</div>"

    product_display.short_description = 'Cart Contents'





admin.site.unregister(User)

# Extend the User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserProductInline]

# Re-register the User admin with inline
admin.site.register(User, UserAdmin)

admin.site.register(UserCartItem, UserCartItemAdmin)







class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product_name', 'price', 'quantity', 'total', 'product_image_preview']
    fields = ['product_name', 'price', 'quantity', 'total', 'product_image_preview']
    extra = 0
    can_delete = False

    def product_image_preview(self, obj):
        if obj.product_image:
            return format_html(f'<img src="{obj.product_image.url}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />')
        return "No Image"

    product_image_preview.short_description = "Product Image"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'user','id', 'first_name', 'total', 'status', 'created_at']
    # readonly_fields = ['user', 'first_name', 'total',  'created_at']
    list_filter = ['user','status', 'created_at','first_name', 'last_name', 'email','id',]
    search_fields = ['user','status', 'created_at','first_name', 'last_name', 'email','id']
    inlines = [OrderItemInline]


class UserOrderInline(admin.TabularInline):
    model = Order
    extra = 0
    can_delete = False
    
    readonly_fields = ['view_link','id', 'order_link', 'total', 'status', 'created_at']
    fields = ['view_link','order_link', 'total', 'status', 'created_at']
    show_change_link = True  # makes each order clickable
    def order_link(self, obj):
        return f"Order Id: {obj.id}"

    order_link.short_description = "Details"
    def view_link(self, obj):
        return ""  # Placeholder, link still works from pencil icon

    view_link.short_description = "See Order"  

# Unregister first (you already did)
admin.site.unregister(User)

# ✅ Append the Order inline to your existing UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = [UserProductInline, UserOrderInline]  # 🧾 Added Order inline here

# Re-register
admin.site.register(User, UserAdmin)
# admin.site.register(OrderItem)