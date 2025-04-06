from rest_framework import serializers
from .models import Product, Category, Retailer, Order,  Employee, Truck, Shipment

from django.contrib.auth.models import User, Group

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')  # Fetching category name instead of ID

    class Meta:
        model = Product
        fields = '__all__'  # Keep all fields from the Product model, but override 'category'


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    def update(self, instance, validated_data):
        """
        When status is updated to 'delivered', update:
        - The order's status
        - The product's total_required_quantity and total_shipped
        """
        if "status" in validated_data and validated_data["status"] == "delivered":
            order = instance.order
            product = order.product

            # Update order status
            order.status = "delivered"
            order.save(update_fields=["status"])

            # Update product details
            product.total_required_quantity = max(0, product.total_required_quantity - order.required_qty)
            product.total_shipped += order.required_qty
            product.save(update_fields=["total_required_quantity", "total_shipped"])

        return super().update(instance, validated_data)
    
class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'product_count']


class UserRegistrationSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(write_only=True)  # Accept group name during registration

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'group_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        group_name = validated_data.pop('group_name', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Assign the user to the specified group
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError({"group_name": "Group does not exist."})

        return user