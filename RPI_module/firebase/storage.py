from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
# cred = credentials.Certificate("../private_lol/firebase-sdk.json")
# initialize_app(cred, {
#     'storageBucket': 'covid-rapid-screener.appspot.com'
# })

# Put your local file path 
def put_image_in_storage(path_to_image):
    bucket = storage.bucket()
    blob = bucket.blob("./image"+ path_to_image)
    blob.upload_from_filename("./image"+ path_to_image)

class storage:

    def __init__():
        cred = credentials.Certificate("../private_lol/firebase-sdk.json")
        initialize_app(cred, {
            'storageBucket': 'covid-rapid-screener.appspot.com'
        })
        self.bucket = storage.bucket()
        print("storage bucket reference created")

    

# fileName = "myImage.jpg"
# bucket = storage.bucket()
# blob = bucket.blob(fileName)
# blob.upload_from_filename(fileName)

# # Opt : if you want to make public access from the URL
# blob.make_public()

# print("your file url", blob.public_url)