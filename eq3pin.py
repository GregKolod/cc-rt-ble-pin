# EQ3 serial to PIN
# based on https://github.com/sunflower-seed/cc-rt-ble-pincheck

serial = "aaannnnnnn"

pin=0

arr = bytes(serial, 'utf-8')

pin  =  int((bin((arr[3]) ^ (arr[7]))),2)%10 * 1000
pin  +=  int((bin((arr[4]) ^ (arr[8]))),2)%10 * 100
pin  +=  int((bin((arr[5]) ^ (arr[9]))),2)%10 * 10
pin  +=  int((bin((arr[6]- 48) ^ (arr[0] -65))),2)%10

print("PIN:", pin)
