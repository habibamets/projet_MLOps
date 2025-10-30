FROM python:3.10-slim 
#use slim to reduce the size of the final image

#setting the working directory : crée un dossier /app dans le conteneur
WORKDIR /app

#Copy the requirements file into the container
COPY requirements.txt .

#Install the dependencies
#on pourrait rajouter --no-cache-dir pour pip install pour éviter de stocker (garde une copie) les fichiers temporaires
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code into the container
COPY api/ ./api/

#expose the port the app runs on
EXPOSE 8000

#command to run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

