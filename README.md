# misc_scripts
Miscellaneous scripts

Instructions:
Use read_DBC_data_and_write_file.py to generate a Decoded CAN Messages file
	ie. "2020-03-24-16-42-54_CAN_Messages_Decoded_Messages.csv"

Using the Decoded Messages file, you can run:
	-radarPlotter.m
	-determineTrueOutputRates.m
	-dashCamRadarTrackOverlay.m
	
Details:
radarPlotter.m
	-This script will plot radar tracks in a lat/lon grid with respect to the vehicle.
determineTrueOutputRates.m
	-This script will determine the true output rates of all CAN messages using RANSAC.
dashCamRadarTrackOverlay.m
	-This scrip overlays the radar tracks on top of the dash cam video.
	NOTE:: The body-to-camera transformation is performed ad-hoc specifically for the time
	frame specified (132-145).  Because the RADAR tracks only provide a planar lat/lon
	coordinate location, this transformation will not necessarily translate to other portions
	of the video, especially when the gradient of the roads differ.

