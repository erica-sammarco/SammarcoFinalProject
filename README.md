# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 2 docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the `webapp` user. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## For setting up a Conda Web-Dev environment:

1. `conda create -n webdev python=3.9`
1. `conda activate webdev`
1. `pip install flask flask-mysql flask-restful cryptography flask-login`

# CHAARG Weekly Workout Management System
## Video Pitch
https://user-images.githubusercontent.com/68513658/207464376-8a47373d-4a34-4087-ba6d-ca73638001c8.mp4

## Application Summary
CHAARG is a national organization that focuses on the empowerment of women in fitness, and it has chapters at many universities across the country including Northeastern. Each week, we host workouts at different fitness studios across the city. This systems helps manage those events and allows members to sign-up to attend.

In the current app prototype, there are three user types: General CHAARG Members, CHAARG Committee Members, and CHAARG Executive-Board Members.

From the home screen, you can choose to act as any of those three user types.

<img width="1266" alt="CHAARG Weekly Workout Management System Welcome Screen" src="https://user-images.githubusercontent.com/68513658/207450000-0b0fe099-15c8-4042-8314-8554448e2dc5.png">

## CHAARG Member
As a General CHAARG Member, you have the ability to see all public event sessions. 
You can choose to sign-up for any of these event sessions. If they have reached capacity, you can join the waitlist. 
At any time, you can change your own sign-up or waitlist status for any event. 
You can also view Event Details to see more information about an event session as well as reviews for the studio. 
<img width="1410" alt="General CHAARG Member Event Screen" src="https://user-images.githubusercontent.com/68513658/207450374-be901f1a-5839-4d66-9279-2336a6bd1048.png">
<img width="1290" alt="General CHAARG Member Event Details Screen" src="https://user-images.githubusercontent.com/68513658/207450500-0909ea3f-1c89-4434-bd70-c22828784a6f.png">
In this app prototype, you can choose to impersonate any CHAARG Member from the dropdown.

For the CHAARG Committee Members and CHAARG E-Board Members there is no member-specific information so there is no need for this dropdown. 

## CHAARG Committee Member
A CHAARG Committee Member can also view all public event sessions, but they have access to more information such as event capacity, sign-ups and waitlist. 
The CHAARG Committee Member can adjust the sign-up and waitlist for event sessions. 
<img width="1370" alt="CHAARG Committee Member Event Screen" src="https://user-images.githubusercontent.com/68513658/207450934-b98d5b34-4587-4cc5-a2fb-1785178f57ba.png">
<img width="1118" alt="CHAARG Committee Member Manage Sign-Ups Screen" src="https://user-images.githubusercontent.com/68513658/207450952-aa647317-4085-4371-b057-4f6849ad5886.png">

## CHAARG E-Board Member
A CHAARG Executive Board Member can see all events and toggle their publicity. 
These users can also add Weekly Events and Event Sessions to the DB.
<img width="1311" alt="CHAARG E-Board Events Screen" src="https://user-images.githubusercontent.com/68513658/207451134-98248812-0ae3-4b6c-a335-aecfb74846ad.png">
<img width="988" alt="CHAARG E-Board Add Event Screen" src="https://user-images.githubusercontent.com/68513658/207451151-05568616-13b3-44ce-b359-99a6e15d9508.png">
<img width="1123" alt="CHAARG E-Board Event Details Screen" src="https://user-images.githubusercontent.com/68513658/207451161-ac3cade8-9b5b-41ae-95d6-6512f21bfdbe.png">
<img width="775" alt="CHAARG E-Board Add Event Session Screen" src="https://user-images.githubusercontent.com/68513658/207451179-44d9d4de-a5e0-4cb1-a36a-8230cb5d9cf5.png">

A Studio might not have any instructors. This field is optional so if there are no choices in the dropdown, it can be left blank. 
