from datetime import datetime
from influxdb_client import InfluxDBClient


# Parameter
token = "MUuECMKhp10IrqXczdTu-9sY16GyZfRS6Uco4w-a_IauwLpYctE0zwq0JJA4_N8AvCqK4MWC7iCDvvsdENikFg=="
org = "yk2797@columbia.edu"
bucket = "yk2797's Bucket"

client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token=token)
