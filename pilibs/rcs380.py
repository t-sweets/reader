import nfc
import binascii
from nfc.tag.tt3 import Type3Tag


def read(express=False):
    clf = nfc.ContactlessFrontend('usb:054c:06c3')

    target_req = nfc.clf.RemoteTarget("212F")

    if express:
        target_req.sensf_req = bytearray.fromhex("0000030000")
    target_res = clf.sense(target_req, iterations=10, interval=0.01)

    if target_res is not None:
        tag = Type3Tag(clf, target_res)
        tag.sys = 3
        idm = binascii.hexlify(tag.idm).upper()
        clf.close()
        return str(idm)
    clf.close()
    return None


def scan():
    result = read(False)
    if result is not None:
        return result
    result = read(True)
    if result is not None:
        return result
    return None
