# Secure a seat From XMU Lecture Website.

[Official Website](http://event.wisesoe.com/)

Students in School of Economics of Xiamen Univ. must attend a minimum number of lectures every semester and the number for grad students is ten. So the question arose when a student tries to reserve lectures in advance at the beginning of a semester: how to secure a seat of popular lectures? When everyone goes crazy to grab a ticket and it sold out as quickly as tickets of Jay Chou’s world concert tour or railroad tickets during Chunyun, what you can do to tackle with this annoying problem except for having a what-the-fucking-hell-happened face.Well, I’m one of the students and as a lazy man, I don’t like to seat in from of my laptop and wait till the Lecture Reserving Website releases lecture information. So I decided to write a Python script to automate the reservation process.## Pull Request ##

If you are interested in this project, you can fork my repo and pull your requset to compete this robot.
## How to run this robot?

Fortunately, I succeeded in developing the web robot. I have tested a lot of times and it seems working well. You just need to follow the instructions below to let the robot work for you:1. Download the `LectureRobot` app in `app` path
2. Unzip the file **LectureRobot.zip**
3. Double click the app `LectureRobot`
4. Please substitute the field of username and password by YOUR OWN username (i.e. your student ID) and password of Lecture Reserving Website, respectively. 注意，该程序目前还存在一个bug，现在只支持纯数字的密码！ 
5. Click the `GetCookie` Button, and wait a few seconds
6. Click the `GrabLecture` ButtonStill didn’t reserve successfully for a lecture? No worry, my robot will help you secure your seat in advance, fast, free and friendly.
If you want to explore the operational logic of this website, please visit My Blog--[LectureRobot](http://fibears.top/2016/03/21/LectureRobot/).

## Features
### V1.1 (2016.09.16)
- Update Robot UI

### V1.0 (2016.09.14)
- The first version

### App Building(2016.06.02)
- Package the code to App.

### New Feature(2016.03.25)

- The robot support for printing the information of Lectures which you have reserved.