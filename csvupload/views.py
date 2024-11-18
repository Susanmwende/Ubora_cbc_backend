from django.http import JsonResponse, HttpResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from .models import School

@csrf_exempt
def upload_school_csv(request):
    if request.method == 'POST':
        # Step 1: Confirm if the file exists in the request
        if 'csv_file' not in request.FILES:
            print("CSV file not found in the request.")  # Log this
            return JsonResponse({"error": "No file uploaded."}, status=400)

        csv_file = request.FILES['csv_file']
        print(f"Received file: {csv_file.name}")  # Log file name

        try:
            # Step 2: Read the file with pandas
            data_df = pd.read_csv(csv_file)
            print("CSV data loaded successfully.")  # Log successful load

            # Replace NaN values with None
            data_df = data_df.where(pd.notnull(data_df), None)

            # Convert to JSON-like records
            df_json = data_df.to_dict(orient='records')
            print(f"Data to insert: {df_json}")  # Log the data to be inserted

            # Step 3: Insert records into the database
            for row in df_json:
                School.objects.create(
                    code=row.get('code'),
                    school_name=row.get('school_name'),
                    level=row.get('level'),
                    school_status=row.get('school_status'),
                    school_type=row.get('school_type'),
                    county=row.get('county'),
                    sub_county=row.get('sub_county'),
                    division=row.get('division'),
                    location=row.get('location'),
                    constituency=row.get('constituency')
                )
            print("Data inserted into the database.")  # Log successful insertion
            return JsonResponse({"message": "CSV Uploaded and Data Inserted"}, status=201)

        except Exception as e:
            print(f"Error while processing CSV: {e}")  # Log the error
            return JsonResponse({"error": str(e)}, status=500)

    print("Invalid request method.")  # Log invalid method
    return JsonResponse({"error": "Invalid request method"}, status=405)
