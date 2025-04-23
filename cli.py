import argparse
from credeed_pdf_to_markdown import PDFToMarkdownConverter

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown using Azure AI and upload to S3.")
    parser.add_argument("source", help="PDF file path or URL")
    parser.add_argument("--azure-endpoint", required=True, help="Azure Document Intelligence endpoint")
    parser.add_argument("--azure-key", required=True, help="Azure Document Intelligence key")
    parser.add_argument("--s3-bucket", required=True, help="AWS S3 bucket name")
    parser.add_argument("--aws-access-key", required=True, help="AWS Access Key ID")
    parser.add_argument("--aws-secret-key", required=True, help="AWS Secret Access Key")
    parser.add_argument("--s3-region", default="ap-southeast-1", help="AWS S3 region (default: ap-southeast-1)")

    args = parser.parse_args()

    converter = PDFToMarkdownConverter(
        azure_endpoint=args.azure_endpoint,
        azure_key=args.azure_key,
        s3_bucket=args.s3_bucket,
        aws_access_key=args.aws_access_key,
        aws_secret_key=args.aws_secret_key,
        s3_region=args.s3_region
    )

    try:
        markdown_url = converter.convert(args.source)
        print(f"✅ Markdown file uploaded: {markdown_url}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
