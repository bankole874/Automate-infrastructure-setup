import subprocess

def create_user(username, group):
    try:
        # Create the group if it doesn't exist
        subprocess.run(['sudo', 'groupadd', group], check=True)
    except subprocess.CalledProcessError:
        # Group already exists
        pass
    
    try:
        # Create the user and assign to the group
        subprocess.run(['sudo', 'useradd', '-m', '-G', group, username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

def create_users_and_groups(users):
    for username, group in users.items():
        create_user(username, group)

users = {
    'andrew': 'system_administrators',
    'julius': 'legal',
    'chizi': 'human_resources',
    'jeniffer': 'sales',
    'adeola': 'business_strategists',
    'bach': 'ceo',
    'gozie': 'it_interns',
    'ogochukwu': 'finance'
}

create_users_and_groups(users)
