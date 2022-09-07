import logging
import uuid
import boto3
from django.conf import settings
from botocore.exceptions import ClientError
from PIL import Image
import io


UPLOAD_DIRECTORY = "uploaded_data"


s3_client = boto3.client(
        "s3", 
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY, 
        aws_secret_access_key=settings.AWS_SECRET_KEY
        )

def upload_file(file_obj):
    """Upload a file to S3 bucket.

    :param file_obj: File Object to upload
    """
    file_ext = file_obj.name.split(".")[-1]
    obj_name = str(uuid.uuid4()) + "." + file_ext

    try:
        s3_client.upload_fileobj(file_obj, settings.AWS_BUCKET_NAME, f"{UPLOAD_DIRECTORY}/{obj_name}")
        logging.info("File uploaded with name: {}".format(obj_name), obj_name)

        return obj_name
    except ClientError as e:
        logging.error(e)


def delete_remote_file(uri):
    s3_client = boto3.client("s3", aws_access_key_id=settings.AWS_ACCESS_KEY,
                             aws_secret_access_key=settings.AWS_SECRET_KEY)
    try:
        s3_client.delete_object(Bucket=settings.AWS_BUCKET_NAME, Key=f"{UPLOAD_DIRECTORY}/{uri}")
        logging.info("File deleted with name: {}".format(uri))

    except ClientError as e:
        logging.error(e)


def read_image(uri):
    key = f"{UPLOAD_DIRECTORY}/{uri}"
    s3 = boto3.resource('s3')
    image = s3.Object(bucket_name=settings.AWS_BUCKET_NAME, key=key)
    img_data = image.get().get('Body').read()
    return Image.open(io.BytesIO(img_data))


s3_download_client = boto3.client(
        "s3", 
        endpoint_url=settings.AWS_S3_DOWNLOAD_ENDPOINT_URL,
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY, 
        aws_secret_access_key=settings.AWS_SECRET_KEY
        )

def get_public_link(s3_file_name):
    """Getting a publicly accessible link to an asset.

    :param s3_file_name: name of file object which is uploaded before.
    """
    try:
        return s3_download_client.generate_presigned_url("get_object", Params={
            "Bucket": settings.AWS_BUCKET_NAME, "Key": f"{UPLOAD_DIRECTORY}/{s3_file_name}"}, ExpiresIn=3600)
    except ClientError as e:
        logging.error(e)
