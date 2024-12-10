FROM alpine:3.21

# Install necessary packages
RUN apk add --no-cache \
    git=2.47.1-r0 \
    bash=5.2.37-r0 \
    gawk=5.3.1-r0 \
    sed=4.9-r0 \
    perl=5.40.0-r0 \
    grep=3.11-r0

# Set the working directory inside the container    
WORKDIR /usr/src

# Copy any source file(s) required for the action
COPY entrypoint.sh .

# Configure the container to be run as an executable
ENTRYPOINT ["/usr/src/entrypoint.sh"]