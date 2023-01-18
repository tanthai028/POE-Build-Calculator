# 	# Create the console string print-out report of the prices
# 	def createReport(self):
# 		keys, values = [], []
# 		with open(self.file) as f:
# 			lines = f.readlines()

# 			for elem in lines:
# 				elem = elem.strip()
# 				if elem in ["Jewels", "Gems", "Gear", ""]: continue
# 				key = elem[:elem.index(":")].strip()
# 				value = elem[elem.index(":") + 1:].strip()
# 				keys.append(key)
# 				values.append(value)

# 			self.setReport(dict(zip(keys, values)))

# # Print the report to console
# 	def printReport(self):
# 		if not self._report:
# 			print("Missing Report")
# 			return

# 		print("{:30} | {:5}".format("Item", "Price"))
# 		print("{:30} | {:5}".format("=" * 30, "=" * 10))

# 		for item, price in self._report.items():
# 			print("{:30} | {:5}".format(item, price))

# 		print("{:30} | {:5}".format("=" * 30, "=" * 10))
# 		print("{:>30} | ~{} div".format("Total", round(self.getPrice())))

# 	def printSortedReport(self):

# 		if not self._sorted_report:
# 			print("Missing Report")
# 			return

# 		print("{:30} | {:5}".format("Item", "Price"))
# 		print("{:30} | {:5}".format("=" * 30, "=" * 10))

# 		for item, price in self._sorted_report.items():
# 			print("{:30} | {:5} div".format(item, price))

# 		print("{:30} | {:5}".format("=" * 30, "=" * 10))
# 		print("{:>30} | ~{} div".format("Total", round(self.getPrice())))

# # Calculate the price of the build
# def calculatePrice(self):


# 	with open(self.file) as f:
# 		lines = f.readlines()

# 	for line in lines:
# 		price_div, price_chaos = 0, 0
# 		line = line.strip()
# 		if ":" not in line: continue
	
# 		price_string = line[line.index(":") + 1:].strip()

# 		if "div" in price_string:

# 			price_div = price_string[:price_string.index("div")].strip()

# 		elif "c" in price_string:

# 			price_chaos = price_string[:price_string.index("c")].strip()

# 		sum = float(price_div) + (float(price_chaos) / div)
# 		self.setTotal(sum)