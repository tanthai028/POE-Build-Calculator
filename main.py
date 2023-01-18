from POEBuildCalculator import POEBuildCalculator


def main():
	file = "test.txt"
	pbc = POEBuildCalculator(file)
	pbc.run()
	pbc.printReport()


if __name__ == "__main__":
	main()
