import hashlib
import hmac
import urllib
import traceback


class MigsClient(object):

    def __init__(self, secure_token, vpc_url):
        self.secure_secret = secure_token.decode("hex")
        self.vpcURL = vpc_url

    def hash_all_fields(self, fields):
        field_names = fields.keys()
        field_names.sort()

        to_be_hashed = ''
        for key in field_names:
            print key, fields[key]
            if (len(key) > 0) and ((key[0:4] == "vpc_") or (key[0:5] == "user_")):
                to_be_hashed += key + "=" + fields[key] + "&"
        try:
            return self.hmac_sha256(self.secure_secret, to_be_hashed[0:len(to_be_hashed) - 1])
        except Exception:
            traceback.print_exc()

    def setup(self, fields):
        secure_hash = self.hash_all_fields(fields)
        fields["vpc_SecureHash"] = secure_hash

        # Create a redirection URL
        buf = self.vpcURL + '?'
        buf = buf + urllib.urlencode(fields) + "&vpc_SecureHashType=SHA256"

        return buf

    def hmac_sha256(self, key, msg):
        message = bytes(msg).encode('utf-8')
        hash_value = hmac.new(key, message, hashlib.sha256)
        return hash_value.hexdigest().upper()
