# Django Authentication System

***User Objects***
---


There are 3 types of users in Django that the authentication system provides :
- Superusers
- Staff
- User


These are the user objects core to the authentication system.

---

***Note : When we migrate the first time in django there it creates several tables related to User and authentication system.***

---

---

## Auth Users

---

After migration for the first time there create a table called auth users  which have the boolean values for the type of users you want to set particullary

The columns are 
- is_supersuer
- is_staff
- is_active


These are the classes that are really needed to label a partiular user and add particualar set of permissions.

---

---

## Creating a User (using command line / shell)



> First enter the virtual enviornment you have created.

        venv\Scripts\activate

> Enter the python shell

        python manage.py shell

> Create User steps :

        from django.contrib.auth.models import User

        u = User.objects.create_user('admin',password='admin')

        u.is_superuser=True

        u.save()


You can check your table <b style="font-size:18px;color:#4169e1">auth_user</b>

It will have a entry of the admin user with is_superuser set = 1.

The class <b style="font-size:16px;color:#4169e1">django.contrib.auth</b> have :
- Four default permissions:
    - add
    - change
    - delete
    - view
- Created for each django model


---

---

## Auth Permissions


There is another table called <b style="font-size:18px;color:#4169e1">auth_permissions</b> which have diffrent permissions that are set to assign to a user.



        id	content_type_id 	codename	      name
        1	1	            add_logentry	    Can add log entry
        2	1	            change_logentry	    Can change log entry
        3	1	            delete_logentry	    Can delete log entry
        4	1	            view_logentry	    Can view log entry
        5	2	            add_permission	    Can add permission
        6	2	            change_permission	Can change permission
        7	2	            delete_permission	Can delete permission
        8	2	            view_permission	    Can view permission
        9	3	            add_group	        Can add group
        10	3	            change_group	    Can change group
        11	3	            delete_group	    Can delete group
        12	3	            view_group	        Can view group
        13	4	            add_user	        Can add user
        14	4	            change_user	        Can change user
        15	4	            delete_user	        Can delete user
        16	4	            view_user	        Can view user
        17	5	            add_contenttype	    Can add content type
        18	5	            change_contenttype	Can change content type
        19	5	            delete_contenttype	Can delete content type
        20	5	            view_contenttype	Can view content type
        21	6	            add_session	        Can add session
        22	6	            change_session	    Can change session
        23	6	            delete_session	    Can delete session
        24	6	            view_session	    Can view session



Apart from <b style="font-size:18px;color:#4169e1">auth_user</b> and <b style="font-size:18px;color:#4169e1">auth_permissions</b>  tables there are more tables that are 
- <b style="font-size:18px;color:#4169e1">auth_user_user_permissions</b>
- <b style="font-size:18px;color:#4169e1">auth_group_permissions</b>

An auth_user table has a many to many relationship to auth_group table, you can say one user can be part of may groups and one group can have many users. In the similar way auth_user have many to many relationship with auth_permission table.

Therefore there are these link tables as <b style="font-size:18px;color:#4169e1">auth_user_user_permissions</b> to link <b style="font-size:18px;color:#4169e1">auth_permissions</b> and <b style="font-size:18px;color:#4169e1">auth_user  </b>


> Adding permissions to multiple groups can be done by add the users to a auth_group and apply thr permissions to the group that would be a better way to handle such situation

> You can also extend the permission table to a custom table if required in your application architecture.

> Super Users can access Every thing and other users may have a particular access to a certain context.

> We have to set permission to users to access certain section
