import sqlite3
import random
import logging
import hashlib
import binascii
import base64

logging.basicConfig(level=logging.DEBUG)

cnn = sqlite3.connect("try-api.db")
cursor = cnn.cursor()

create_tb_cmd = '''
    create table if not exists human (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hash_val INTEGER
        name TEXT
    );
'''
cursor.execute(create_tb_cmd)

insert_cmd = '''
    insert into human (name) values (?);
'''
insert_name = "name_{}".format(random.randint(0, 99999999))
ret = cursor.execute("insert into human (name) values(?)", (insert_name,))

logging.debug("insert result {}".format(ret))
cnn.commit()

select_cmd = '''
    select * from human;
'''

rows = cursor.execute(select_cmd)
for row in rows:
    #logging.debug("row detail {}".format(row))
    pass

logging.debug("--------------------------------------")
logging.debug("insert name {}".format(insert_name))
m = hashlib.md5()
m.update(insert_name.encode())
logging.debug("digit {}".format(m.digest()))
logging.debug("hexdigest {}".format(m.hexdigest()))

logging.debug("--------------------------------------")
dk = hashlib.pbkdf2_hmac("sha256", b'password', b'salt', 512)
logging.debug(dk)
logging.debug("pbkdf2_hmac result {}".format(binascii.b2a_hex(dk)))

logging.debug("--------------------------------------")
#base64.b64encode base64.b64decode 都返回bytes
#base64.b64encode接受bytes并返回encode_bytes
#可以把encode_bytes decode为字符串，参见ret_str，作为base64.b64decode的输入
#base64.b64decode的输入无论是encode_bytes还是ret_str得到的返回值都一样。（返回值是bytes）

ret = base64.b64encode(insert_name.encode())
ret_str = ret.decode()
logging.debug("b64encode result {} :: {}".format(ret, ret_str))


ret = base64.b64decode(ret)
ret_str = base64.b64decode(ret_str)
logging.debug("b64decode result {} :: {}".format(ret, ret_str))

#str.encode() -> binary
#binary.decode() -> str
str_encode_data = "lxl罗小龙".encode()
str_decode_data = str_encode_data.decode()
logging.debug("--------------------------------------")
logging.debug("encode ret {}".format(str_encode_data))
logging.debug("decode ret {}".format(str_decode_data))