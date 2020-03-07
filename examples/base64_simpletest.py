import adafruit_base64 as base64

s0 = b"Aladdin:open sesame"
print(repr(s0))
s1 = base64.encodebytes(s0)
print(repr(s1))
s2 = base64.decodebytes(s1)
print(repr(s2))