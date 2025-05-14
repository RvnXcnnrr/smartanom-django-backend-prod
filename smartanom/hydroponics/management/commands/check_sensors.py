from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from hydroponics.models import Sensor

class Command(BaseCommand):
    help = 'Verify DHT22 sensor configuration'

    def handle(self, *args, **options):
        User = get_user_model()
        
        print("Checking DHT22 sensor configurations...")
        
        # Check if any users have DHT22 sensors
        sensors = Sensor.objects.filter(type="DHT22").select_related(
            'smar_tanom__hydroponic__user'
        )
        
        if not sensors.exists():
            print("No DHT22 sensors found in database!")
            return
            
        print("\nConfigured DHT22 sensors:")
        for sensor in sensors:
            print(f"- User: {sensor.smar_tanom.hydroponic.user.email}")
            print(f"  Sensor ID: {sensor.id}")
            print(f"  Status: {sensor.status}\n")