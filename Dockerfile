FROM alpine:3.20

# Install necessary packages
RUN apk add --no-cache \
    git=2.32.0-r0 \
    bash=5.1.16-r0 \
    gawk=5.1.0-r0 \
    sed=4.8-r0 \
    perl=5.32.1-r0 \
    grep=3.6-r0

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]