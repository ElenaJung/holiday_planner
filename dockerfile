# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables for non-interactive and optimized Python output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the rest of the application code into the container
COPY . /app/

# Expose a port (e.g., 8000) on which the application will run
EXPOSE 8000

# Define the command to run your application using Gunicorn (you can change it if using another server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "holiday_planner.wsgi:application"]