import uuid
from datetime import datetime
from fpdf import FPDF
from flask import jsonify
from google.cloud import storage

# Initialize Google Cloud Storage client
storage_client = storage.Client()

def generate_pdf(request):
    """Cloud Function to generate a PDF from text and provide a downloadable link."""
    try:
        # Parse JSON input
        request_json = request.get_json(silent=True)
        if not request_json:
            return jsonify({"error": "Request must contain a JSON body."}), 400

        long_text = request_json.get("text")
        if not long_text:
            return jsonify({"error": "'text' field is required."}), 400

        # Generate a unique name for the PDF
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = uuid.uuid4().hex[:8]
        pdf_file_name = f"document_{timestamp}_{unique_id}.pdf"

        # Generate the PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=long_text)

        # Upload PDF to Google Cloud Storage
        bucket_name = "" 
        if not bucket_name:
            return jsonify({"error": "CLOUD_STORAGE_BUCKET environment variable not set."}), 500

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(pdf_file_name)
        blob.upload_from_string(pdf.output(dest="S").encode("latin1"), content_type="application/pdf")
        
        # Construct the public URL
        pdf_url = f"https://storage.googleapis.com/{bucket_name}/{pdf_file_name}"

        # Return the downloadable link
        return jsonify({
            "message": "PDF generated and uploaded successfully.",
            "pdf_url": pdf_url
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
