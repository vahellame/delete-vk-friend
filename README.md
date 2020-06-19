## delete VK friend

### Step 1) Requirements

- Windows / Linux / macOS 10 (or Docker)
- Python 3.5+

### Step 2) Install

Run in your console:

```
sudo apt update && sudo apt -y dist-upgrade
sudo apt install -y git python3-venv 
git clone https://github.com/vahellame/delete-vk-friend.git
cd delete-vk-friend
```

View and edit `main.py`.

```
python3 -m venv venv
./venv/bin/pip install -U pip 
./venv/bin/pip install -r requirements.txt
```

### Step 3) Running

```
nohup $PWD/venv/bin/python $PWD/main.py 1> $PWD/out.txt 2> $PWD/errors.txt &
```
