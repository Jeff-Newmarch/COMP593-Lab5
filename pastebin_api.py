import requests

DEVELOPER_KEY = 'ZqMrfP-peJ8xU6MLdDGGUDindM0OvDIc' 
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("This is a title", "This\nis\nthe body", "1H", True)
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public paste to PasteBin

    Args:
        title (str): Pate title
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of past (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to False.

    Returns:
        str: URL of the new paste, if successful. None if unsuccessful
    """
    # Setup the parameters for the request message
    paste_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private': 0 if listed else 1
    }

    # Send the POST request to the PasteBin API
    print('Posting new paste to PasteBin...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data=paste_params)
    
    #Check whether the POST was successful
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    else:
        print('failure')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')



if __name__ == '__main__':
    main()