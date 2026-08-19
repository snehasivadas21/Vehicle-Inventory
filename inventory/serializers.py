from rest_framework import serializers
from datetime import date
from .models import Vehicle,Booking

class VehicleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehicle
        fields = ["id","name","brand","year","price_per_day","fuel_type","is_available"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id","vehicle","customer_name","customer_phone","start_date","end_date","total_amount"] 
        read_only_fields = ["total_amount"]

    def validate_customer_phone(self,value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("phone number must be exactly 10 digits")
        return value

    def validate(self,attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")
        vehicle = attrs.get("vehicle")

        if start_date and start_date < date.today():
            raise serializers.ValidationError({"start_date":"start date cannot be in the past"})
        
        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError({"end_date":"end date must be after start date"})
        
        if vehicle and not vehicle.is_available:
            raise serializers.ValidationError({"vehicle":"This vehicle is currently unavailable"})

        if vehicle and start_date and end_date:
            overlapping_bookings = Booking.objects.filter(vehicle=vehicle,start_date__lt=end_date,end_date__gt=start_date)

            if self.instance:
                overlapping_bookings = overlapping_bookings.exclude(id=self.instance.id)

            if overlapping_bookings.exists():
                raise serializers.ValidationError({"vehicle":("This vehicle is already booked""for the selected dates")})
        return attrs 

    def create(self, validated_data):
        vehicle = validated_data["vehicle"]
        start_date = validated_data["start_date"]
        end_date = validated_data["end_date"]
        days = (end_date - start_date).days

        validated_data["total_amount"] = (days * vehicle.price_per_day)

        booking = Booking.objects.create(**validated_data)

        vehicle.is_availble = False
        vehicle.save(update_fields=["is_available"])
        return booking     
        

