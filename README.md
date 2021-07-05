# django-crm
A Customer relationship management system made using Django

This CRM consists of three posts:
- The Owner(Who has access to all agents and leads)
- The Agents(They are under the owner and control the leada)
- The Leads(They are the lowest level)

- The owner can enter agents and leads in the system. Once the owner adds agents in the system, their accounts are automatically created and an -mail is sent to the agents and leads with their username, email and temporary password to access the system.

- The owner can assign leads to agents and monitor which agent has which leads, the owner can unassign leads from agents and remove agents and leads.

<img src="assets/crm.jpg">

# How to run this: 


Download requirements:
```
pip install -r requirements.txt
```
Then run the python file:
```
python manage.py runserver 
```

# Features:
<img src="assets/agents.png" width="600px">

- You can create leads
- assign/un-assign them to agents 
- create different categories for leads
- add different leads to different categories.

<img src="assets/leads.png" width="600px">

<img src="assets/lead_detail.png" width="600px">

- Check different categories of leads for full management of the crm 

<img src="assets/categories.png" width="600px">

<img src="assets/categories_inside.png" width="600px">

# The Django-Apps
<table>
<thead>
    <th>Django-App</th>
    <th>Contains</th>
</thead>
<tr><td> agents </td><td>Contains the views for agents</td></tr>
<tr><td> leads </td><td>Dcontains most of the functioning of the website</td></tr>
<tr><td> djcrm </td><td>Main DJango-app</td></tr>
</table>
