from django.contrib.auth.models import User

def load_sample_data(delete=False):
    # This method will load sample data to the app (ie. sample users, items etc.)  
    if delete==True:
        delete_sample_data()
    
    print("load_sample_data not implemented.")
    
def delete_sample_data():
    print("delete_sample_data not implemented.")

def create_admin_user(username, email, password):
    admin_exists = User.objects.filter(username=username).exists()
    if not admin_exists:
        User.objects.create_superuser(username, email, password)
