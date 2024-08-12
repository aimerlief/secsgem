# Handler

{py:class}`secsgem.hsms.protocol.HsmsProtocol` has the basic HSMS connection handling build in.
It automatically selects and deselects the link and performs a periodic linktest.
It also replies to incoming HSMS requests like linktest automatically.

```python
>>> def on_connect(event, data):
...     print "Connected"
...
>>> client = secsgem.hsms.HsmsProtocol("10.211.55.33", 5000, False, 0, "test")
>>> client.events.connected += on_connect
>>> client.enable()
Connected
>>> client.send_linktest_req()
secsgem.hsms.HsmsPacket({'header': secsgem.hsms.HsmsHeader({'function': 0, 'stream': 0, 'p_type': 0, 'system': 7, 'session_id': 65535, 'require_response': False, 's_type': 6}), 'data': ''})
>>> client.disable()
```

The handler has functions to send requests and responses and wait for a
certain response.

## Events

Events of the handler can be received with the help of
`secsgem.common.EventHandler`{.interpreted-text role="class"}. The
handler sends the following events:

| Event name | Description |
|---|---|
| connected | Connection was established |
| communicating | Connection was selected |
| disconnected | Connection was terminated |

For an example on how to use these events see the code fragment above.
