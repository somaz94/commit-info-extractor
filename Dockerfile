FROM alpine:3.22

# Install necessary packages
RUN apk add --no-cache \
    git \
    bash \
    gawk \
    sed \
    perl \
    grep

# Set the working directory inside the container    
WORKDIR /usr/src

# Copy any source file(s) required for the action
COPY entrypoint.sh .

# Configure the container to be run as an executable
ENTRYPOINT ["/usr/src/entrypoint.sh"]