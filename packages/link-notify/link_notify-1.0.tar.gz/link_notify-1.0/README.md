Link_Notify
Simple notification creator with button package by progbits

visit us - https://progbits.xyz

For docs, tutorials and updates visit - https://progbits.xyz/link-notify
Installation-
`pip install link-notify`
Simple code to create a notification-
```Python
import link_notify as ln
ln.notify(
	"Text for notification under 40 characters",
	"link to open(example.com)",
	5, #time till notification disappears
	"text on button")
