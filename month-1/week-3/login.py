import logging
import datetime

# set up the logger
logger = logging.getLogger('ScriptLogger')
logger.setLevel(logging.DEBUG)

log_filename = datetime.datetime.now().strftime('script_log_%Y-%m-%d.log')
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def login(username, password):
    # Use Error Handling to catch exceptions
    try:
        if username == 'admin' and password == 'password':
            logger.info('Login Successful')
            logger.debug('User: admin logged in successfully')
            return True
        else:
            raise ValueError('Login Failed!. Invalid Credentials')
            
    except Exception as e:
        logger.error(f'Error: {e}')
        return False
    finally:
        logger.info('Login Script function executed successfully')

def main():    
    # Test the login function
    login('admin', 'password')
    login('admin', 'wrongpassword')

if __name__ == "__main__":
    main()

