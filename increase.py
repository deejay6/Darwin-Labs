import hashlib, uuid
import random
import datetime
from operator import setitem
salt = uuid.uuid4().hex  # generate salt to get more randomize hash key

data = "Dhananjay"  # This is my original Test Data

print "Original Data: ", data

weighted_data = ""  # Initialised String which will contain original_data + randomly added bits

final_string = [None]*len(data)  # Final_String contains the original data after removing extra bits

old_position = []  # This array stores the original position of elements as it is in original data

new_position =[]  # This array stores position of elements of original data in weighted_data

hashed_key = hashlib.sha1(salt).hexdigest()  # Generated hash key for adding bits

data = list(data)

# Added last digit of current timestamp  to length of original data to get variable length of weighted data
length_of_weighted_data = len(data) + int(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')[-1])

# This is an algo to generate weighted data by getting random elements from original data and hash key
for i in range(0, length_of_weighted_data):
    if len(list(set(data))) > 1:
        while True:
            char_from_original_data = random.choice(data)
            if char_from_original_data != None:
                break
        weighted_data = weighted_data.__add__(char_from_original_data)
        new_position.append(weighted_data.index(char_from_original_data))
        old_position.append(data.index(char_from_original_data))
        setitem(data,data.index(char_from_original_data), None)

    char_from_hash_key = random.choice(hashed_key)
    weighted_data = weighted_data.__add__(char_from_hash_key)

print "Weighted Data After Adding Random Bits : ", weighted_data

# This is for retrieving the original data
for j,k in zip(old_position,new_position):
    final_string[j] = weighted_data[k]
final_string = "".join(final_string)
print "Retrieved Data: ", final_string





