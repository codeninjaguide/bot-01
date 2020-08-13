# Public dataset fo HSN codes
# https://github.com/datasets/harmonized-system

# Gst upadates and news
# https://www.gst.gov.in/newsandupdates

# Income tax updates and news
# https://www.incometaxindiaefiling.gov.in/moreNewsUpdates

# TO DO
	# Upcoming tax payment dates
	# Income tax rates information https://cleartax.in/s/income-tax-slabs
	# GST reconciliation sheet
	# TDS reconciliation sheet
	# Accounting firm near me
	# Latest job from Indeed

import re
import time
import wget

def verify_gst(number):
	reg = '^([0][1-9]|[1-2][0-9]|[3][0-7])([a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9a-zA-Z]{1}[zZ]{1}[0-9a-zA-Z]{1})+$'

	if (len(number) < 15):
		print("GST number should be of 15 digits. Only {} digits has been provided!".format(len(number)))
		return "invalid"

	if (re.search(reg, number)):
		return "valid"
	else:
		return "invalid"

	return


def validate_pan_number(number):
	if (len(number) < 10):
		print("PAN number should be of 10 digits. Only {} digits has been provided!".format(len(number)))
		return

	if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', number):
		print("Valid PAN Number")
	else:
		print("Invalid PAN Number")


def hsn_code_info():
	pass


def img_download(url):
	# http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg
	data_folder = '/home/vishalchopra/Desktop/CA helper bot/public/'
	file_id = wget.download(url)
	print("***\n")
	print(file_id)
	return file_id


if __name__ == '__main__':
	img_download('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')

# # def test():
# # 	return ["ME {}".format(x) for x in range(1, 10)]

# if __name__ == '__main__':

# 	# print(test())

# 	# num = '19AAACW6953H1ZX'
# 	# num1 = '1AA2ACW6953H1ZX'
# 	# num2 = '19AAACW6A53H1ZX'

# 	# verify_gst(num)
# 	# verify_gst(num1)
# 	# verify_gst(num2)

# 	# validate_pan_number('AAACW6953H')
# 	# validate_pan_number('AAACWA953H')
# 	# validate_pan_number('AACWA953H')