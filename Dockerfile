FROM alpine:3.20

# Install necessary packages
RUN apk add --no-cache \
    git=2.45.2-r0 \
    bash=5.2.26-r0 \
    gawk=5.3.0-r1 \
    sed=4.9-r2 \
    perl=5.38.2-r0 \
    grep=3.11-r0

RUN git config --global --add safe.directory /repo

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]