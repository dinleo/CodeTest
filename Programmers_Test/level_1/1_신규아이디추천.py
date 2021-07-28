import re

new_id = "123_.def"

# 1단계
new_id = new_id.lower()

# 2단계
m = re.findall('[\-_.a-z0-9]+', new_id)
new_id = "".join(m)

# 3단계
while(".." in new_id):
    new_id = new_id.replace("..",".")

# 4단계
new_id = new_id.lstrip('.')
new_id = new_id.rstrip('.')

# 5단계
if(new_id == ""):
    new_id = "a"

# 6단계

if(len(new_id) >= 16):
    new_id = new_id[0:15]
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')


if(len(new_id) == 1):
    new_id = new_id*3

if(len(new_id) == 2):
    new_id = new_id + new_id[-1]



print(new_id)

