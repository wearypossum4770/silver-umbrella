import urllib.request
import xml.etree.ElementTree as ET

requestXML = """
<?xml version="1.0"?> 
<AddressValidateRequest USERID="693DRAGO4853">
<Revision>1</Revision>
<Address ID="0">
<Address1>SUITE K</Address1>
<Address2>29851 Aventura</Address2>
<City/>
<State>CA</State>
<Zip5>92688</Zip5>
<Zip4/>
</Address>
</AddressValidateRequest>
"""


def build_request(request_string):
    doc_string = request_string.replace("\n", "").replace("\t", "")
    parsed_doc_string = urllib.parse.quote_plus(doc_string)
    return f"https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML={parsed_doc_string}"


def submit_verification(url):
    content = {}
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print(f"Error making HTTP call:{response.info()}")
        exit()
    root = ET.fromstring(response.read())
    for address in root.findall("Address"):
        content.update(
            Address1=address.find("Address1").text,
            Address2=address.find("Address2").text,
            City=address.find("City").text,
            State=address.find("State").text,
            Zip5=address.find("Zip5").text,
            Zip4=address.find("Zip4").text,
        )
    return content


address = submit_verification(build_request(requestXML))
print(address)


def verify_address(raw_address):
    return submit_verification(build_request(requestXML))


{
    "ckqib0rxk0000hsveixloydmx" "Address1": "STE K",
    "Address2": "29851 AVENTURA",
    "City": "RANCHO SANTA MARGARITA",
    "State": "CA",
    "Zip5": "92688",
    "Zip4": "2014",
}
