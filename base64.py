import base64

text = "Abdullah Al Mamun Rifat"
text_to_bytes = text.encode("ascii")

base64_bytes = base64.b64encode(text_to_bytes)
base_string = base64_bytes.decode("ascii")

print(base_string)



base64_bytes_de = base_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes_de)
sample_string = sample_string_bytes.decode("ascii")

print(sample_string)
