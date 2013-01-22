# DO NOT EDIT DIRECTLY!
# This file was generated automatically by GenStackDefines.py
# on Mon, 21 Jan 2013 22:55:02
#

components = {
   0: "NULL",
   1: "OPENWSN",
   2: "IDMANAGER",
   3: "OPENQUEUE",
   4: "OPENSERIAL",
   5: "PACKETFUNCTIONS",
   6: "RANDOM",
   7: "RADIO",
   8: "IEEE802154",
   9: "IEEE802154E",
  10: "RES_TO_IEEE802154E",
  11: "IEEE802154E_TO_RES",
  12: "RES",
  13: "NEIGHBORS",
  14: "SCHEDULE",
  15: "OPENBRIDGE",
  16: "IPHC",
  17: "FORWARDING",
  18: "ICMPv6",
  19: "ICMPv6ECHO",
  20: "ICMPv6ROUTER",
  21: "ICMPv6RPL",
  22: "OPENTCP",
  23: "OPENUDP",
  24: "OPENCOAP",
  25: "TCPECHO",
  26: "TCPINJECT",
  27: "TCPPRINT",
  28: "UDPECHO",
  29: "UDPINJECT",
  30: "UDPPRINT",
  31: "RSVP",
  32: "OHLONE",
  33: "HELI",
  34: "IMU",
  35: "RLEDS",
  36: "RREG",
  37: "RWELLKNOWN",
  38: "RT",
  39: "REX",
  40: "RXL1",
  41: "RINFO",
  42: "RHELI",
  43: "RRUBE",
  44: "LAYERDEBUG",
  45: "UDPRAND",
  46: "UDPSTORM",
  47: "UDPLATENCY",
  48: "TEST",
}

errorDescriptions = {
   1: "received an echo request",
   2: "received an echo reply",
   3: "getData asks for too few bytes, maxNumBytes={0}, fill level={1}",
   4: "the input buffer has overflown",
   5: "unknown transport protocol {0} (code position {1})",
   6: "wrong TCP state {0} (code position {1})",
   7: "TCP reset while in state {0} (code position {1})",
   8: "unsupported port number {0} (code position {1})",
   9: "unexpected DAO (code position {0})",
  10: "unsupported ICMPv6 type {0} (code position {1})",
  11: "unsupported 6LoWPAN parameter {1} at location {0}",
  12: "no next hop",
  13: "invalid parameter",
  14: "invalid forward mode",
  15: "neighbors table is full (max number of neighbor is {0})",
  16: "there is no sent packet in queue",
  17: "there is no received packet in queue",
  18: "schedule overflown",
  19: "wrong celltype {0} at slotOffset {1}",
  20: "unsupported IEEE802.15.4 parameter {1} at location {0}",
  21: "got desynchronized at slotOffset {0}",
  22: "synchronized at slotOffset {0}",
  23: "large timeCorrection of {0} ticks (code location {1})",
  24: "wrong state {0} in end of frame+sync",
  25: "wrong state {0} in startSlot, at slotOffset {1}",
  26: "wrong state {0} in timer fires, at slotOffset {1}",
  27: "wrong state {0} in start of frame, at slotOffset {1}",
  28: "wrong state {0} in end of frame, at slotOffset {1}",
  29: "maxTxDataPrepare overflows while at state {0} in slotOffset {1}",
  30: "maxRxAckPrepapare overflows while at state {0} in slotOffset {1}",
  31: "maxRxDataPrepapre overflows while at state {0} in slotOffset {1}",
  32: "maxTxAckPrepapre overflows while at state {0} in slotOffset {1}",
  33: "wdDataDuration overflows while at state {0} in slotOffset {1}",
  34: "wdRadio overflows while at state {0} in slotOffset {1}",
  35: "wdRadioTx overflows while at state {0} in slotOffset {1}",
  36: "wdAckDuration overflows while at state {0} in slotOffset {1}",
  37: "busy sending",
  38: "sendDone for packet I didn't send",
  39: "no free packet buffer (code location {0})",
  40: "freeing unused memory",
  41: "freeing memory unsupported memory",
  42: "unsupported command {0}",
  43: "unknown message type {0}",
  44: "wrong address type {0} (code location {1})",
  45: "isBridge mismatch (code location {0})",
  46: "header too long, length {1} (code location {0})",
  47: "input length problem, length={0}",
  48: "booted",
}
