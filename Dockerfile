FROM alpine:3.21

# Install necessary packages
RUN apk add --no-cache \
    git=2.45.2-r0 \
    bash=5.2.26-r0 \
    gawk=5.3.0-r1 \
    sed=4.9-r2 \
    perl=5.38.2-r0 \
    grep=3.11-r0

# Set the working directory inside the container    
WORKDIR /usr/src

# Copy any source file(s) required for the action
COPY entrypoint.sh .

# Configure the container to be run as an executable
ENTRYPOINT ["/usr/src/entrypoint.sh"]