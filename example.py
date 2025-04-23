from credeed_pdf_to_markdown import PDFToMarkdownConverter

converter = PDFToMarkdownConverter(
    azure_endpoint="https://<your-azure-endpoint>",
    azure_key="<your-azure-key>",
    s3_bucket="your-s3-bucket",
    aws_access_key="your-aws-access-key",
    aws_secret_key="your-aws-secret-key",
    s3_region="ap-southeast-1"
)

# Use online PDF
markdown_url = converter.convert("https://example.com/sample.pdf")
print("Markdown URL (from URL):", markdown_url)

# Or local file path
markdown_url_local = converter.convert("/path/to/local/sample.pdf")
print("Markdown URL (from file):", markdown_url_local)
