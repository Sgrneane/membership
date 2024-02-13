import pandas as pd
from .models import Membership
from account.models import CustomUser

def bulk_import(request):
    if request.method == 'POST':
        pandas = pd.read_excel('your_excel_file.xlsx')
        
        