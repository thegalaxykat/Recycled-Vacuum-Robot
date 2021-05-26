#!/bin/bash
cvlc v4l2:///dev/video0 --sout '#transcode{vcodec=mp2v,vb=800,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=http{mux=ts,dst=:8080/}}'