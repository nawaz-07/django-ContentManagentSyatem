from django_seed import Seed
from django.core.management.base import BaseCommand
from cms_app.models import CustomUser

class Command(BaseCommand):
    help = 'Seed data for admin user'

    def handle(self, *args, **options):
        admin_email = 'admin@example.com'
        
        # Check if an admin user with the specified email already exists
        if CustomUser.objects.filter(email=admin_email).exists():
            self.stdout.write(self.style.SUCCESS('Admin user with the specified email already exists. No new seed data created.'))
        else:
            seeder = Seed.seeder()
            seeder.add_entity(
                CustomUser,
                1,
                {   'id':-1,
                    'email': admin_email,
                    'full_name': 'admin user',
                    'password': 'Password@123',
                    'phone': '1234567890',
                    'is_admin': True,
                    # Add other fields as needed
                },
            )
            inserted_pks = seeder.execute()
            self.stdout.write(self.style.SUCCESS(f'Admin user seed data created successfully. PKs: {inserted_pks}'))
