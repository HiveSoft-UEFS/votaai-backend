from django.core.management.base import BaseCommand, CommandError
from app.db.seeder import DatabaseSeeder

class Command(BaseCommand):
    help = 'Executa a operação de seed'

    def handle(self, *args, **options):
        dbs = DatabaseSeeder()
        dbs.seed()
        self.stdout.write('Comando runseed executado com sucesso!')
