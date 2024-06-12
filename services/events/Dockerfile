# Use the official Node.js 16 image
FROM node:16

# Create and set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 5001
EXPOSE 5001

# Run the app
CMD ["npm", "start"]
