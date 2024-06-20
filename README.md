# Automate-infrastructure-setup

## Steps

- Set up Vagrant ubuntu vm.
```
vagrant up
vagrant ssh
```
- Create a github repository “Automate-infrastructure-setup”.
- Clone repository into ubuntu VM in vscode.
```
git clone https://github.com/bankole874/Automate-infrastructure-setup.git
```
- In the cloned repository create a python file named ```createUsers.py``` to create groups, create users and assign them to their respective groups.

| Users, Groups             |
| ----------------- |
|Andrew, System Administrator|
|Julius, Legal|
|Chizi, Human Resource Manager|
|Jeniffer, Sales Manager|
|Adeola, Business Strategist|
|Bach, CEO|
|Gozie, IT intern|
|Ogochukwu, Finance Manager|

- Create a python file named ```createDirectories.py``` to create directories.

| Directories             |
| ----------------- |
Finance Budgets
Contract Documents
Business Projections
Business Models
Employee Data
Company Vision and Mission Statement
Server Configuration Script

- Create a python file named ```promptUsers.py``` to prompt users to create new files into the existing directories.

## Screenshots

- Checking the newly created file
![1](https://github.com/bankole874/Automate-infrastructure-setup/blob/main/images/Checking%20the%20newly%20created%20file.png)

- Committing changes to github
![2](https://github.com/bankole874/Automate-infrastructure-setup/blob/main/images/Committing%20changes%20to%20github.png)

- Checking the groups, users created
![3](https://github.com/bankole874/Automate-infrastructure-setup/blob/695e7e1031d30fc760a7858ad41c1c4e7703f471/images/Checking%20the%20groups%2C%20users%20created.png)

- Checking the newly created file
![4](https://github.com/bankole874/Automate-infrastructure-setup/blob/main/images/Listing%20the%20directories%20created.png)
