import reedsolo

rs = reedsolo.RSCodec(10)  # Create codec with 10 parity symbols
data = b"Example data"
encoded = rs.encode(data)
decoded = rs.decode(encoded)
print("Decoded:", decoded)
