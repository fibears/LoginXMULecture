# Secure a seat From XMU Lecture Website.

[Official Website](http://event.wisesoe.com/)

Students in School of Economics of Xiamen Univ. must attend a minimum number of lectures every semester and the number for grad students is ten. So the question arose when a student tries to reserve lectures in advance at the beginning of a semester: how to secure a seat of popular lectures? When everyone goes crazy to grab a ticket and it sold out as quickly as tickets of Jay Chou’s world concert tour or railroad tickets during Chunyun, what you can do to tackle with this annoying problem except for having a what-the-fucking-hell-happened face.Well, I’m one of the students and as a lazy man, I don’t like to seat in from of my laptop and wait till the Lecture Reserving Website releases lecture information. So I decided to write a Python script to automate the reservation process.## Pull Request ##

If you are interested in this project, you can fork my repo and pull your requset to compete this robot.
## How to run this robot?

Fortunately, I succeeded in developing the web robot. I have tested a lot of times and it seems working well. You just need to follow the instructions below to let the robot work for you:1. Install [Anaconda](https://www.continuum.io/downloads) on your computer2. Click the button Download ZIP on the top right of the page and download the whole materials in this page
3. Extract your downloaded files
4. Go to file-folder code, right-click auto.bat(Windows User) and choose edit (编辑); If you are OSX or Linux user, please edit the auto.sh
5. In the second-to-last line, please substitute the field of username and password by YOUR OWN username (i.e. your student ID) and password of Lecture Reserving Website, respectively. **注意，该程序目前还存在一个bug，现在只支持纯数字的密码！**
6. Save the auto.bat(or auto.sh) file
7. Click auto.bat file and the robot has sailed off to reserve seats for all available lectures!
8. Attention! If you are OSX or Linux user, you must run `chmod a+x auto.sh` in terminal before you run auto.sh file.

```bash
# Set path to '../LoginXMULecture/code'
chmod a+x auto.sh
./auto.sh
```Still didn’t reserve successfully for a lecture? No worry, my robot will help you secure your seat in advance, fast, free and friendly.
If you want to explore the operational logic of this website, please visit My Blog--[LectureRobot](http://fibears.top/2016/03/21/LectureRobot/).

## Features
### App Building(2016.06.02)
- Package the code to App.

### New Feature(2016.03.25)

- The robot support for printing the information of Lectures which you have reserved.