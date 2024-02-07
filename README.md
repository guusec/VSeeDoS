VSeeFace offers a remote tracking feature that makes it possible to pair with the VTube Studio iOS application.
<img src="https://github.com/guusec/VSeeDoS/assets/78179391/dc8ec463-4264-479b-8d82-4b293024e33a" height=324 width=324> 

Once paired, the iOS device will send unencrypted UDP packets to VSeeFace containing JSON payloads with values that map the puppeteer's movements to the model.

It's possible to spoof the origin IP of these UDP packets and render a user's session unusable as VSeeFace will not be able to distinguish legitimate UDP packets from spoofed ones.

As well, if the JSON payloads contain values of 10 digits or larger, this will cause VSeeFace to hang, causing a denial of service.

This script provides a proof of concept that can cause VSeeFace to hang from a single UDP packet.

This script affects the most recent release of VSeeFace (v1.13.38c2) and likely all versions prior with the remote tracking feature.
