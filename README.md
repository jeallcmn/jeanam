# Running

Launch mod-host
```bash
mod-host -n -v
```

Launch Soopor Loopr with default proline
(Quantize dub, Quantize Record, Quantize Mute, Sync, Play Sync )

```bash
slgui -L default.slsess 
```

Configure Hydrogen
* Disable automatic play
* Disable auto c5onnect to jack system outputs (we want to connect them to reverb)

Launch Hydrogen in headless mode with test song containing drum patterns

```bash
h2cli -s test.h2song
```

Launch ttymidi to capture footpedal via serial

```bash
./ttymidi -s /dev/ttyUSB0 -v -n foot_controller
```
