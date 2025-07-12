# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

package kata

import "fmt"

func clean(r int) int {
  if r < 0 {
    return 0
  } else if r > 255 {
    return 255
  }
  return r
}


func RGB(r, g, b int) string {
  r = clean(r)
  g = clean(g)
  b = clean(b)
  return fmt.Sprintf("%02X%02X%02X", r, g, b)
}