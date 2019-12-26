# YoutubeCommentTakerOutter
A few lines of python to take the comments from YouTube videos without using the API
## Usage
```python
import Youtubecommenttakeroutter
```
This imports the library so that you can use it. Once you have imported it, using it is super simple.
```python
GetComments("video url", number of comments, comment prefix)
```
Here is an example!
```python
GetComments("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 30, "comment:")
```
The output will be at least 30 comments and it will look something like this
```text
comment: Nice video!
comment: Bad Video!
```
