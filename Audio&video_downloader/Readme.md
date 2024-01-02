<h1>-First run command :: pip install -r requirements.txt</h1>


<h2>
<b>For output::</b>

<l>python main.py -v "[YouTube Video URL]"   (for video)</l>
<l>python main.py -a -v "[YouTube Video URL]"   (for audio)</l>
</h2>
<br>
<p>
To download age-restricted videos, you need to provide Pytube with YouTube API credentials, including an API key and OAuth client ID.
This allows Pytube to authenticate and access age-restricted content.

Here's a general guide on how to use Pytube with API credentials:

1.Get API Key and OAuth client ID:
  -Go to the Google Cloud Console.
  -Create a new project (or select an existing one).
  -Enable the YouTube Data API v3 for your project.
  -Create credentials (API Key and OAuth client ID).

2.Configure Pytube:
  -Modify your main.py script to include the API key and OAuth client ID.

3.Provide API Key and OAuth Client ID:
  -You need to set your API key and OAuth client ID in your Pytube script. Update the script with the obtained credentials.

**Remember to keep your credentials secure, and do not share them publicly.** 

