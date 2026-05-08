import sys
import os
import struct
from collections import OrderedDict

BLOCKSIZE = 512
MAGIC = b"4348PRJ3"

#-------------------BTree-----------------------
class Btree:
    def __init__(self, path, mode='r+b', create=False):
        self.path = path

        if create: #file needs to be created
            if os.path.exists(path):
                raise FileExistsError("File already exists")
            self.f = open(path, 'w+b')

            #add header
            header = bytearray(BLOCKSIZE)
            header[0:8] = MAGIC
            header[8:16] = struct.pack(">Q", 0) #root id
            header[16:24] = struct.pack(">Q)", 1) #nextblock id
            self.f.write(header)
            self.f.flush()
        else:
            if not os.path.exists(path):
                raise FileNotFoundError("File doesn't exist")
            self.f = open(path,mode)
            header = self.f.read(BLOCKSIZE)
            if len(header) != BLOCKSIZE or header[0:8] != MAGIC:
                raise ValueError("Invalid index file")
        self._load_header()
        self.cache = NodeCache(self.f, max_nodes=3)

    def _load_header(self):
        self.f.seek(0)
        header = self.f.read(BLOCKSIZE)
        self.root_id = struct.unpack(">Q", header[8:16])[0]
        self.next_block_id = struct.unpack(">Q", header[16:24])[0]

    def insert(self, key, value):
        print("Btree insert");

    def search(self, key):
        print("Btree search");

    def close(self):
        self.cache.flush_all()
        self._write_header()
        self.f.close()

    def _write_header(self):
        header = bytearray(BLOCKSIZE)
        header[0:8] = MAGIC
        header[8:16] = struct.pack(">Q", self.root_id)
        header[16:24] = struct.pack(">Q", self.next_block_id)
        self.f.seek(0)
        self.f.write(header)
        self.f.flush()

#-----------------NodeCache------------------
class NodeCache:
    def __init__(self, f, max_nodes=3):
        self.f = f
        self.max_nodes = max_nodes
        self.cache = OrderedDict()

    def flush_all(self):
        for bid, node in self.cache.items():
            if node.dirty:
                self._write_block(bid, node.encode())
        self.cache.clear()


def main():	
    if len(sys.argv) < 2:
        print("Usage: project3.py <command> [args}", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]

    try:
        match cmd:
            case "create":
                if len(sys.argv) != 3:
                    raise RuntimeError("Usage: project3.py create <indexfile>")
                
                idxfile = sys.argv[2]
                if os.path.exists(idxfile):
                    raise RuntimeError("File already exists")

                btree = BTree(idxfile, create=True)
                btree.close()
            case "insert":
                if len(sys.argv) != 5:
                    raise RuntimeError("Usage: project3.py insert <indexfile> <key> <value>")
                
                key = sys.argv[3]
                value = sys.argv[4]
                btree = Btree(sys.argv[2])

                btree.insert(key, value)
                btree.close()
            case "search":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py search <indexfile> <key>")

                key = sys.argv[3]
                btree = Btree(sys.argv[2])

                value = btree.search(key)
                btree.close()
                if value is None:
                    raise RuntimeError("Key not found")
                print(f"{key}: {value}")
            case "load":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py load <indexfile> <csvfile>")
                print("case load")
            case "print":
                if len(sys.argv) != 3:
                    raise RuntimeError("Usage: project3.py print <indexfile>")
                print("case print")
            case "extract":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py extract <indexfile> <csvfile>")
                print("case create")
            case _:
                raise RuntimeError(f"Unknown command: {cmd}")
    except (RuntimeError, FileNotFoundError, FileExistsError, ValueError, IOError) as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
	main()
