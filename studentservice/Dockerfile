# syntax=docker/dockerfile:1

# Build stage
FROM golang:1.17-alpine AS build

WORKDIR /app

# Copy go mod and sum files
COPY go.mod ./
COPY go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source code
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Production stage
FROM alpine:latest

WORKDIR /

COPY --from=build /app/main .

EXPOSE 5001

CMD ["./main"]
