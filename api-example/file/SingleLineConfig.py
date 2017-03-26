import logging
import sys
import re;

class SingleLineConfig:
	LOG_NAME = "SingleLineConfig"
	LOG_FILENAME = 'SingleLineConfig.log'
	LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
	__log_format = logging.Formatter(LOG_FORMAT)
	__log_stream_handler = logging.StreamHandler(sys.stdout)
	__log_stream_handler.setFormatter(__log_format);
	__log_file_handler = logging.FileHandler(LOG_FILENAME)
	__log_file_handler.setFormatter(__log_format)
	logger = logging.getLogger(LOG_NAME)
	logger.addHandler(__log_stream_handler)
	logger.addHandler(__log_file_handler)
	logger.setLevel(logging.DEBUG)

	def __init__(self):
		self.m_path = ""
		self.m_dict = {}
		self.m_title_pattern = re.compile(r"\[(?P<title>\S+)\]")
		self.m_content_pattern = re.compile(r"(?P<key>\S+)\s*=\s*(?P<value>\S+)\s*#*.*")
		self.m_curr_title = ""
		self.m_curr_key = ""
		self.m_curr_value = ""

	def __def__(self):
		pass

	def GetValue(self, title, key):
		contents = self.m_dict.get(title)
		if contents:
			return contents.get(key)

		return None

	def Load(self, file_path):
		self.m_path = file_path
		with open(file_path, "r") as fd:
			while True:
				str_line = fd.readline()
				if not str_line:
					break

				str_line = str_line.strip()
				if str_line.find("#", 0, 1) != -1:
					continue

				print(str_line)

				title_mr = self.m_title_pattern.match(str_line)
				if title_mr:
					self.m_curr_title = title_mr.group("title")
					SingleLineConfig.logger.debug("match title %s", self.m_curr_title)
					assert(self.m_curr_title not in self.m_dict)
					self.m_dict[self.m_curr_title] = {}

				content_mr = self.m_content_pattern.match(str_line)
				if content_mr:
					self.m_curr_key = content_mr.group("key")
					self.m_curr_value = content_mr.group("value")
					SingleLineConfig.logger.debug("match Content %s=%s", self.m_curr_key, self.m_curr_value)
					assert(self.m_curr_title in self.m_dict)

					self.m_dict[self.m_curr_title][self.m_curr_key] = self.m_curr_value

		for title, contents in self.m_dict.items():
			for key, value in contents.items():
				print("title %s key %s value %s" % (title, key, value))



config = SingleLineConfig()
config.Load("data.txt") 
value = config.GetValue("title", "key1")
print("m_dict[title][key1] = %s" % (value))



