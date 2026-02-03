# syntax=docker/dockerfile:1

# Build stage
FROM maven:3.8.4-openjdk-17 AS build

WORKDIR /app

# Copy the pom.xml
COPY pom.xml .

# Copy the source code
COPY src ./src

# Build the project and create the fat JAR
RUN mvn clean package -DskipTests

# Production stage
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Copy the JAR from the build stage
COPY --from=build /app/target/teacherservice-1.0.0.jar .

EXPOSE 5002

CMD ["java", "-jar", "teacherservice-1.0.0.jar"]
