from fastapi import APIRouter
from fastapi import Depends
from .tasks import send_email_report_dashboard
from auth.base_config import current_user

router = APIRouter(
    prefix='/report'
)





@router.get('/dashboard')
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    print('sending mail')
    return{
        'status':200,
        'data':'mail send',
        'details':None
    }
    
    
    