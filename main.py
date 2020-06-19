import random
import time

import vk_api

vk_session = vk_api.VkApi("YOUR_VK_LOGIN", 'YOUR_VK_PASSWORD')
vk_session.auth()

vk = vk_session.get_api()

while True:
    try:
        vk.friends.delete(user_id=int("FRIEND_ID_TO_DELETE"))
    except:
        pass

    time.sleep(random.randint(1, 42) * 600)
