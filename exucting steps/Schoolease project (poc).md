# Schoolease project (poc)

### work done on 

1. Api bulid 
   1. user registration 
   2. edit user details
2. admin panel
   1. filter on email and username
   2. hide user password ,last_login,created_date from admin
   3. create a user from admin panel

## process for execution

```python
pip install requirment.txt
```

```python
py manage.py makemigrations
py mangage.py migrations

```

Creation of super user ( admin user)

```python
py manage.py createsuperuser
email:test@schoolease.com
username:test
category: school
password:test@schoolease.com
password2:test@schoolease.com
```

```python
py manage.py runserver
```



### Api normal user registration

#### POST REQUEST

```python
http://127.0.0.1:8000/api/schoolease/register
```

please check the below image for the passing of the data for the creation of the user registration

![](D:\personal_projects\django_projects\schoolease\exucting steps\user registration.PNG)

 

After submitting ( success message look like this )

![](D:\personal_projects\django_projects\schoolease\exucting steps\success message of user registration.PNG)

#### GET REQUEST

To get the details of the user 

```python
http://127.0.0.1:8000/api/schoolease/<user email id>
```

![](D:\personal_projects\django_projects\schoolease\exucting steps\get_userinfo_email.PNG)

![](D:\personal_projects\django_projects\schoolease\exucting steps\display_get_userinfo.PNG)

#### PUT REQUEST

to change the details of the user 

```python
http://127.0.0.1:8000/api/schoolease/edituser/<user email id>
```

![](D:\personal_projects\django_projects\schoolease\exucting steps\edit_user_info.PNG)

![](D:\personal_projects\django_projects\schoolease\exucting steps\update_user_info.PNG)

### admin panel

the admin panel can be access by

```python
http://127.0.0.1:8000/admin
```

Enter the  super user(admin user) created above

```html
email : test@schoolease.com
password: test@schoolease.com
```

To view the users created and there information go to Accounts

the look of the admin panel

![](D:\personal_projects\django_projects\schoolease\exucting steps\admin_panel.PNG)

Here we have search box to filter the user based on the email and username(which are unique while creating the user profile)

the look of the user profile can be seen as

![](D:\personal_projects\django_projects\schoolease\exucting steps\admin_panel_user_profile.PNG)