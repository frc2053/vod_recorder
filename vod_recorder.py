import os
import sys
import subprocess

stream, name, poll_first, poll_rest, max_count = sys.argv[1:]

max_count = int(max_count)

first = True
poll = poll_first
count = 0
offset = 0
print(stream, name.format(count), poll_first, poll_rest)
#input()
while count < max_count:
    if os.path.exists(os.path.join("/mnt/volume_nyc1_01/frc_vods/", name.format(count + offset))):
        offset += 1
        continue

    subprocess.run(["./venv/bin/streamlink", stream, "best", "--hls-live-edge", "999999", 
			"--hls-live-restart", "--hls-segment-threads", "6", "--retry-streams", 
			poll, "-o", os.path.join("/mnt/volume_nyc1_01/frc_vods/", name.format(count + offset))])
    if first:
        poll = poll_rest
        first = False
    count += 1
