import boto3,json,os
from boto3 import session
# from ec2_metadata import ec2_metadata
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)
# 
# RegionName = ec2_metadata.region
dynamodb = boto3.resource('dynamodb',region_name="us-east-1")
#dynamodb = boto3.resource('dynamodb',region_name=os.environ['AWS_REGION'])

fopen = open("/etc/environment", "r")
for x in fopen:
    print(x)
    TableName = x.split("=")[-1].replace("\n", "").strip()
    print(TableName)
table=dynamodb.Table(TableName)

@app.route("/")
def index():
    items = [
        {
        "id": "skagen_skw6327",
        "name": "Skagen",
        "description": "Skagen Men's SKW6327 Hagen Stainless Steel Mesh Watch",
        "image": "skagen_skw6327.png"
    },
    {
        "id": "skagen_titanium",
        "name": "Skagen",
        "description": "Skagen Connected Men's Holst Titanium Hybrid Smartwatch",
        "image": "skagen_titanium.png"
    },
    {
        "id": "fossil_smartwatch_gen4",
        "name": "Fossil Smartwatch",
        "description": "Fossil Men's Gen 4 Explorist HR Stainless Steel Touchscreen Smartwatch with Heart Rate, GPS, NFC, and Smartphone Notifications",
        "image": "fossil_smartwatch_gen4.png"
    },
    {
        "id": "fossil_nate_stainless",
        "name": "Fossil Nate Stainless",
        "description": "Fossil Men's Nate Stainless Steel Hybrid Smartwatch with Activity Tracking and Smartphone Notifications",
        "image": "fossil_nate_stainless.png"
    },
    {
        "id": "apple_series5",
        "name": "Apple Series 5",
        "description": "Apple Watch Series 5 (GPS, 40mm) - Space Gray Aluminum Case with Black Sport Band",
        "image": "apple_series5.png"
    },
    {
        "id": "samsung_smartwatch",
        "name": "Samsung smartwatch",
        "description": "Samsung Galaxy Smartwatch (46mm) Bluetooth - Silver/Black",
        "image": "samsung_smartwatch.png"
    },
    {
        "id": "tagheuer_carrera",
        "name": "Tag Heuer",
        "description": "Mens Tag heuer Carrera Calibre Heuer 01 Automatic Chronograph 45 MM CAR2A1W.BA0703",
        "image": "tagheuer_carrera.png"
    },
    {
        "id": "Casio Analog Black Dial Men's Watch-MTP-VT01L-1BUDF (A1615)",
        "name": "Casio",
        "description": "Casio Analog Black Dial Men's Watch-MTP-VT01L-1BUDF (A1615)",
        "image": "Casio Analog Black Dial Men's Watch-MTP-VT01L-1BUDF (A1615).PNG"
    },
    {
        "id": "Casio Enticer Analog Black Dial Men's Watch - MTP-VD01G-1BVUDF (A1367)",
        "name": "Casio",
        "description": "Casio Enticer Analog Black Dial Men's Watch - MTP-VD01G-1BVUDF (A1367)",
        "image": "Casio Enticer Analog Black Dial Men's Watch - MTP-VD01G-1BVUDF (A1367).PNG"
    },
    {
        "id": "Casio Enticer Analog Blue Dial Men's Watch - MTP-1314D-2AVDF (A551)",
        "name": "Casio",
        "description": "Casio Enticer Analog Blue Dial Men's Watch - MTP-1314D-2AVDF (A551)",
        "image": "Casio Enticer Analog Blue Dial Men's Watch - MTP-1314D-2AVDF (A551).PNG"
    },
    {
        "id": "Casio Enticer Analog Blue Dial Men's Watch - MTP-VD01D-2EVUDF (A1364)",
        "name": "Casio",
        "description": "Casio Enticer Analog Blue Dial Men's Watch - MTP-VD01D-2EVUDF (A1364)",
        "image": "Casio Enticer Analog Blue Dial Men's Watch - MTP-VD01D-2EVUDF (A1364).PNG"
    },
    {
        "id": "Casio Enticer Analog Silver Dial Men's Watch - MTP-V001D-7BUDF (A1082)",
        "name": "Casio",
        "description": "Casio Enticer Analog Silver Dial Men's Watch - MTP-V001D-7BUDF (A1082)",
        "image": "Casio Enticer Analog Silver Dial Men's Watch - MTP-V001D-7BUDF (A1082).PNG"
    },
    {
        "id": "Casio Enticer Chronograph Black Dial Men's Watch - MTP-1374L-1AVDF (A834)",
        "name": "Casio",
        "description": "Casio Enticer Chronograph Black Dial Men's Watch - MTP-1374L-1AVDF (A834)",
        "image": "Casio Enticer Chronograph Black Dial Men's Watch - MTP-1374L-1AVDF (A834).PNG"
    },
    {
        "id": "Casio Youth-Combination Analog-Digital Gold Dial Men's Watch - AEQ-110BW-9AVDF (AD206)",
        "name": "Casio",
        "description": "Casio Youth-Combination Analog-Digital Gold Dial Men's Watch - AEQ-110BW-9AVDF (AD206)",
        "image": "Casio Youth-Combination Analog-Digital Gold Dial Men's Watch - AEQ-110BW-9AVDF (AD206).PNG"
    },
    {
        "id": "casio-MTP-v300D-1AUDF(A1173)",
        "name": "Casio",
        "description": "casio-MTP-v300D-1AUDF(A1173)",
        "image": "casio-MTP-v300D-1AUDF(A1173).PNG"
    },
    {
        "id": "casio-MTP-v300D-7AUDF(A1177)",
        "name": "Casio",
        "description": "casio-MTP-v300D-7AUDF(A1177)",
        "image": "casio-MTP-v300D-7AUDF(A1177).PNG"
    },
    {
        "id": "casio-MTP-vD01L-1EVUDF",
        "name": "Casio",
        "description": "casio-MTP-vD01L-1EVUDF",
        "image": "casio-MTP-vD01L-1EVUDF.PNG"
    },
    {
        "id": "scuderia_ferrari",
        "name": "Scuderia Ferrari",
        "description": "Scuderia Ferrari Men's Stainless Steel Quartz Watch with Silicone Strap, Black, 24 (Model: 830344)",
        "image": "scuderia_ferrari.png"
    },
    {
        "id": "armani_exchange",
        "name": "Armani Exchange",
        "description": "Armani Exchange Men's Classic Stainless Steel Watch",
        "image": "armani_exchange.png"
    },
    {
        "id": "casio_vintage_a168wa",
        "name": "Casio Vintage",
        "description": "Casio Men's Vintage A168WA-1 Electro Luminescence Watch",
        "image": "casio_vintage_a168wa.png"
    }
    ]
    for i in items:
        table.put_item(Item=i)
    return render_template('demo.html', name=items)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
