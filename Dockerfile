FROM ubuntu:latest
LABEL authors="yvasi"

ENTRYPOINT ["top", "-b"]