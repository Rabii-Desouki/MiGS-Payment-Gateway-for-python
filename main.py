from migs import MigsClient


vpc_SecureHash = "YOUR_SECURE_HASH"
vpc_AccessCode = "YOUR_ACCESS_CODE"
vpc_Merchant = "YOUR_MERCHANT"
vpc_Url = "https://migs.mastercard.com.au/vpcpay"

client = MigsClient(vpc_SecureHash, vpc_Url)
fields = {
    "vpc_AccessCode": vpc_AccessCode,
    "vpc_Amount": "100",
    "vpc_Command": "pay",
    "vpc_Gateway": "ssl",
    "vpc_MerchTxnRef": "test",
    "vpc_Merchant": vpc_Merchant,
    "vpc_OrderInfo": "test",
    "vpc_ReturnURL": "https://masterpassdemo.appspot.com/jsp/JSP_VPC_3DS_2_5_Party_DR.jsp",
    "vpc_Version": "1"
}
res = client.setup(fields)
print (res)

