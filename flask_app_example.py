from flask import Flask, request, jsonify
from credeed_pdf_to_markdown import PDFToMarkdownConverter
import tempfile

app = Flask(__name__)

# Replace these with your real credentials
AZURE_ENDPOINT = "https://<your-doc-intel-endpoint>.cognitiveservices.azure.com/"
AZURE_KEY = "<your-azure-key>"
AWS_ACCESS_KEY = "<your-aws-access-key>"
AWS_SECRET_KEY = "<your-aws-secret-key>"
S3_BUCKET = "<your-s3-bucket-name>"
S3_REGION = "ap-southeast-1"  # Modify if different

converter = PDFToMarkdownConverter(
    azure_endpoint=AZURE_ENDPOINT,
    azure_key=AZURE_KEY,
    s3_bucket=S3_BUCKET,
    aws_access_key=AWS_ACCESS_KEY,
    aws_secret_key=AWS_SECRET_KEY,
    s3_region=S3_REGION
)

@app.route("/convert", methods=["POST"])
def convert_pdf():
    try:
        # 1. Check if pdf_url is provided
        pdf_url = request.form.get("pdf_url")
        if pdf_url:
            result_url = converter.convert(pdf_url)
            return jsonify({"status": "success", "markdown_url": result_url}), 200

        # 2. Or handle uploaded file
        file = request.files.get("pdf_file")
        if file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                file.save(tmp_file.name)
                result_url = converter.convert(tmp_file.name)
                return jsonify({"status": "success", "markdown_url": result_url}), 200

        return jsonify({"status": "error", "message": "Please provide a PDF file or pdf_url"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
