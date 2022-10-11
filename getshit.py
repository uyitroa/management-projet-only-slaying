import requests
import json
from bs4 import BeautifulSoup

# # url = 'https://centralesupelec.edunao.com/my/'

auth = json.load(open("config.json"))

login_data = {'username': auth["mail"], 'password': auth["password"], 'execution': 'e29a17b0-84ce-4e63-9811-8cbb89127454_ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LjJZYkxtckdIQUdCbU9RVlJNQzdNVlNiTEJkODBfWjBjUkhEeDd2TlM5SXppYmhkaXpzQ1NCRnU4SjZMbDBBR0R6OUhKT3A4MVMxZDZHMWVWYWpwQ1RvM0xuMjlPZ2t6TkFmMVgxZm54b0xuRVlaUGVvY2ZONW45VjRBajd2cjVacWlJMTBsZlFiU2JtZU5aN1JOTE9qNTdyZGlqd3pPaHZpUUF3VG44U3RGTjZndmtOb0ZITnlpT1VQVjdNVDZhLUlVQ1d3Z2l1RVh5RWhJOF83UzI4alVhMGdNbG5pNGlLTFp4NkdfRG1VeGVHRjVuM21NOTZ0NE1xWmxvTGVGanZ2TS0zVEMwMFpsTnlITVJSdHpjMkhTV01TUUxWZVNSc0pycEYya0lsTWpXZVBlT183c0U1UlRUTDQyVHI0RFoyZ2lQMGF0WERNcmFDbW5FNllMLTZaZE1UZW0tTW1iYTRybUgweWFLeS1vQlRmX3plcm5NNDllbkxHOW11WlhfMnBQVFFybjF1T1U2REoxU20xblplMVlMX18xdnFvU0hIaGF5Zk1ia0NNck1hZGRCVUc1d1Q3NFhCODBMTFlxRy1pa3RXdTRsWnRCNG1HWVNaMklzclduLVFfRzdWckw0RlM0SkxhTU1rUWNwUEJ0cGNnOTltRnBqaEstd1FiR01SYXV1RFRtNXNsTnFSR002ZzM5YzFfRG8xRXJqVFQ2SVJuUzI3Qk5tUlNYM05IZ0h5SHVZbS0zZ25JNW1lY1ZkVFUwY0VtN0hDRm15T0ZFOExPbmNxeGRQcWo4SEhGYlpOWXdWeTBlVks3QVNTb190Qmw2azFFTGZkSGlfM0x5TmNYdG1QdnVnVVlSUGJFc012b1ZCR1d3bUY3cTBXN3FDV09hSUQ0dHlLRXpDM3F0VEx3WE9zVGdsY0s1T2JOWFVvZ01uTFlvd25DcTJKaVhGbGVZWWdhR29uZ2EyelRaSEJfMDBtTGtMbUhJb1o3dTlyam5kMnZTUUhtRldKS3NBMXlSN1ZvRmxpMGxYYS0wd1ZMdDRtYWdSUUlpRkVDTVBrYkNPVDhHTXl5YVZfcnV6QTc5MXdxX29MT0EtallkaDJfZkMzZXFMSkFoaVpNOUxVbUlKajZzRTIxLWtZUWZmUmN0Zl96eWtWLWNnUVl4aGF3bjFJRkRHeHhReTRJdFA0ek5rWXdGSVh3Wkh3MFJZcnVUTDRBOFN1bkRVQU1ndEdOR0NFMUtoU3BRbllnZkV5UnE4eHBJNEtvZzZQZWdQanc4ZjJBOTE0dlozbjdaT3RuWDQwOE9hUTlfUzIwNG1ERHp2VE5ubXhraENCelJfbDdhMm9sOU5BNFNYNHhPcXhXRExCZGgzZlYtU09YZVZ2TnpDQks2b3R4b0Zmb0dpek0zZFR4YVNMOXhacndkNzY5WE1mbU55a2NDYlYuc1dSUHVRSjVTRTVpQ1h6S2hHTGhYa0JwRDZhTUZqaDVWZ0gxam5zZ01MZ256RWVnZUp1SnZjNTJfTjJjQkFkdzhGblZVV3VNTHNyMHhqZ0pkVEFFNGc=', '_eventId': 'submit'}

s = requests.Session()
s.post("https://cas.centralesupelec.fr/cas/login?service=https%3A%2F%2Fcentralesupelec.edunao.com%2Flogin%2Findex.php%3FauthCAS%3DCAS", login_data)

r1 = s.get("https://cas.centralesupelec.fr/cas/login?service=https%3A%2F%2Fcentralesupelec.edunao.com%2Flogin%2Findex.php%3FauthCAS%3DCAS&gateway=true")

cookiesdict = s.cookies.get_dict()
# print(cookiesdict)
cookiesvalue = cookiesdict["MoodleSessionsaclaycentrale"]

cookies = "MoodleSessionsaclaycentrale={}; intelliboardPage=module; intelliboardParam=105452; intelliboardTime=7".format(cookiesvalue)


sesskey_index = r1.text.find("sesskey")
sesskey = r1.text[sesskey_index + 10: sesskey_index + 20]
# print(r1.text[sesskey_index: sesskey_index + 30])
print("Session key:", sesskey)


headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Content-Length": "1255",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Cache-Control": "max-age=0"
}

url = "https://centralesupelec.edunao.com/mod/quiz/startattempt.php"

data = """cmid=105452&sesskey={}""".format(sesskey)

r = requests.post(url, data=data, headers=headers)
print(r.status_code)


url = r.history[1].url

attempt_index = url.find("attempt=")
attempt = url[attempt_index+8:attempt_index+14]
print(url)

data = """attempt=170057&cmid=105452&page=7&sesskey={}""".format(sesskey)
headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
}
r1 = s.get(url, headers=headers)
print(r1.status_code)

sequencecheck_index = r1.text.find("_:sequencecheck")
answerid = r1.text[sequencecheck_index - 9: sequencecheck_index - 2]
print("Answer id:", answerid)

headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Content-Length": "1255",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryhKPWcwAaFC4qgS1B",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/attempt.php?attempt=169438&cmid=105452&page=7",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
}


question_number = 5

def sendresponse(question_number, answerid, answer, attempt, sesskey):
	headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Content-Length": "1255",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryhKPWcwAaFC4qgS1B",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/attempt.php?attempt=169438&cmid=105452&page=7",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
}

	url = "https://centralesupelec.edunao.com/mod/quiz/processattempt.php?cmid=105452"
	data = f"""------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="{answerid}:{question_number}_:flagged"

	0
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="{answerid}:{question_number}_:flagged"

	0
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="{answerid}:{question_number}_:sequencecheck"

	1
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="{answerid}:{question_number}_answer"

	2
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="next"

	Page suivante
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="attempt"

	{attempt}
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="thispage"

	2
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="nextpage"

	3
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="timeup"

	0
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="sesskey"

	{sesskey}
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="scrollpos"


	------WebKitFormBoundaryhKPWcwAaFC4qgS1B
	Content-Disposition: form-data; name="slots"

	{question_number}
	------WebKitFormBoundaryhKPWcwAaFC4qgS1B--"""

	r = requests.post(url, data=data, headers=headers)
	print(r.status_code)


def sendresponses(question_numbers, answerid, answers, attempt, sesskey):
	url = "https://centralesupelec.edunao.com/mod/quiz/processattempt.php?cmid=105452"
	data = ""
	for i in range(len(question_numbers)):
		question = question_numbers[i]
		answer = answers[i]
		answer_string = f"""------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="{answerid}:{question}_:flagged"

0
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="{answerid}:{question}_:flagged"

0
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="{answerid}:{question}_:sequencecheck"

1
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="{answerid}:{question}_answer"

{answer}\n"""
		data += answer_string


	question_numbers = [str(i) for i in question_numbers]
	questionlist = ", ".join(question_numbers)

	data += f"""------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="next"

Page suivante
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="attempt"

{attempt}
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="thispage"

0
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="nextpage"

10
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="timeup"

0
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="sesskey"

{sesskey}
------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="scrollpos"


------WebKitFormBoundaryhKPWcwAaFC4qgS1B
Content-Disposition: form-data; name="slots"

{questionlist}
------WebKitFormBoundaryhKPWcwAaFC4qgS1B--"""


	headers = {
	"Host": "centralesupelec.edunao.com",
	"Connection": "keep-alive",
	"Content-Length": "1255",
	"Origin": "https://centralesupelec.edunao.com",
	"X-Requested-With": "XMLHttpRequest",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
	"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryhKPWcwAaFC4qgS1B",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Referer": "https://centralesupelec.edunao.com/mod/quiz/attempt.php?attempt=169438&cmid=105452&page=7",
	"Accept-Encoding": "gzip,deflate,br",
	"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	"Cookie": cookies,
	"Sec-Fetch-Site": "same-origin",
	"Cache-Control": "max-age=0"
	}

	url = "https://centralesupelec.edunao.com/mod/quiz/processattempt.php?cmid=105452"

	# print(data)

	r = requests.post(url, data=data, headers=headers)
	# print("Sending responses:", r.status_code)



def submit(attempt, sesskey):
	url = "https://centralesupelec.edunao.com/mod/quiz/processattempt.php"
	headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Content-Length": "1255",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/summary.php?attempt=170721&cmid=105452",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
	}
	data = f"attempt={attempt}&finishattempt=1&timeup=0&slots=&cmid=105452&sesskey={sesskey}"

	r = requests.post(url, data=data, headers=headers)
	# print("Submitting responses:", r.status_code)



def start(sesskey):
	headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Content-Length": "1255",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
	}
	data = f"cmid=105452&sesskey={sesskey}"
	url = "https://centralesupelec.edunao.com/mod/quiz/startattempt.php"
	r = requests.post(url, data=data, headers=headers)

	url = r.history[1].url
	attempt_index = url.find("attempt=")
	attempt = url[attempt_index+8:attempt_index+14]
	# print("Attempt:", attempt)

	url = r.history[1].url

	attempt_index = url.find("attempt=")
	attempt = url[attempt_index+8:attempt_index+14]
	print(url)

	data = """attempt=170057&cmid=105452&page=7&sesskey={}""".format(sesskey)
	headers = {
	    "Host": "centralesupelec.edunao.com",
	    "Connection": "keep-alive",
	    "Origin": "https://centralesupelec.edunao.com",
	    "X-Requested-With": "XMLHttpRequest",
	    "Cache-Control": "max-age=0",
	    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Accept": "text/html",
	    "Referer": "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452",
	    "Accept-Encoding": "gzip,deflate,br",
	    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
	    "Cookie": cookies,
	    "Sec-Fetch-Site": "same-origin",
	    "Cache-Control": "max-age=0"
	}
	r1 = s.get(url, headers=headers)
	print(r1.status_code)

	sequencecheck_index = r1.text.find("_:sequencecheck")
	answerid = r1.text[sequencecheck_index - 9: sequencecheck_index - 2]
	# print("Answer id:", answerid)
	return attempt, answerid


def getscore(sesskey):
	url = "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452"
	headers = {
    "Host": "centralesupelec.edunao.com",
    "Connection": "keep-alive",
    "Origin": "https://centralesupelec.edunao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html",
    "Referer": "https://centralesupelec.edunao.com/mod/quiz/view.php?id=105452",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cookie": cookies,
    "Sec-Fetch-Site": "same-origin",
    "Cache-Control": "max-age=0"
	}

	r = s.get(url, headers=headers)
	soup = BeautifulSoup(r.text, 'html.parser')
	tab = soup.find("table",{"class":"generaltable quizattemptsummary"})
	tab_body = tab.find('tbody')
	rows = tab_body.find_all('tr')
	note = 0
	num = 0
	rows.reverse()
	for row in rows:
		cell1value = row.find("td", {"class": "cell c1"})
		if "En cours" in cell1value.text:
			continue
		cellvalue = row.find("td", {"class": "cell c2"})
		note = cellvalue.text.replace(",", ".")
		note = float(note)

		cellnumber = row.find("td", {"class": "cell c0"})
		num = int(cellnumber.text)
		break

	print(f"------ Tentative: {num}, Note {note}/20 --------")

	return note


# attempt, answerid = start(sesskey)
# sendresponses([i+1 for i in range(20)], answerid, [3, 17, 17, 17, 1, 17, 17, 2, 17, 1, 17, 1, 3, 2, 0, 0, 0, 2, 0, 0], attempt, sesskey)
# submit(attempt, sesskey)
# getscore(sesskey)

# qcms = []

# from algo import *

# attempt = start(sesskey)
# answers = next_answers()
# sendresponses([i+1 for i in range(20)], answerid, answers, attempt, sesskey)
# submit(attempt, sesskey)
# current_score = getscore(sesskey)
# while current_score < 10:
# 	attempt = start(sesskey)
# 	answers = next_answers(current_score)
# 	sendresponses([i+1 for i in range(20)], answerid, answers, attempt, sesskey)
# 	submit(attempt, sesskey)
# 	current_score = getscore(sesskey)
