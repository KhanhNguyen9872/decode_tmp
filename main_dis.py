from subprocess import getoutput
from marshal import loads
from zlib import decompress
from base64 import b32decode,b16decode,b64decode
from inp import original_enc

a=b16decode(original_enc[::-1])
a=decompress(a)
with open('out.py','w') as f:
    f.write(f"decompile={a}")
a=getoutput(r"python dis_out.py")
print(a.split()[12])
if (a.split()[12][1:-1][:2]=="b'") and (a.split()[12][1:-1][-1]=="'"):
    original_enc="original_enc="+a.split()[12][1:-1]
    z='inp.py'
else:original_enc=a;z='final.py';print("Done!")


with open(z,'w') as f:
    f.write(original_enc)


## write to pyc file
# import importlib, sys
# pyc_data = importlib._bootstrap_external._code_to_timestamp_pyc(<code-object-here>)    
# open('file.pyc','wb').write(pyc_data)