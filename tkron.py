from optparse import OptionParser

import hashlib

parser = OptionParser("""
####### #    #  ######  ####### #     #
   #    #   #   #     # #     # ##    #
   #    #  #    #     # #     # # #   #
   #    ###     ######  #     # #  #  #
   #    #  #    #   #   #     # #   # #
   #    #   #   #    #  #     # #    ##
   #    #    #  #     # ####### #     #

Starting TKRON
Hashs :

md5 sha1 sha224 sha256 sha384 sha512 blake2b blake2s sha3_224 sha3_256 sha3_384 sha3_512


""")
parser.add_option("-A", dest = "Hash", help = "The Type Of Hash")
parser.add_option("-K", dest = "Kay", help = "The Text You Want To Hash")
(options, args) = parser.parse_args()

hashs = ["md5",  "sha1",  "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s",
        "sha3_224", "sha3_256", "sha3_384", "sha3_512"]


Hash = str(options.Hash)

Kay = str(options.Kay)

if options.Hash is None:
    print(parser.usage)
    if options.Hash in hashs:
        print('Ok')
    else:
        exit()
        
if options.Kay is None:
    print("ERROR In Kay")

print(parser.usage)

h = hashlib.new(Hash)
Kay = Kay.encode("utf-8")
h.update(Kay)
print('Your ' + Hash + ' hash value: ',h.hexdigest())


