raspivid -o - -t 0 -rot 180 -w 640 -h 480 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8010}' :demux=h264

cvlc v4l2:///dev/video0 --v4l2-width 640 --v4l2-height 480 --v4l2-chroma h264 --sout '#standard{access=http,mux=ts,dst=0.0.0.0:12345}'

raspivid -t 0 -w 640 -h 480 -ih -fps 20 -o - | nc -l 2222