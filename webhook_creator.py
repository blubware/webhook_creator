import random, string, requests, time, json
from clear_screen import clear

def neon():
    try:
        clear()

        token = input('Token: ')
        channel = input('Channel ID: ')
        name = input('Webhook name, blank for random: ')

        if name == '':
            name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

        while True:

            webhook_url = f'https://discord.com/api/v9/channels/{channel}/webhooks'
            post_webhook = requests.post(webhook_url, headers={'authorization': token}, json={'name': name})

            match post_webhook.status_code:
                case 200:
                    print(f'Made 1 webhook called {name}')

                case 429:
                    response = post_webhook.text
                    response_content = json.loads(response)
                    ratelimit = response_content.get('retry_after')
                    print(f'Sleeping for {ratelimit}')
                    time.sleep(ratelimit)
            

    except KeyboardInterrupt:
        neon()

if __name__ == '__main__':
    neon()

    