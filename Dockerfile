FROM alpine:3.20

# Install necessary packages
RUN apk add --no-cache \
    git \
    bash \
    gawk \
    sed \
    perl \
    grep

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]