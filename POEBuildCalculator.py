import os

DIV = 245
MAGEBLOOD = 320


class POEBuildCalculator:

	# Constructor
	def __init__(self, file):
		self.file = file
		self.price = 0
		self.report = dict()
		self.sorted_report = dict()
		self.gear = dict()
		self.jewels = dict()
		self.gems = dict()


##################################################################

	def run(self):
		self.createReport()
		self.createdSortedReport()
		self.calculatePrice()

	def convertToDiv(self, value):

		if "c" in value:
			value = float(value[:value.index(" ")].strip())
			value = round(value / DIV, 1)

		else:
			value = float(value[:value.index(" ")].strip())

		return value

	def calculatePrice(self):

		for k, v in self.report.items():

			for i in v:
				if i == "Belt" and v[i] != MAGEBLOOD: v[i] = MAGEBLOOD
				self.price += v[i]

	def createReport(self):
		categories = []
		category = ""
		with open(self.file) as f:
			lines = f.readlines()

		for line in lines:
			line = line.strip()
			if line == "": continue
			if ":" not in line:
				category = line
				categories.append(category)
				continue

			key = line[:line.index(":")].strip()
			value = line[line.index(":") + 1:].strip()
			value = self.convertToDiv(value)

			if category == "Gear":

				self.gear.update({key: value})

			elif category == "Jewels":

				self.jewels.update({key: value})

			elif category == "Gems":

				self.gems.update({key: value})

		nested_report = dict()
		categories_list = [self.gear, self.jewels, self.gems]

		for category, key_item_pair in zip(categories, categories_list):
			nested_report[category] = key_item_pair

		self.report = nested_report

	def createdSortedReport(self):

		if not self.report:
			print("Missing Report")
			return

		res = {
		 key: dict(sorted(val.items(), key=lambda ele: ele[1], reverse=True))
		 for key, val in self.report.items()
		}

		self.sorted_report = res

	# Print the report to console
	def printReport(self):

		option = int(
		 input('''Which type of report do you wish to see?
1. Original report
2. Sorted report\n> '''))
		os.system("clear")

		if option == 1: report = self.report
		elif option == 2: report = self.sorted_report

		if not bool(report):
			print("Missing Report")
			return

		s1 = "{:{col1}} | {:{col2}}"
		s2 = "{:>{col1}} | ~{} div"
		s3 = "\t{:{col1}} | {:{col2}} div"
		width1, width2, width3, width4 = 34, 5, 10, 30

		print(s1.format("Item", "Price", col1=width1, col2=width2))
		print(s1.format("=" * width1, "=" * width3, col1=width1, col2=width2))

		for category, kv_pair in report.items():
			print(s1.format(category, "", col1=width1, col2=width2))
			for key, value in kv_pair.items():
				print(s3.format(key, value, col1=width4, col2=width2))

		print(s1.format("=" * width1, "=" * width3, col1=width1, col2=width2))
		print(s2.format("Total", round(self.price), col1=width1))
		print(
		 s2.format("Total w/o Mageblood", round(self.price) - MAGEBLOOD,
		           col1=width1))
