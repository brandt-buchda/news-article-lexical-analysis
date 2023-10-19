from pywebcopy import save_webpage

url = 'https://www.nytimes.com/2023/10/03/us/politics/trump-stolen-election.html'
download_folder = 'articles/'

kwargs = {'bypass_robots': False, "project_name": "NYT"}
save_webpage(url, download_folder, **kwargs)

print("DONE!")