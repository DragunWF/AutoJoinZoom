# AutoJoinZoom

![GitHub top language](https://img.shields.io/github/languages/top/DragunWF/AutoJoinZoom)
![Lines of code](https://img.shields.io/tokei/lines/github/DragunWF/AutoJoinZoom)
![GitHub repo size](https://img.shields.io/github/repo-size/DragunWF/AutoJoinZoom)

## Description

Hello! I created this mainly to automatically join my own zoom classes. The code is mainly
personalized for my own convenience but just in case if you wanna know how to get it to work
I'll be providing the details down below.

I had a script before that also auto-joins me to my zoom classes but with less features and
less reliability which you find at [this link](https://github.com/DragunWF/Python-Mini-Projects/blob/main/scripts/school/auto_join_zoom.py). I mainly created this new one as an improved version
of that script.

## Details

- To be able to join a zoom meeting, you first have to go to `config/settings.json` and inside
  the `"meetings"` property array, you have to set your zoom meetings there with its details such
  as the `"days"` of when the day of the week it occurs and `"hour"` of the hour it starts.
- You can ignore the `"chrome_profile"` property for now. I'm still planning a feature that uses it.
- The `"is_exe"` just asks if you're going to run the bot from an `.exe` file or from the source code.

```json
[
  {
    "chrome_profile": "",
    "is_exe": false,
    "meetings": [
      {
        "name": "Mathematics",
        "link": "https://zoom.us/j/<meeting_code>",
        "days": ["monday", "wednesday"],
        "hour": { "start": "12:00", "end": "12:40" }
      },
      {
        "name": "Media Information and Literacy",
        "link": "https://zoom.us/j/<meeting_code>",
        "days": ["tuesday", "thursday"],
        "hour": { "start": "13:55", "end": "14:35" }
      }
    ]
  }
]
```

- In the `"link"` you have to provide the zoom link that directly leads to the meeting. Once
  that time comes of when the zoom meeting starts. Your web browser is going to open that link
  you stored in the `"link"` property.
- As an extra convenience tip, make sure to check the checkbox circled with red in the image
  so you don't have to go through that confirmation tab over and over again whenever my code
  starts joining you.

![Picture of confirmation tab](img/on_browser_opened.PNG)

- There's also an **SQLite database** in the `sql` directory that just stores the meetings you join,
  of when you join them, and when you open the program.
- One last note, is that I mainly use this by compiling my program to an `.exe` file with pyinstaller
  then just changing the values in `config/settings.json` to my meetings. And of course, I hid them
  for privacy reasons.

## Contact

If you have any questions you can contact me via discord. My discord tag is **DragonWF#9321**.
