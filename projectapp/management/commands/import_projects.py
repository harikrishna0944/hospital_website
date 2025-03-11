# # projectapp/management/commands/import_projects.py
# import pandas as pd
# from django.core.management.base import BaseCommand
# from projectapp.models import Project

# class Command(BaseCommand):
#     help = 'Import project data from an Excel file'

#     def handle(self, *args, **kwargs):
#         # Replace with the actual path to your Excel file
#         df = pd.read_excel('/home/prasad/Hospital_Projects_Data.xlsx')

#         for index, row in df.iterrows():
#             Project.objects.create(
#                 sno=row['S.No'],
#                 year=row['Year'],
#                 document_link=row['Document Link'],
#                 project_id=row['Project ID'],
#                 project_details=row['Project Details']
#             )

#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))


# projectapp/management/commands/import_projects.py
import pandas as pd
from django.core.management.base import BaseCommand
from projectapp.models import Project

class Command(BaseCommand):
    help = 'Import projects from an Excel file'

    def add_arguments(self, parser):
        # Add argument for the Excel file path
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']  # Get the file path argument

        try:
            # Load the Excel file
            data = pd.read_excel(file_path, engine='openpyxl')
        except Exception as e:
            self.stderr.write(f"Error reading Excel file: {e}")
            return

        # Loop through rows and add data to the Project model
        for _, row in data.iterrows():
            project, created = Project.objects.get_or_create(
                sno=row['S.No'],
                year=row['Year'],
                document_link=row['Document Link'],
                project_id=row['Project ID'],
                project_details=row['Project Details']
            )
            if created:
                self.stdout.write(f"Added project: {project.project_id}")
            else:
                self.stdout.write(f"Skipped duplicate project: {project.project_id}")

        self.stdout.write("Import completed successfully.")

