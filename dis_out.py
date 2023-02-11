import dis,marshal
from out import decompile
dis.dis(marshal.loads(decompile))
