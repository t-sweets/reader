import binascii
import nfc
import sys


class CardReader(object):

    @classmethod
    def read(cls, express=False):
        try:
            clf = nfc.ContactlessFrontend('usb')
        except IOError:
            raise Exception("FeliCa device error")
        target_req = nfc.clf.RemoteTarget("212F")
        if express:
            target_req.sensf_req = bytearray.fromhex("0000030000")
        target_res = clf.sense(target_req, iterations=10, interval=0.01)
        if target_res is not None:
            sys.stdout.write(binascii.hexlify(target_res.sensf_res))
            clf.close()
            return 2
        return 1

    @classmethod
    def scan(cls):
        while True:
            if CardReader.read(False) == 2:
                break
            if CardReader.read(True) == 2:
                break


if __name__ == '__main__':
    CardReader.scan()
