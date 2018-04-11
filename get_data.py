from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"trump, banana","format":"png"}   #creating list of arguments

response.download(arguments)   #passing the arguments to the function
